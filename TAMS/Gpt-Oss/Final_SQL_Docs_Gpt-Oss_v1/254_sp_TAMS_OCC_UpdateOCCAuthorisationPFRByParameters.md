# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters

### Purpose
Updates the status and audit trail of an OCC authorisation record based on the current workflow level and supplied parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the update |
| @OCCAuthID | int | Primary key of the OCC authorisation to modify |
| @OCCLevel | int | Current workflow level of the authorisation |
| @Line | nvarchar(10) | Line identifier; only 'DTL' triggers processing |
| @TrackType | nvarchar(50) | Optional track type (unused in logic) |
| @RemarksPFR | nvarchar(1000) | Remark to store in the authorisation record |
| @SelectionValue | nvarchar(50) | Status value to apply at the current level |
| @StationName | nvarchar(50) | Station name for level 7 processing |

### Logic Flow
1. **Line Check** – If `@Line` is not `'DTL'`, the procedure exits without action.  
2. **Transaction Start** – A transaction is begun to ensure atomicity.  
3. **Variable Declaration** – Local variables for workflow, endorser, station, buffer flag, and test result are declared.  
4. **Level‑Specific Processing** – For each supported `@OCCLevel` (4, 5, 6, 7, 12, 13, 15, 17, 18) the following pattern is executed:  
   - Retrieve the active workflow record for the line.  
   - Retrieve the endorser record for the current level.  
   - Update the existing workflow entry for this authorisation and endorser, setting status, action timestamp, and acting user.  
   - Determine the next level’s endorser and its workflow status ID.  
   - Insert a new workflow record for the next level with status `'Pending'` (or `'Completed'` for level 18 when a test result is supplied).  
   - Update the main authorisation record: set status ID, remarks, and, where applicable, timestamps for power off, racked‑out, or buffer flags.  
   - For level 7, resolve the station ID from `@StationName` (or `0` if `'N.A.'`) and set it in the workflow update.  
   - For level 18, translate a `'Select'` selection into `'Pending'`; otherwise store the supplied test result and mark the status `'Completed'`.  
5. **Audit Insertion** – After the level‑specific updates:  
   - Insert a record into `TAMS_OCC_Auth_Workflow_Audit` for the updated workflow entry (`'U'`).  
   - Insert a record for the newly inserted workflow entry (`'I'`).  
   - Insert a record into `TAMS_OCC_Auth_Audit` capturing the current state of the authorisation record (`'U'`).  
6. **Commit / Rollback** – If all operations succeed, the transaction is committed; otherwise it is rolled back in the catch block.

### Data Interactions
* **Reads**  
  - `TAMS_Workflow` – to locate the active workflow for the line.  
  - `TAMS_Endorser` – to find endorser IDs for current and next levels.  
  - `TAMS_Station` – to resolve station ID for level 7.  
  - `TAMS_OCC_Auth_Workflow` – to capture existing workflow entries for audit.  
  - `TAMS_OCC_Auth` – to read buffer flag and current status before updates.  

* **Writes**  
  - `TAMS_OCC_Auth_Workflow` – updates existing entries and inserts new pending entries.  
  - `TAMS_OCC_Auth` – updates status, remarks, timestamps, and buffer flag.  
  - `TAMS_OCC_Auth_Workflow_Audit` – inserts audit records for updates and inserts.  
  - `TAMS_OCC_Auth_Audit` – inserts audit record of the authorisation after changes.