# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters_bak20230711

### Purpose
Updates the OCC authorisation workflow for a DTL line, advancing the workflow level, recording actions, and logging audit entries.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the action |
| @OCCAuthID | int | Primary key of the OCC authorisation record |
| @OCCLevel | int | Current workflow level to process |
| @Line | nvarchar(10) | Line identifier (must be 'DTL' for processing) |
| @RemarksPFR | nvarchar(100) | Remark to store in the OCC authorisation record |
| @SelectionValue | nvarchar(50) | Status value supplied by the user (e.g., 'Select', 'Completed') |
| @StationName | nvarchar(50) | Name of the station for level 7 processing |

### Logic Flow
1. **Line Check** – Only proceed if `@Line` equals `'DTL'`.  
2. **Transaction Start** – Begin a transaction to ensure atomicity.  
3. **Variable Declaration** – Prepare local variables for workflow, endorser, station, buffer flag, and test result.  
4. **Level‑Specific Processing** – For each supported `@OCCLevel` (4, 5, 6, 7, 12, 13, 15, 17, 18) the procedure:  
   - Retrieves the active workflow definition for the DTL line.  
   - Finds the current endorser record for the level.  
   - Updates the existing workflow row to mark it as completed or set the supplied status.  
   - Determines the next endorser and its status ID.  
   - Inserts a new workflow row for the next level with status `'Pending'`.  
   - Updates the OCC authorisation record: sets the new status ID, stores `@RemarksPFR`, and records timestamps (`PowerOffTime`, `RackedOutTime`, `UpdatedOn`) as appropriate for the level.  
   - **Level 7** additionally resolves the station ID from `@StationName` (or defaults to 0), updates the current workflow row with the station, and only inserts the next pending row if the record is not a buffer.  
   - **Level 18** interprets `@SelectionValue`: if it is `'Select'` it becomes `'Pending'`; otherwise it is treated as a test result and the status becomes `'Completed'`. The test result is stored in the workflow row.  
5. **Audit Logging** – After the level logic, the procedure inserts audit records:  
   - Two entries into `TAMS_OCC_Auth_Workflow_Audit` for the updated and newly inserted workflow rows.  
   - One entry into `TAMS_OCC_Auth_Audit` capturing the updated OCC authorisation record.  
6. **Transaction Commit** – Commit the transaction if all operations succeed.  
7. **Error Handling** – On any error, roll back the transaction.

### Data Interactions
* **Reads**  
  - `TAMS_Workflow` – to locate the active workflow definition.  
  - `TAMS_Endorser` – to find current and next endorser records and status IDs.  
  - `TAMS_Station` – to resolve station ID for level 7.  
  - `TAMS_OCC_Auth_Workflow` – to capture existing workflow rows for audit.  
  - `TAMS_OCC_Auth` – to read buffer flag and to audit the updated record.

* **Writes**  
  - `TAMS_OCC_Auth_Workflow` – updates current row, inserts next pending row.  
  - `TAMS_OCC_Auth` – updates status, remarks, timestamps, and station‑related fields.  
  - `TAMS_OCC_Auth_Workflow_Audit` – inserts audit rows for updated and inserted workflow entries.  
  - `TAMS_OCC_Auth_Audit` – inserts audit row for the updated OCC authorisation record.