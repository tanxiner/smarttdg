# Procedure: sp_TAMS_Get_ChildMenuByUserRole_20231009

### Purpose
This stored procedure retrieves child menus based on a user's role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve child menus for. |
| @MenuID | NVARCHAR(100) | The ID of the parent menu to retrieve child menus from. |

### Logic Flow
1. The procedure first creates a temporary table #RoleTbl to store unique role codes.
2. It then inserts distinct role codes into the #RoleTbl based on the user's ID, their corresponding roles in TAMS_User_Role and TAMS_Role tables, and the user's login ID.
3. If the user has at least one assigned role, it constructs a SQL query to retrieve child menus by concatenating the role code with 'IN(' and ')'.
4. The procedure executes this constructed query using the EXEC function.
5. After executing the query, it drops the temporary table #RoleTbl.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role, Menu tables.
* **Writes:** None