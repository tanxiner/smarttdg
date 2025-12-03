# Procedure: sp_TAMS_Insert_UserRegRole_SysAdminApproval

### Purpose
This stored procedure performs the business task of inserting a new user registration role with sysadmin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registered module. |
| @RegRoleID | INT | The ID of the role to be assigned. |
| @IsAssigned | BIT | A flag indicating whether the role is assigned or not. |
| @UpdatedBy | INT | The ID of the user who updated the registration. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then retrieves the next stage ID for the specified registered module and workflow type, as well as the new workflow status ID and endorser ID.
3. If these values are found, it inserts a new record into the TAMS_Reg_Role table with the provided parameters.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_Reg_Module, TAMS_Reg_Role
* **Writes:** TAMS_Reg_Role