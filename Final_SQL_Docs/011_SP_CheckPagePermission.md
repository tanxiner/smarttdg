# Procedure: SP_CheckPagePermission

### Purpose
Determines whether a specified user has permission to access a given menu item.

### Parameters
| Name   | Type          | Purpose |
| :----- | :------------ | :------ |
| @userid | nvarchar(50) | User login identifier to check permissions for. |
| @menuid | nvarchar(50) | Menu identifier whose access is being verified. |
| @res | bit OUTPUT | Returns 1 if the user has access, 0 otherwise. |

### Logic Flow
1. Disable row‑count messages to avoid interfering with the SELECT result.  
2. Execute a single existence check that joins the tables **TAMS_Menu_Role**, **TAMS_Role**, **TAMS_User_Role**, and **TAMS_User** to determine if there is a role‑based link between the supplied user and menu.  
3. If such a link exists, set **@RES** to 1; otherwise set **@RES** to 0.

### Data Interactions
* **Reads:** TAMS_Menu_Role, TAMS_Role, TAMS_User_Role, TAMS_User  
* **Writes:** None