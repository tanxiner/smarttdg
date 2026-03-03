# Procedure: sp_TAMS_Get_RegistrationInboxByUserID
**Type:** Stored Procedure

Purpose: Retrieves a list of registration inbox items for a specified user ID, including relevant details and workflow status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to retrieve registration inbox items for. |

### Logic Flow
1. Checks if the user exists.
2. Iterates through each role (SysAdmin and SysApprover) associated with the user.
3. For each role, it checks the workflow status and inserts relevant details into a temporary table (#RegistrationTable).
4. The procedure then selects distinct rows from #RegistrationTable and returns them.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role
* **Writes:** #RegistrationTable