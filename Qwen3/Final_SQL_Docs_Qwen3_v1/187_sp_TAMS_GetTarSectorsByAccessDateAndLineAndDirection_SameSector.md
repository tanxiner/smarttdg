# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection_SameSector

### Purpose
This stored procedure retrieves tar sectors by access date, line, and direction for a specific sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results by. |
| @Line | nvarchar(10) | The line number to filter the results by. (Default: NULL). |
| @Direction | nvarchar(10) | The direction to filter the results by. (Default: NULL). |

### Logic Flow
1. A temporary table #TMP is created with columns for sector ID, line, same sector, and other relevant information.
2. If the specified line (@Line) is 'DTL', the procedure inserts data from TAMS_Sector and TAMS_TAR tables into #TMP based on the access date (@AccessDate), TARStatusId, and direction (@Direction).
3. If the specified line (@Line) is 'NEL', a similar insertion process occurs for TAMS_Sector and TAMS_TAR_Test tables.
4. The procedure updates the ColourCode column in #TMP by selecting the ColourCode from the same row where SameSector is not null and TarNo is not null and ColourCode is not null.
5. Finally, the procedure selects all columns from #TMP.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Test