# Procedure: EAS_Admin_MenuRoles_GetInfo

### Purpose
This procedure retrieves information about menu roles associated with a specified role, filtering for active menu items.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The role to filter menu roles by. |

### Logic Flow
The procedure begins by selecting data from the `EAS_Menu` table, filtering for rows where the `Active` column is equal to 1.  It then joins this data with the `EAS_Menu_Role` table based on matching `MenuID` and the provided `@Role` parameter. The selection includes the `MenuID`, `DispText` from the `EAS_Menu` table, an indicator of the role's active status (`_Active`), and an indicator of whether the menu role has a defined `MenuID` (`IsSelected`). Finally, the results are ordered by `MenuID`.

### Data Interactions
* **Reads:** `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None