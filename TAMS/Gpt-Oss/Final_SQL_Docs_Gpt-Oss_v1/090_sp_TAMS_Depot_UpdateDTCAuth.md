# Procedure: sp_TAMS_Depot_UpdateDTCAuth

### Purpose
Updates a specific step of a DTC authorization workflow, advancing status, recording timestamps, and applying related changes to power zone or SPKS records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | User performing the update |
| @authid | int | Identifier of the DTC authorization record |
| @workflowid | int | Identifier of the workflow step being processed |
| @statusid | int | Current status identifier for the workflow |
| @val | bit | Checkbox value (used when @type = 1) |
| @valstr | nvarchar(50) | String value for dropdown or status text (used when @type = 2) |
| @powerzoneid | int | Power zone identifier (used for certain workflow steps) |
| @success | bit OUTPUT | Flag set to 1 on success, 0 on error |
| @type | int | 1 = checkbox, 2 = dropdown |
| @spksid | int | SPKS identifier (used for specific workflow steps) |
| @Message | nvarchar(500) OUTPUT | Error or status message returned on failure |

### Logic Flow
1. **Transaction Setup** – Begins a new transaction if none is active.  
2. **Access Check** – Verifies that the user has an endorser role linked to the specified workflow. If not, sets an error message and exits.  
3. **Workflow Validation** – For most workflows (except IDs 139 and 141), confirms the workflow exists in `TAMS_Depot_Auth_Workflow`. If missing, errors out.  
4. **Duplicate Update Prevention** – Checks if the workflow step has already been updated (non‑NULL status and checkbox value). If so, errors out.  
5. **Next Status Determination** – Retrieves the next active status ID from `TAMS_WFStatus` based on the current `@statusid`.  
6. **Current Workflow Update** – Sets the current workflow’s status to “Completed” (if checkbox) or to `@valstr`, records the acting user and timestamp, and records the checkbox value if applicable. This is skipped for a predefined list of workflow IDs.  
7. **Next Workflow Insertion** – Determines the next workflow ID and inserts a new record into `TAMS_Depot_Auth_Workflow` for the next step, unless the current workflow is in the excluded list.  
8. **Special Step Actions** – Executes specific updates based on `@workflowid`:  
   - **126** – Updates `ProtectOffTiming`, `ProtectOffType`, and `ProtectOffActionBy` in `TAMS_Depot_DTCAuth_SPKS`.  
   - **127** – Updates power‑off fields and status in `TAMS_Depot_Auth_Powerzone`.  
   - **135** – Updates power‑on fields and status in `TAMS_Depot_Auth_Powerzone`.  
   - **137** – Updates protect‑on fields and status in `TAMS_Depot_DTCAuth_SPKS`.  
   - **131 / 139** – Updates racked‑out fields and status in `TAMS_Depot_Auth_Powerzone`.  
   - **136** – Updates racked‑in fields and status in `TAMS_Depot_Auth_Powerzone`, then updates `StatusID` in `TAMS_Depot_DTCAuth_SPKS` for a set of SPKS records that meet complex criteria.  
9. **Status Advancement for Composite Workflows** – For workflow IDs 127, 131, 139, 135, 136, or 137:  
   - Determines a `checkstatus` value based on the current workflow ID.  
   - If the workflow is 137, verifies that no SPKS records have a status below `checkstatus`. If none, increments the overall authorization status, updates the main auth record, updates the workflow record, and inserts a new workflow record marked “Completed”.  
   - For other IDs, performs a similar check against power‑zone records, then updates the main auth record, workflow record, and inserts a new workflow record with null status.  
10. **Fallback Status Update** – If the workflow ID is not in the composite set, simply updates the main auth record’s status to the next status ID.  
11. **Error Handling** – If any error occurs during the process, rolls back the transaction, sets `@success` to 0, and exits.  
12. **Commit** – On successful completion, commits the transaction, sets `@success` to 1, and returns.

### Data Interactions
* **Reads**  
  - `TAMS_Endorser`  
  - `TAMS_User_Role`  
  - `TAMS_User`  
  - `TAMS_Depot_Auth_Workflow`  
  - `TAMS_WFStatus`  
  - `TAMS_Depot_Auth`  
  - `TAMS_Depot_Auth_Powerzone`  
  - `TAMS_Depot_DTCAuth_SPKS`  
  - `TAMS_Track_Power_Sector`  
  - `TAMS_Track_SPKSZone`  
  - `TAMS_Power_Sector`

* **Writes**  
  - `TAMS_Depot_Auth_Workflow` (UPDATE and INSERT)  
  - `TAMS_Depot_DTCAuth_SPKS` (UPDATE)  
  - `TAMS_Depot_Auth_Powerzone` (UPDATE)  
  - `TAMS_Depot_Auth` (UPDATE)  

---