# Procedure: sp_TAMS_GetTarSectorsByTarId

### Purpose
This stored procedure retrieves a list of sectors associated with a specific TAR (TAR stands for Tariff Area Management System Sector) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to retrieve sectors for. |

### Logic Flow
The procedure starts by joining three tables: TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR. It filters the results to only include sectors where the TAR ID matches the input parameter (@TarId) and the sector is not a buffer (IsBuffer = 0). The results are then ordered by Order and Sector in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables.