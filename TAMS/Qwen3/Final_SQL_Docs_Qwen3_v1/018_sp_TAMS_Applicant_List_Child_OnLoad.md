# Procedure: sp_TAMS_Applicant_List_Child_OnLoad

### Purpose
This stored procedure generates a list of applicants for a specific sector, filtered by access date and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector by. |
| @TrackType | NVARCHAR(50) | The track type to filter the applicants by. |
| @ToAccessDate | NVARCHAR(20) | The start date for access filtering. |
| @FromAccessDate | NVARCHAR(20) | The end date for access filtering. |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicants by. |
| @SectorID | INT | The ID of the sector to retrieve applicants for. |

### Logic Flow
1. The procedure starts by setting a current date variable.
2. It creates a temporary table #TmpAppList to store the filtered applicant data.
3. The procedure truncates the existing data in #TmpAppList and inserts new data from TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables based on the provided parameters.
4. It filters the applicants by sector ID and access date range.
5. The procedure groups the filtered data by TARID and returns a list of applicant details.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector tables.
* **Writes:** #TmpAppList table.