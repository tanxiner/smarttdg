# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters_bak20230711

### Purpose
Updates the status of an OCC authorisation workflow for the NEL line, advancing it through defined levels and recording audit history.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the update |
| @OCCAuthID | int | Primary key of the OCC authorisation record |
| @OCCLevel | int | Current workflow level (1‑15) |
| @Line | nvarchar(10) | Workflow line identifier, must be 'NEL' to execute |
| @Remarks | nvarchar(100) | Comment to attach to the authorisation record |
| @SelectionValue | nvarchar(50) | Status value used for specific levels (5, 12, 15) |

### Logic Flow
1. Verify that `@Line` equals 'NEL'; otherwise exit.  
2. Begin a transaction.  
3. For the current `@OCCLevel` (1‑15) perform the following pattern:  
   a. Retrieve the active workflow definition for line 'NEL' and type 'OCCAuth'.  
   b. Identify the endorser record matching that workflow, line, and level.  
   c. Mark the current workflow step as 'Completed' (or set to `@SelectionValue` for levels 5, 12, 15).  
   d. Record the action date and user.  
   e. Determine the next endorser (level + 1) and its status ID.  
   f. Insert a new workflow record for the next endorser with status 'Pending' and placeholder dates.  
   g. Update the OCC authorisation record with the new status ID, remarks, and, where applicable, timestamps for power off or racked‑out events (levels 4, 6, 10, 11, 13, 14).  
4. After the level‑specific updates, insert audit entries:  
   - Log the update and insert actions on the workflow table into `TAMS_OCC_Auth_Workflow_Audit`.  
   - Log the update of the authorisation record into `TAMS_OCC_Auth_Audit`.  
5. Commit the transaction.  
6. If any error occurs, roll back the transaction.

### Data interactions
**Reads from**  
- `TAMS_Workflow` (active workflow lookup)  
- `TAMS_Endorser` (current and next endorser lookup)  
- `TAMS_OCC_Auth_Workflow` (current step details)  
- `TAMS_OCC_Auth` (authorisation record for audit)

**Writes to**  
- `TAMS_OCC_Auth_Workflow` (update current step, insert next step)  
- `TAMS_OCC_Auth` (status and remarks update, level‑specific timestamp updates)  
- `TAMS_OCC_Auth_Workflow_Audit` (audit record for update and insert actions)  
- `TAMS_OCC_Auth_Audit` (audit record for the authorisation record)