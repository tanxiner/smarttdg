# Procedure: sp_TAMS_GetTarPossessionLimitByPossessionId

### Purpose
This stored procedure retrieves and returns the possession limit details for a specified possession ID from the TAMS_Possession_Limit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the limit details. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_Limit table.
2. It filters the results to only include rows where the possession ID matches the input parameter @PossessionId.
3. The retrieved data is ordered in ascending order based on the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_Limit