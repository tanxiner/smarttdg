# Procedure: sp_TAMS_Approval_Reject

### Purpose
Rejects a TAR request, updates workflow status, logs the action, and sends notification emails.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR to reject |
| @TARWFID | INTEGER | Current workflow record ID |
| @EID | INTEGER | Current endorser ID |
| @ELevel | INTEGER | Current endorser level |
| @Remarks | NVARCHAR(1000) | Comment for the rejection (mandatory) |
| @UserLI | NVARCHAR(100) | Login ID of the user performing the action |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to caller |

### Logic Flow
1. Initialise a transaction flag and start a transaction if none is active.  
2. Clear the output message.  
3. Retrieve the user’s internal ID and name from **TAMS_User** using the supplied login ID.  
4. Mark the current workflow record (**TAMS_TAR_Workflow**) as *Rejected*, store the remark, and record the acting user and timestamp.  
5. Load endorser title, TAR type, line, email addresses, TAR number, remarks, company, and access date from **TAMS_TAR**.  
6. Get the workflow ID from the current workflow record.  
7. Determine the title of the endorser at the current level within the workflow.  
8. Update the TAR status: set *TARStatusId* to 8 if the line is *NEL*, otherwise to 7; record update time and user.  
9. If the TAR is of type *Urgent*, compose a rejection email by calling **sp_TAMS_Email_Urgent_TAR** with the TAR details.  
10. Insert an action log entry into **TAMS_Action_Log** noting the rejection, user, and timestamp.  
11. Retrieve the workflow type and whether power is involved from **TAMS_Workflow**.  
12. If the workflow is *UrgentAfter*, power is involved, and the endorser level is 2, prepare an additional email to the OCC role:
    - Build a comma‑separated list of active users with the role matching the line plus “_PFR”.
    - Append any additional OCC contact email from **TAMS_Parameters**.
    - Call **sp_TAMS_Email_Urgent_TAR_OCC** to send the notification.  
13. If any error occurs during the updates, set an error message and jump to the error handler.  
14. Commit the transaction if it was started internally and return the message.  
15. On error, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR  
  - TAMS_Workflow  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Parameters  

* **Writes:**  
  - TAMS_TAR_Workflow (UPDATE)  
  - TAMS_TAR (UPDATE)  
  - TAMS_Action_Log (INSERT)