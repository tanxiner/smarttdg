# Procedure: sp_TAMS_Depot_GetTarSectorsByAccessDateAndLine

### Purpose
This stored procedure retrieves Tar Sectors from TAMS Depot by Access Date and Line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results. |
| @Line | nvarchar(10) = NULL | The line to filter the results (optional). |

### Logic Flow
1. A temporary table #TMP is created with various columns.
2. If the @Line parameter is 'NEL', the procedure inserts data into #TMP from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables based on the specified Access Date and conditions.
3. The procedure updates the ColourCode column in #TMP by selecting a value from another row with matching SameSector, TarNo, and ColourCode.
4. Finally, the procedure selects all data from #TMP ordered by [Order] ASC.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables.
* **Writes:** #TMP table.