# Procedure: sp_TAMS_GetTarPossessionPlanByTarId

### Purpose
This stored procedure retrieves a possession plan for a specific TarId from the TAMS_Possession and TAMS_Type_Of_Work tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar to retrieve the possession plan for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Possession and TAMS_Type_Of_Work tables.
2. It filters the results to only include rows where the typeofworkid in TAMS_Possession matches the id in TAMS_Type_Of_Work, and the tarid in TAMS_Possession matches the provided @TarId parameter.
3. The procedure then returns a list of columns from the selected data.

### Data Interactions
* **Reads:** TAMS_Possession, TAMS_Type_Of_Work