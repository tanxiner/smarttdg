# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_bak20230112

### Purpose
Registers an internal user’s module request, assigns the initial workflow stage, logs the action, and notifies approvers via email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Identifier of the user registration record |
| @Line | NVARCHAR(20) | Business line for which the registration applies |
| @Module | NVARCHAR(20) | Module name being registered |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Retrieve the active workflow ID for the supplied line where `WorkflowType = 'TARIntUser'` and the current date falls between `EffectiveDate` and `ExpiryDate`.  
3. From the endorser table, fetch the first‑level endorser for that workflow: capture `WFStatusId` as the next stage ID, `RoleID` as the new workflow role ID, and the endorser’s ID.  
4. Look up the status description for the obtained stage ID in the workflow status table (`WFType = 'UserRegStatus'`).  
5. Insert a new record into `TAMS_Reg_Module` with the registration ID, line, module, next stage ID, workflow ID, endorser ID, status set to 'Pending', the status description, current timestamp, and audit flags.  
6. Record the action in `TAMS_Action_Log` with details of the module registration event.  
7. Build an email notification:  
   - Query users who hold a role containing 'SysApprover' for the given line and module; concatenate their email addresses into a comma‑separated list.  
   - Set email metadata (sender, system ID, subject, greetings, etc.).  
   - Construct an HTML body comprising three sections: a prompt to approve/reject, a link to the TAMS login page, and a footer disclaimer.  
   - Enqueue the email via `EAlertQ_EnQueue`, passing the assembled parameters.  
8. Commit the transaction.  
9. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_Workflow`, `TAMS_Endorser`, `TAMS_WFStatus`, `TAMS_User`, `TAMS_User_Role`, `TAMS_Role`  
* **Writes:** `TAMS_Reg_Module`, `TAMS_Action_Log` (plus the email queue handled by `EAlertQ_EnQueue`)