# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationCCByParameters

### Purpose
Updates the status of an OCC authorisation workflow for a DTL line, advances the workflow to the next level, records the change, and logs audit entries.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the update |
| @OCCAuthID | int | Primary key of the OCC authorisation record |
| @OCCLevel | int | Current workflow level being processed |
| @Line | nvarchar(10) | Line identifier; only 'DTL' triggers processing |
| @TrackType | nvarchar(50) | Optional track type used in audit records |
| @RemarksCC | nvarchar(1000) | Remarks to store in the OCC authorisation record |

### Logic Flow
1. **Line Check** – Proceed only if `@Line` equals `'DTL'`.  
2. **Transaction Start** – Begin a transaction to ensure atomicity.  
3. **Variable Declaration** – Declare local variables for endorser IDs, workflow ID, and status ID.  
4. **Level‑Specific Processing** – For each of the levels 2, 3, 8, 14, 16, 19:  
   1. Retrieve the active workflow definition for the line.  
   2. Find the current endorser record for that workflow and level.  
   3. Mark the current workflow record as **Completed**, recording action time and user.  
   4. Identify the next level’s endorser and its status ID.  
   5. Insert a new workflow record for the next level with status **Pending** and default values.  
   6. Update the OCC authorisation record with the new status ID, supplied remarks, and audit timestamps.  
   7. For levels 14, 16, and 19 an additional read of the current level’s status ID is performed before the update.  
5. **Audit Logging** – After the level block:  
   1. Insert an audit row for the updated workflow record (`AuditAction = 'U'`).  
   2. Insert an audit row for the newly inserted pending workflow record (`AuditAction = 'I'`).  
   3. Insert an audit row for the updated OCC authorisation record (`AuditAction = 'U'`).  
6. **Commit** – Commit the transaction if all operations succeed.  
7. **Error Handling** – On any error, roll back the transaction.

### Data Interactions
* **Reads:**  
  - `TAMS_Workflow` – to locate the active workflow definition.  
  - `TAMS_Endorser` – to find current and next endorser records.  
  - `TAMS_OCC_Auth_Workflow` – to fetch the current workflow row for audit.  
  - `TAMS_OCC_Auth` – to fetch the authorisation row for audit.  

* **Writes:**  
  - `TAMS_OCC_Auth_Workflow` – update current row to **Completed** and insert new **Pending** row.  
  - `TAMS_OCC_Auth` – update status ID, remarks, and timestamps.  
  - `TAMS_OCC_Auth_Workflow_Audit` – insert audit rows for update and insert actions.  
  - `TAMS_OCC_Auth_Audit` – insert audit row for the authorisation update.