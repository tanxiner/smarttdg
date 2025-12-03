# Procedure: sp_TAMS_Get_ChildMenuByUserRole

### Purpose
This stored procedure retrieves child menu items based on a user's role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user for whom to retrieve child menu items. |
| @MenuID | NVARCHAR(100) | The ID of the parent menu item. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether to include internet-based menu items (1) or not (0). |

### Logic Flow
The procedure first checks if a user is logged in and has roles assigned. If so, it creates a temporary table to store the role IDs and then selects the corresponding child menu items from the TAMS_Menu_Role table based on the user's role. If no user is logged in or does not have any roles, it directly retrieves the child menu items for the specified parent menu item.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role