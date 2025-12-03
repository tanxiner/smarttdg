# Procedure: sp_TAMS_Update_UserRegRole_SysOwnerApproval

### Purpose
This stored procedure updates the user registration role system owner approval status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module. |
| @RegRoleID | INT | The ID of the registration role. |
| @IsAssigned | BIT | A flag indicating whether the user is assigned to the role. |
| @RejectRemarks | NVARCHAR(MAX) | Remarks for rejecting the assignment. |
| @UpdatedBy | INT | The ID of the user updating the approval status. |

### Logic Flow
1. The procedure starts by declaring variables and selecting data from various tables based on the input parameters.
2. It then updates the registration role table with the new approval status, updated date, reject remarks, and updated by user ID.
3. If the user is assigned to the role, it checks if the user already has an entry in the TAMS_User_Role table for the same line, role, and track type. If not, it inserts a new record into this table.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_Role, TAMS_User_Role
* **Writes:** TAMS_Reg_Role