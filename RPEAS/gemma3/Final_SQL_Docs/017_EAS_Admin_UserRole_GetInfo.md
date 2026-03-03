# Procedure: EAS_Admin_User_GetInfo

### Purpose
This procedure retrieves information about staff roles, including user identifiers, role names, and active status, based on a specified role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The specific role to filter for. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_User` table and the `EAS_User_Role` table.
2.  It first selects user identifiers (`UserID`), role names (`Name`), and the active status (`_Active`) from `EAS_User` where the `UserID` exists in `EAS_User_Role` and the `Role` matches the input `@Role`. The active status is determined by checking the `Active` column in `EAS_User`.
3.  It then performs a `UNION ALL` operation to combine the results with a second set of data.
4.  The second set of data selects `UserID` and `Name` from `EAS_User` where the `UserID` is *not* present in the `EAS_User_Role` table. This identifies users who do not have an assigned role.
5.  The final result set is ordered by the `UserID` column.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`
* **Writes:** None