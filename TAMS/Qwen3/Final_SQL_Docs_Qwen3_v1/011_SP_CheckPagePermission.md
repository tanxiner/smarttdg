# Procedure: SP_CheckPagePermission

### Purpose
This stored procedure checks if a user has permission to access a specific menu.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @userid | nvarchar(50) | The ID of the user to check permissions for. |
| @menuid | nvarchar(50) | The ID of the menu to check permissions against. |
| @res | bit OUTPUT | A flag indicating whether the user has permission (1) or not (0). |

### Logic Flow
The procedure first checks if a user exists in the system and if they have been assigned a role that includes access to the specified menu. It does this by joining multiple tables: TAMS_Menu_Role, TAMS_Role, TAMS_User_Role, and TAMS_User. If a match is found, it sets @res to 1; otherwise, it sets @res to 0.

### Data Interactions
* **Reads:** TAMS_Menu_Role, TAMS_Role, TAMS_User_Role, and TAMS_User