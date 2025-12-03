# Procedure: sp_TAMS_Depot_GetPossessionDepotSectorByPossessionId

This procedure retrieves data from the TAMS_Possession_DepotSector table based on a specified PossessionId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The ID of the possession for which to retrieve depot sector information |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_DepotSector table.
2. It filters the results to only include rows where the PossessionId matches the input parameter.
3. The results are ordered in ascending order by the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_DepotSector