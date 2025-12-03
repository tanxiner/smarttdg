# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_Hnin

### Purpose
This stored procedure generates a list of applicant records for a specific sector, filtered by access date and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector records. |
| @TrackType | NVARCHAR(50) | The track type to filter the applicant records. |
| @ToAccessDate | NVARCHAR(20) | The start date for access filtering. |
| @FromAccessDate | NVARCHAR(20) | The end date for access filtering. |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicant records. |
| @SectorID | INT | The ID of the sector to retrieve the applicant records for. |

### Logic Flow
1. The procedure starts by setting a current date variable.
2. It creates a temporary table #TmpAppList to store the filtered applicant records.
3. The procedure truncates the existing data in #TmpAppList and inserts new data based on the following conditions:
	* The sector ID matches the specified @SectorID.
	* The access date falls within the range defined by @ToAccessDate and @FromAccessDate.
	* The track type matches the specified @TARType or is empty (default).
4. It selects the required columns from #TmpAppList and groups them by TARID, TARNo, TARType, AccessDate, AccessType, Company, WFStatus, and ColorCode.
5. The procedure sorts the results in ascending order by TARID.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector
* Writes: #TmpAppList