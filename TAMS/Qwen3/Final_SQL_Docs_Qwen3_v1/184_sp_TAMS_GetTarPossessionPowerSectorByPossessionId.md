# Procedure: sp_TAMS_GetTarPossessionPowerSectorByPossessionId

### Purpose
This stored procedure retrieves and displays information about a specific power sector associated with a possession ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the corresponding power sector details. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_PowerSector table based on the provided PossessionId.
2. It filters the results to only include rows where the PossessionId matches the input parameter.
3. The selected data is then ordered in ascending order by the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_PowerSector