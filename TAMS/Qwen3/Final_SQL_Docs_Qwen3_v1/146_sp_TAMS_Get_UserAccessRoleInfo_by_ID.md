# Procedure: sp_TAMS_Get_UserAccessRoleInfo_by_ID

This procedure retrieves user access role information for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve access role information for. |

### Logic Flow
1. Check if a user with the provided UserID exists in the TAMS_User table.
2. If the user exists, retrieve all rows from the TAMS_User_Role and TAMS_Role tables where the roleID matches the ID of the specified role in the TAMS_Role table, and the UserID in the TAMS_User_Role table matches the provided UserID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role