# Procedure: sp_TAMS_GetTarOtherProtectionByPossessionId

### Purpose
This stored procedure retrieves a list of other protection details for a specified possession ID from the TAMS_Possession_OtherProtection table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The ID of the possession for which to retrieve other protection details. |

### Logic Flow
1. The procedure starts by selecting all columns (id, possessionid, and otherprotection) from the TAMS_Possession_OtherProtection table.
2. It filters the results to only include rows where the possessionid matches the provided @PossessionId parameter.
3. The resulting data is ordered in ascending order by the id column.

### Data Interactions
* **Reads:** TAMS_Possession_OtherProtection