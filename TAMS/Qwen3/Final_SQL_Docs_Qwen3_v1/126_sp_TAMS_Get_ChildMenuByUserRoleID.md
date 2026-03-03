# Procedure: sp_TAMS_Get_ChildMenuByUserRoleID

### Purpose
This stored procedure retrieves child menu items based on a user's role ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The user ID to retrieve roles for. |
| @MenuID | NVARCHAR(100) | The parent menu ID to retrieve child menu items for. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether to include internet menus or not. |

### Logic Flow
The procedure first creates a temporary table to store the user's role IDs. It then inserts these roles into the table and selects the corresponding role codes. The procedure concatenates these role codes into a single string, which is used to filter menu items.

If the concatenated role code is not empty, the procedure generates a SQL query to retrieve child menu items based on the role ID. This query includes filters for the parent menu ID, menu level, and module ID. If the @IsInternet parameter is 1, the query includes internet menus; otherwise, it excludes them.

The procedure prints the generated SQL query and executes it using the EXECUTE statement. Finally, it drops the temporary table used to store role IDs.

### Data Interactions
* Reads: TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role, Menu
* Writes: None