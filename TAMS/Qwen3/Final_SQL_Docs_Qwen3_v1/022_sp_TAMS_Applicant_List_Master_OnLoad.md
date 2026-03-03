# Procedure: sp_TAMS_Applicant_List_Master_OnLoad

### Purpose
This stored procedure generates a list of applicants for a specific sector, filtered by track type, access dates, and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector by. |
| @TrackType | NVARCHAR(50) | The track type to filter the sector by. |
| @ToAccessDate | NVARCHAR(20) | The start date of access for filtering applicants. |
| @FromAccessDate | NVARCHAR(20) | The end date of access for filtering applicants. |
| @TARType | NVARCHAR(20) | The TAR type to filter the sector by. |

### Logic Flow
1. The procedure starts by setting the current date and truncating any temporary tables.
2. It then inserts data into a temporary table (#TmpSector) from TAMS_Sector, filtering by the specified line number, track type, and access dates.
3. The procedure then selects data from #TmpSector, grouping by sector order and direction (BB or NB), and ordering by sector order.
4. Finally, it drops the temporary tables.

### Data Interactions
* Reads: TAMS_Sector table
* Writes: #TmpSector table