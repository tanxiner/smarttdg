# Procedure: sp_TAMS_Get_UserInfo

### Purpose
This stored procedure retrieves user information from the TAMS database, including account status and role assignments.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | NVARCHAR(100) | The login ID of the user to retrieve information for. |

### Logic Flow
The stored procedure checks the existence of a valid user account based on the provided login ID and current date. It then updates the last login timestamp if the account is active. If the account has expired or been deactivated, it sets specific status messages. Finally, it retrieves the user's role assignments.

### Data Interactions
* **Reads:** [TAMS_User], [TAMS_User_Role], [TAMS_Role]
* **Writes:** [TAMS_User] (lastlogin timestamp)