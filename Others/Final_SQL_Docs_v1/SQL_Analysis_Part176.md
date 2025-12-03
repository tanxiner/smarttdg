# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20230112
**Type:** Stored Procedure

The procedure updates a user registration module's status to "Approved" and creates or updates a new user account if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who is updating the registration module. |

### Logic Flow
1. Checks if the registration module exists and is external.
2. Determines the workflow type based on the module's ID.
3. Retrieves the current stage, workflow ID, and endorser information for the registration module.
4. If the registration module already exists, updates its status to "Approved" and inserts a new audit log entry.
5. Creates or updates a new user account if necessary, depending on whether the registration module is external.
6. Sends an email notification to the registered user with instructions on how to access TAMS.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_User, TAMS_Action_Log, EAlertQ_EnQueue
* **Writes:** TAMS_Reg_Module (insert/update), TAMS_User (create/update), TAMS_Action_Log