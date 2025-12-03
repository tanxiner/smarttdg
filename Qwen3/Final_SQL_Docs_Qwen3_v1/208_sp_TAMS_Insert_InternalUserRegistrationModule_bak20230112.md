# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_bak20230112

### Purpose
This stored procedure performs the business task of inserting a new internal user registration module into the TAMS system, triggering a workflow and sending an email to approvers for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It retrieves the next stage in the workflow for the given line and module, which determines the status of the registration.
3. Based on the retrieved status, it inserts a new record into the TAMS_Reg_Module table with the provided details.
4. An audit log is inserted to track the action taken.
5. The procedure then sends an email to approvers (sys approvers) for approval, including a link to access the TAMS system and approve/reject the registration.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log
* Writes: TAMS_Reg_Module, TAMS_Action_Log