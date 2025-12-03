# Procedure: sp_TAMS_GetTarWorkingLimitByPossessionId

### Purpose
This stored procedure retrieves the working limit details for a specific possession ID from the TAMS_Possession_WorkingLimit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the working limit. |

### Logic Flow
1. The procedure starts by selecting all columns (id, possessionid, and redflashinglampsloc) from the TAMS_Possession_WorkingLimit table.
2. It filters the results to only include rows where the possessionid matches the provided @PossessionId parameter.
3. The results are ordered in ascending order by the id column.

### Data Interactions
* **Reads:** TAMS_Possession_WorkingLimit