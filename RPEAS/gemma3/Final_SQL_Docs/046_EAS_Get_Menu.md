# Procedure: EAS_Get_Menu

### Purpose
This procedure retrieves a hierarchical menu structure for a specified user and system, displaying the menu items and their associated details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_UserID | nvarchar(100) | The identifier for the user. |
| @p_sysid | nvarchar(30) | The identifier for the system. |

### Logic Flow
1.  The procedure initializes a variable, @urole, to an empty string.
2.  It selects the roles associated with the specified user and system from the `EAS_User_Role` and `EAS_User` tables. The selection is based on matching UserID and Sysid, and the active status of both tables. The selected roles are concatenated into the @urole variable, separated by commas.
3.  The `LEFT` function is used to remove the trailing comma from the @urole variable.
4.  If @urole is not null and not empty, the procedure constructs a dynamic SQL string, @rsql.
5.  The dynamic SQL string selects menu items from the `EAS_Menu` table where the Active status is 1 and the ParentMenuID is null.
6.  The dynamic SQL string further filters the menu items to include only those whose Role is present in the @urole variable. The results are ordered by MenuLevel.
7.  The dynamic SQL string is executed, retrieving the specified menu details.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`, `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None