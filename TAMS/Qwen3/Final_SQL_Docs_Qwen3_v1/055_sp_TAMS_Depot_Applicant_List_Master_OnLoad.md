# Procedure: sp_TAMS_Depot_Applicant_List_Master_OnLoad

### Purpose
This stored procedure generates a list of depot applicants based on specific criteria, including line, track type, access date range, and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @ToAccessDate | NVARCHAR(20) | Specifies the end date of the access range. |
| @FromAccessDate | NVARCHAR(20) | Specifies the start date of the access range. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and time.
2. It creates a temporary table, #TmpSector, to store the filtered sector data based on the provided line, track type, and access date range.
3. The procedure then truncates any existing data in #TmpSector.
4. It inserts data into #TmpSector from TAMS_Sector, filtering by the specified line, track type, and active status within the current date range.
5. The procedure groups the data in #TmpSector by sector order and orders the results accordingly.
6. Finally, it drops the temporary table.

### Data Interactions
* **Reads:** TAMS_Sector
* **Writes:** None