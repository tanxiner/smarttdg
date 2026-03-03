# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval_20231009
**Type:** Stored Procedure

### Purpose
This stored procedure performs a system admin approval for user registration module updates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module. |

### Logic Flow
1. Checks if a user exists for the given registration module.
2. Retrieves the next stage in the workflow based on the module type and line number.
3. Inserts a new record into the TAMS_Reg_Module table with the updated status.
4. Updates the existing record in the TAMS_Reg_Module table with the approved status.
5. Sends an email to the endorser with a link to access TAMS for approval/rejection.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User_Role.
* **Writes:** TAMS_Reg_Module.