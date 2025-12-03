# Procedure: sp_TAMS_Approval_Reject_20220930

### Purpose
Rejects a TAR, updates its workflow status, logs the action, and sends notification emails based on TAR type and workflow conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR to be rejected |
| @TARWFID | INTEGER | Current workflow record ID for the TAR |
| @EID | INTEGER | Current endorser ID initiating the rejection |
| @ELevel | INTEGER | Current endorser level in the workflow |
| @Remarks | NVARCHAR(1000) | Remarks supplied for the rejection |
| @UserLI | NVARCHAR(50) | Login ID of the user performing the action |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. Begin a transaction if none is active.  
2. Clear the output message.  
3. Retrieve the user’s internal ID and name from TAMS_User using @UserLI.  
4. Update the TAMS_TAR_Workflow record identified by @TARWFID: set status to 'Rejected', store @Remarks, record the acting user and timestamp.  
5. Load the endorser title for @EID, and load TAR details (type, line, email, company, access date, etc.) for @TARID.  
6. Determine the current workflow ID from the workflow record.  
7. Identify the actor title for the current level within the workflow.  
8. Update the TAR status: if the line is 'NEL' set status ID to 8, otherwise set to 7; record update timestamp and user.  
9. If the TAR type is 'Late', invoke sp_TAMS_Email_Late_TAR to send a rejection email to the TAR owner.  
10. Insert an action log entry into TAMS_Action_Log recording the rejection event, including line, module, function, transaction ID, message, timestamp, and user.  
11. Retrieve the workflow type and whether power is involved from TAMS_Workflow.  
12. If the workflow is 'LateAfter', power is involved, and the endorser level is 2, gather all active users whose role matches the line plus '_PFR' and whose validity period covers the TAR access date.  
13. Send a rejection email to those OCC users via sp_TAMS_Email_Late_TAR_OCC.  
14. If any error occurs during the process, set an error message and roll back the transaction.  
15. Commit the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_TAR, TAMS_Workflow, TAMS_User_Role, TAMS_Role  
* **Writes:** TAMS_TAR_Workflow, TAMS_TAR, TAMS_Action_Log