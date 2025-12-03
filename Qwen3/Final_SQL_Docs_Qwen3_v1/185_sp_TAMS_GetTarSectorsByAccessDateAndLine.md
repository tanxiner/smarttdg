# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLine

### Purpose
This stored procedure retrieves tar sectors by access date and line, filtering based on specific conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter by. |
| @Line | nvarchar(10) | The line to filter by (DTLD or NELD). |

### Logic Flow
1. A temporary table #TMP is created with various columns.
2. If the specified line (@Line) is 'DTLD', the procedure inserts data from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables into #TMP based on the access date (@AccessDate), TARStatusId, and other conditions.
3. If the specified line (@Line) is 'NELD', a similar insertion process occurs for NELD lines.
4. After inserting data, the procedure updates the ColourCode column in #TMP by selecting from itself where SameSector, TarNo, and ColourCode are not null.
5. Finally, the procedure selects all columns from #TMP ordered by [Order] ASC.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables
* **Writes:** #TMP table