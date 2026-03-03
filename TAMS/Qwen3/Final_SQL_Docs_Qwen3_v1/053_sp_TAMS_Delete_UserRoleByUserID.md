# Procedure: sp_TAMS_Delete_UserRoleByUserID

### Purpose
This stored procedure deletes a user role from the TAMS_User_Role table for a specified user ID, ensuring that only roles with an ID of 1 are deleted.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user whose role is to be deleted. |

### Logic Flow
The procedure starts by attempting to begin a transaction. If successful, it checks if a row exists in the TAMS_User_Role table for the specified user ID and RoleID not equal to 1. If such a row exists, it deletes this row from the table.

### Data Interactions
* **Reads:** TAMS_User_Role
* **Writes:** TAMS_User_Role