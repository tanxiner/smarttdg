# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval_20231009

### Purpose
Approve a user registration module by a system administrator, advance the workflow status, log the action, and notify relevant approvers via email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module record to be approved. |
| @UpdatedBy | INT | Identifier of the user performing the approval. |

### Logic Flow
1. Begin a transaction and declare variables for workflow and status handling.  
2. Retrieve the registration module details (RegID, Line, TrackType, Module, IsExternal, RegStatus) by joining the module and registration tables on the supplied @RegModID.  
3. Determine the workflow type:  
   - If the registration is external, use 'ExtUser'.  
   - Otherwise, use 'TARIntUser' for TAR modules or 'OCCIntUser' for other modules.  
4. Find the active workflow definition that matches the line and workflow type, ensuring the current date falls between its effective and expiry dates.  
5. Locate the next endorser record for this workflow and line where the level is one greater than the current status level, and the record is active and within its validity period. Capture the new workflow status ID, role ID, and endorser ID.  
6. Translate the new workflow status ID into a status text from the status table.  
7. Insert a new record into the registration module table with the new status, workflow ID, endorser ID, and status text, marking it as pending.  
8. If the original module record still exists, update its workflow status to 'Approved', set the updated timestamp, and record the updater.  
9. Insert an audit log entry describing the system‑admin approval action.  
10. Build a comma‑separated list of email addresses for users who hold the role identified in step 5.  
11. Compose an email body that invites recipients to approve or reject the registration via the TAMS login page.  
12. Enqueue the email through the alert queue procedure, supplying sender, subject, recipients, and message body.  
13. Commit the transaction.  
14. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role  
* **Writes:** TAMS_Reg_Module, TAMS_Action_Log  

---