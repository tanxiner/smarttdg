# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval

### Purpose
Approve a user registration module record, advance its workflow status, log the action, and notify the next approver.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module record to be approved. |
| @UpdatedBy | INT | User ID of the system administrator performing the approval. |

### Logic Flow
1. **Transaction start** – all operations are wrapped in a single transaction with error handling.  
2. **Variable initialization** – declare variables for workflow, status, and email details.  
3. **Retrieve current registration data** – join `TAMS_Reg_Module` and `TAMS_Registration` to obtain the registration ID, line, track type, module, external flag, and current status.  
4. **Determine workflow type** –  
   * If the registration is external, set workflow type to `ExtUser`.  
   * Otherwise, set it based on the module: `TARIntUser`, `DCCIntUser`, or `OCCIntUser`.  
5. **Find active workflow** – select the workflow that matches the line, track type, workflow type, and is currently effective.  
6. **Select next endorser** – locate the endorser record that is one level above the current status, within the same workflow and line, and currently effective.  
7. **Get new workflow status** – fetch the status description for the new status ID.  
8. **Insert a new module record** – create a new `TAMS_Reg_Module` entry with the new status, workflow, endorser, and a `Pending` flag.  
9. **Approve the original record** – if the original record still exists, update its status to `Approved` and record the update timestamp and user.  
10. **Log the action** – insert a row into `TAMS_Action_Log` describing the system‑admin approval.  
11. **Prepare email recipients** – build a comma‑separated list of email addresses for users who hold the role identified by the new endorser.  
12. **Compose email content** – assemble HTML body with a link to the login page and standard footer.  
13. **Queue the email** – call `EAlertQ_EnQueue` to send the notification to the recipients.  
14. **Commit transaction** – finalize all changes.  
15. **Error handling** – on any exception, roll back the transaction.

### Data Interactions
* **Reads:**  
  - `TAMS_Reg_Module`  
  - `TAMS_Registration`  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_WFStatus`  
  - `TAMS_User`  
  - `TAMS_User_Role`  

* **Writes:**  
  - `TAMS_Reg_Module` (insert new record, update existing record)  
  - `TAMS_Action_Log` (insert audit entry)  
  - `EAlertQ_EnQueue` (procedure call to enqueue email)