# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection

### Purpose
This stored procedure retrieves a list of tar sectors by access date, line, and direction.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results by. |
| @Line | nvarchar(10) = NULL | The line number to filter the results by. If NULL, all lines are included. |
| @TrackType | nvarchar(50) = NULL | The track type to filter the results by. If NULL, all track types are included. |
| @Direction | nvarchar(10) = NULL | The direction to filter the results by. |

### Logic Flow
1. A temporary table #TMP is created with columns for sector ID, line number, same sector flag, direction, sector name, tar number, access date, access type, sector ID, buffer flag, colour code, gap flag, and order.
2. If @Line is 'DTL', the procedure inserts data into #TMP by selecting from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables based on the specified filter criteria (access date, track type, direction). The results are ordered by [Order] ASC.
3. If @Line is 'NEL', a similar insertion process occurs as in step 2, but with different filter criteria for TAMS_TAR_Sector and TAMS_TAR tables.
4. After inserting data into #TMP, the procedure updates the colour code column to the top value from #TMP where same sector, tar number, and colour code are not null.
5. The final result is selected from #TMP and ordered by [Order] ASC.
6. Finally, the temporary table #TMP is dropped.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables