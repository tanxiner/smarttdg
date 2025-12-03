# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_20231009
**Type:** Stored Procedure

### Purpose
This stored procedure retrieves a list of registration inbox items for a specified user ID, including relevant workflow status and details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to retrieve registration inbox items for. |

### Logic Flow
1. Checks if the user exists.
2. Iterates through each role (SysAdmin and SysApprover) associated with the user.
3. For each role, it checks the workflow status and inserts relevant data into a temporary table (#RegistrationTable).
4. The procedure then selects distinct rows from #RegistrationTable and returns them.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role
* **Writes:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus