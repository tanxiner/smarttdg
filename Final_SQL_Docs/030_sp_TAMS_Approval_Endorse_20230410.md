# Procedure: sp_TAMS_Approval_Endorse_20230410

### Purpose
Finalises a TAR approval or endorsement, updates workflow status, records the action, and triggers any required email notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Identifier of the current workflow record |
| @EID | INTEGER | Identifier of the current endorser (unused in logic) |
| @ELevel | INTEGER | Current endorser level in the workflow |
| @Remarks | NVARCHAR(1000) | Comment supplied by the user (mandatory for reject, optional otherwise) |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVFMode (1 = update) |
| @UserLI | NVARCHAR(100) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns it.
2. **User Identification** – Look up the user’s internal ID and name from TAMS_User using the supplied login ID.
3. **Mark Current Workflow Approved** – Update the TAMS_TAR_Workflow record identified by @TARWFID to status ‘Approved’, recording the acting user, timestamp, and remarks.
4. **Optional TVF Mode Update** – If @TVFRunModeUpdInd equals 1, set the TVFMode column of the TAR record to @TVFRunMode.
5. **Retrieve TAR Context** – Pull the TAR’s type, line, email, number, remarks, company, and access date from TAMS_TAR.
6. **Determine Current Workflow ID** – Get the workflow ID associated with the current workflow record.
7. **Current Endorser Title** – From TAMS_Endorser, fetch the title of the endorser at the current level.
8. **Next Level Endorser Details** – From TAMS_Endorser, fetch the ID, title, workflow ID, status ID, and role ID for the next level (current level + 1).
9. **Last Level Handling** –  
   a. If no next endorser exists, the TAR is at its final approval stage.  
   b. Update the TAR status to 9 if the line is ‘NEL’, otherwise to 8.  
   c. If the TAR type is ‘Urgent’, invoke the urgent approval email routine.