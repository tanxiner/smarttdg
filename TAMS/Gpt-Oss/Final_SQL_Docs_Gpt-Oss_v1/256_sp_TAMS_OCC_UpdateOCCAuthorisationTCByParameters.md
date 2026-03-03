# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationTCByParameters

### Purpose
Updates the status of an OCC authorisation workflow for a detail line, progressing it through predefined levels, and records the changes in audit tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the action |
| @OCCAuthID | int | Primary key of the OCC authorisation record |
| @OCCLevel | int | Current workflow level of the authorisation |
| @Line | nvarchar(10) | Line type; only 'DTL' triggers processing |
| @TrackType | nvarchar(50) | Type of track associated with the workflow |
| @SelectionValue | nvarchar(50) | New status value used when @OCCLevel = 11 |

### Logic Flow
1. **Line Check** – If @Line is not 'DTL', the procedure exits without action.  
2. **Transaction Start** – All subsequent operations run inside a TRY…CATCH transaction.  
3. **Variable Declaration** – Local variables for workflow ID, endorser IDs, and status IDs are declared.  
4. **Level‑Specific Processing** – For each supported @OCCLevel (1, 9, 10, 11, 20) the procedure:  
   * Retrieves the active workflow ID matching @Line, @TrackType, and workflow type 'OCCAuth'.  
   * Finds the current endorser record for that workflow and level.  
   * Marks the current workflow record as 'Completed', recording the action date and user.  
   * For levels 1, 10, 11:  
     * Determines the next level’s endorser and status ID.  
     * Inserts a new workflow record for the next level with status 'Pending' (or the supplied @SelectionValue for level 11).  
     * Updates the OCC authorisation record’s status ID to the next level’s status.  
   * For level 9:  
     * Skips inserting a next‑level record and directly sets the authorisation status to 10.  
   * For level 20:  
     * Marks the current record as 'Completed' but does not create a next‑level record or change the authorisation status.  
5. **Reset Level** – @OCCLevel is set to 0 (unused thereafter).  
6. **Audit Logging** – Three audit inserts record:  
   * The update of the current workflow record.  
   * The insertion of the new pending workflow record (if created).  
   * The update of the OCC authorisation record.  
7. **Commit** – Transaction is committed if all operations succeed; otherwise it is rolled back in the CATCH block.

### Data Interactions
* **Reads:**  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_OCC_Auth_Workflow  
  - TAMS_OCC_Auth  

* **Writes:**  
  - TAMS_OCC_Auth_Workflow (UPDATE, INSERT)  
  - TAMS_OCC_Auth (UPDATE)  
  - TAMS_OCC_Auth_Workflow_Audit (INSERT)  
  - TAMS_OCC_Auth_Audit (INSERT)