# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch

### Purpose
Updates a batch of depot authorization records, advancing workflow stages, recording timing actions, and enforcing access and status rules.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit OUTPUT | Indicates overall success (1) or failure (0). |
| @Message | nvarchar(500) OUTPUT | Stores error or status message. |
| @str | TAMS_DTC_AUTH READONLY | Table-valued parameter containing rows of username, authid, workflowid, statusid, val, valstr, powerzoneid, type, spksid to process. |

### Logic Flow
1. **Transaction Setup** – If no outer transaction, start an internal one and set a flag.  
2. **Cursor Iteration** – For each row in @str:  
   a. Retrieve current workflow status (`@WFStatusID`) and TOA status (`@toastatus`).  
   b. Determine operation date based on a cutoff time; if the cutoff has passed, use yesterday’s date, otherwise today.  
   c. **Access Check** – Verify that the user has a duty roster entry for the operation date and workflow; if not, set error message and jump to error handling.  
   d. **Workflow Validity** – Ensure the workflow exists in `TAMS_Depot_Auth_Workflow`; if missing, error.  
   e. **Resource Conflict Checks** –  
      - If status is 14, confirm the SPKS zone isn’t already used by another TAR with status 8.  
      - (Power‑zone conflict logic is commented out.)  
   f. **Duplicate Update Check** – If the workflow record already has a non‑null status and checkbox value, error.  
   g. **Next Status Calculation** – Find the next workflow status ID (`@newstatusid`) from `TAMS_WFStatus`.  
   h. **Current Workflow Update** – Update the current workflow record with action details, unless the status is one of a set of excluded values.  
   i. **Insert Next Workflow** – Insert a new workflow row for the next status, unless the current status is excluded.  
   j. **Special Status Actions** – For specific `@WFStatusID` values (7, 10, 3, 4, 12, 14, 5/6, 11):  
      - Update related tables (`TAMS_Depot_Auth`, `TAMS_Depot_Auth_Powerzone`, `TAMS_Depot_DTCAuth_SPKS`) with timing, type, action by, and new status IDs.  
      - For status 7, also enable the line‑clear stage by updating the main auth record.  
   k. **Post‑Status Transition Logic** – For statuses that require moving to the next overall status:  
      - Determine the next overall status (`@newstatus`) based on whether all related power‑zone or SPKS records have reached the required status.  
      - Update the main auth record and insert a new workflow record with the new status.  
   l. **Cancellation Handling** – If the TOA status indicates a cancellation, adjust the new status based on specific cancellation scenarios.  
   m. **Final Auth Update** – Update `TAMS_Depot_Auth` with the new status and audit fields, unless the status is 7.  
3. **Error Handling** – If any error occurs during processing, rollback the transaction and set `@success` to 0.  
4. **Commit** – On successful completion, commit the transaction and set `@success` to 1.

### Data Interactions
* **Reads:**  
  - TAMS_WFStatus  
  - TAMS_TOA  
  - TAMS_Depot_Auth  
  - TAMS_Workflow  
  - TAMS_Parameters  
  - TAMS_OCC_Duty_Roster  
  - TAMS_Roster_Role  
  - TAMS_User  
  - TAMS_Endorser  
  - TAMS_Depot_Auth_Workflow  
  - TAMS_Depot_Auth_Powerzone  
  - TAMS_Depot_DTCAuth_SPKS  
  - TAMS_Track_Power_Sector  
  - TAMS_Track_SPKSZone  
  - TAMS_Power_Sector  
  - TAMS_Depot_Auth_Powerzone (for conflict checks)  

* **Writes:**  
  - TAMS_Depot_Auth_Workflow (update & insert)  
  - TAMS_Depot_Auth (update)  
  - TAMS_Depot_Auth_Powerzone (update)  
  - TAMS_Depot_DTCAuth_SPKS (update)  

---