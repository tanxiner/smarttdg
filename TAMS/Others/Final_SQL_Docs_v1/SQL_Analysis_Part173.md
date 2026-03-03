# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany
**Type:** Stored Procedure

The procedure updates a user registration module by obtaining approval from a system administrator.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UserID | NVARCHAR(200) | The ID of the user associated with the registration module. |

### Logic Flow
1. Checks if a user exists for the given registration module.
2. Inserts into an audit table to record the system administrator's approval.
3. Updates the company information in TAMS_Company and TAMS_Registration tables.
4. Sends an email notification to the user with instructions on how to access TAMS.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_User, TAMS_Role, TAMS_Company, TAMS_Registration, TAMS_Action_Log, TAMS_Endorser, TAMS_Workflow, TAMS_EAlertQ_EnQueue
* **Writes:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Company, TAMS_Registration, TAMS_Action_Log