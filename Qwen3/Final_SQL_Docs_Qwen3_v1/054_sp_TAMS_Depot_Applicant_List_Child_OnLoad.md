# Procedure: sp_TAMS_Depot_Applicant_List_Child_OnLoad

### Purpose
This stored procedure retrieves a list of applicant details for a specific depot, filtered by access date and sector ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number |
| @TrackType | NVARCHAR(50) | Track type filter |
| @ToAccessDate | NVARCHAR(20) | To access date filter (inclusive) |
| @FromAccessDate | NVARCHAR(20) | From access date filter (inclusive) |
| @TARType | NVARCHAR(20) | TAR type filter |
| @SectorID | INT | Sector ID filter |

### Logic Flow
1. The procedure starts by setting the current date to a variable.
2. It creates two temporary tables: `#TmpAppList` and `#TmpSector`.
3. The `#TmpAppList` table is populated with applicant details from `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector`. The data is filtered by the input parameters, including depot line number, track type, access dates, TAR type, sector ID, and WF status.
4. The procedure then selects specific columns from the `#TmpAppList` table based on the sector ID filter.
5. Finally, it drops both temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector