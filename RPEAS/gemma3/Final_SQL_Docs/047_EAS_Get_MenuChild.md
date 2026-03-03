# Procedure: EAS_Get_MenuChild

### Purpose
This procedure retrieves child menu items from a specified parent menu, considering user roles and a system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_UserID | nvarchar(100) | The ID of the user making the request. |
| @p_MenuID | nvarchar(100) | The ID of the parent menu. |
| @p_Sysid | nvarchar(30) | A system identifier. |

### Logic Flow
1.  The procedure initializes a variable, @urole, to store the user's roles.
2.  It retrieves the user's roles from the `EAS_User_Role` and `EAS_User` tables, filtering by the provided `@p_UserID` and `@p_Sysid`. The retrieved roles are concatenated into the `@urole` variable, separated by commas. The `LEFT` function is used to remove the trailing comma from the `@urole` variable.
3.  If a user role is found and not empty, the procedure constructs a dynamic SQL string, `@rsql`, to execute a `SELECT` statement.
4.  The `SELECT` statement retrieves menu details from the `EAS_Menu` table, filtering by the provided `@p_MenuID` and `@p_Sysid`, and also by the roles stored in the `@urole` variable. The `MenuID` is filtered using a subquery that selects distinct `MenuID` values from the `EAS_Menu_Role` table, ensuring that only menu items accessible to the user are returned. The results are ordered by `MenuLevel`.
5.  The dynamic SQL string, `@rsql`, is executed, which retrieves the menu details and returns them as a result set.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`, `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None