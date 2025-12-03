# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval
**Type:** Stored Procedure

### Purpose
This stored procedure performs a system admin approval for user registration module updates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module. |

### Logic Flow
1. Checks if a user exists for the given registration module ID.
2. Inserts into the Audit table with details of the system admin approval.
3. Retrieves the next stage in the workflow based on the current status and module type.
4. Updates the registration module with the new workflow status and assigns it to the sysadmin.
5. Sends an email notification to the endorser and other relevant users.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User_Role, TAMS_Action_Log
* **Writes:** TAMS_Reg_Module