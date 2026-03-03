# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch20250120

### Purpose
Updates the status and related records for a batch of DTC authorization requests, enforcing workflow rules, access checks, and zone‑usage constraints.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit OUTPUT | Indicates whether the procedure completed without errors. |
| @Message | NVARCHAR(500) OUTPUT | Stores a descriptive error or status message when the procedure fails. |
| @str | TAMS_DTC_AUTH READONLY | Table‑valued input containing rows of username, authid, workflowid, statusid, val, valstr, powerzoneid, type, and spksid to process. |

### Logic Flow
1. **Transaction Setup**  
   - If no outer transaction exists, start an internal transaction and flag it for later commit or rollback.

2. **Cursor Iteration**  
   - Open a cursor over the rows supplied in @str.  
   - For each row, load the values into local variables.

3. **Access Verification**  
   - Retrieve the current workflow status (`@WFStatusID`) for the supplied `@workflowid`.  
   - Retrieve the TOA status (`@toastatus`) linked to the authorization record.  
   - Determine the user’s access rights by checking duty roster and endorser tables for the current access date.  
   - If the user lacks access, set an error message and jump to the error handler.

4. **Workflow Validation**  
   - If the supplied `@WFStatusID` is not one of the terminal states (6 or 13), confirm that the workflow exists in `TAMS_Depot_Auth_Workflow`.  
   - If missing, set an error message and abort.

5. **Zone‑Usage Checks**  
   - For status 14, ensure the SPKS zone is not already assigned to another active TAR.  
   - (Power‑zone conflict logic is present but commented out.)

6. **Duplicate Update Prevention**  
   - If the workflow record for this authid and workflowid already has a non‑null status and checkbox value, abort with an error.

7. **Determine Next Status**  
   - Compute `@newstatusid` as the next active status in the `TAMS_WFStatus` sequence for the DTCAuth workflow type.

8. **Update Current Workflow**  
   - Set the workflow status to “Completed” for checkboxes or to the supplied `@valstr` for dropdowns.  
   - Record the acting user and timestamp.  
   - Store the checkbox value if applicable.

9. **Insert Next Workflow Step**  
   - Identify the next workflow ID in the sequence.  
   - Insert a new workflow record with null status and action fields, unless the current status is one of the terminal states (7, 4, 5, 6, 11, 12, 14).

10. **Special Status Actions**  
    - **Status 7 (Surrender)** – Update the auth record’s status, insert the next workflow, and set the action fields.  
    - **Status 10** – Increment the power‑zone status ID.  
    - **Status 3** – Record SPKS protection off timing and type.  
    - **Status 4** – Record power‑off timing, type, and update status.  
    - **Status 11** – Record power‑on timing, type, and update status.  
    - **Status 14** – Record SPKS protection on timing, type, and update status.  
    - **Statuses 5 or 6** – Record racked‑out timing, type, and update status.  
    - **Status 12** – Record racked‑in timing, type, update status, and adjust SPKS status for zones not yet completed.

11. **Post‑Status Status Transition**  
    - For statuses 4, 5, 6, 11, 12, or 14, determine the next workflow status (`@checkstatus`).  
    - If all related zones have reached the required status, advance the auth record’s status, update the current workflow record, and insert the next workflow step.

12. **Cancellation Handling**  
    - If the TOA status indicates a cancellation (status 6), adjust the new status based on whether the cancellation pertains to a train‑movement or DTC‑specific scenario, ensuring the auth record moves to the appropriate completion state.

13. **Final Auth Status Update**  
    - Update `TAMS_Depot_Auth` with the computed `@newstatusid`, timestamp, and acting user, unless the current status is 7.

14. **Cursor Cleanup**  
    - Fetch the next row; repeat until all rows are processed.  
    - Close and deallocate the cursor.

15. **Error Handling**  
    - If any error occurs during processing, roll back the internal transaction, set `@success` to 0, and exit.  
    - On successful completion, commit the transaction, set `@success` to 1, and return.

### Data Interactions
* **Reads:**  
  - TAMS_WFStatus  
  - TAMS_TOA  
  - TAMS_Depot_Auth  
  - TAMS_Depot_Auth_Workflow  
  - TAMS_Roster_Role  
  - TAMS_OCC_Duty_Roster  
  - TAMS_User  
  - TAMS_Endorser  
  - TAMS_Depot_DTCAuth_SPKS  
  - TAMS_Depot_Auth_Powerzone  
  - TAMS_Power_Sector  
  - TAMS_Track_Power_Sector  
  - TAMS_Track_SPKSZone  

* **Writes:**  
  - TAMS_Depot_Auth_Workflow (UPDATE & INSERT)  
  - TAMS_Depot_Auth (UPDATE)  
  - TAMS_Depot_Auth_Powerzone (UPDATE)  
  - TAMS_Depot_DTCAuth_SPKS (UPDATE)