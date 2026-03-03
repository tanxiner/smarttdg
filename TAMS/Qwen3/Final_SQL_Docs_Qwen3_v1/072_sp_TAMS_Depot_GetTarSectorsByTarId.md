# Procedure: sp_TAMS_Depot_GetTarSectorsByTarId

### Purpose
This stored procedure retrieves a list of sectors associated with a specific TAR (TAR stands for Tariff Area Management System Sector) ID, excluding buffer sectors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to retrieve sectors for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Sector table.
2. It then joins this table with the TAMS_TAR_Sector table on the SectorId column, and further joins it with the TAMS_TAR table on the TARId column.
3. The procedure filters out buffer sectors (where IsBuffer = 1) based on the provided TAR ID.
4. Finally, the results are ordered by Order and Sector in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR