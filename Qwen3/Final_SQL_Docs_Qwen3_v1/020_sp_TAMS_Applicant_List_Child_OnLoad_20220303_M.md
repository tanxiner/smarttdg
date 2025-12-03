# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303_M

### Purpose
This stored procedure generates a list of applicant records for a specific sector, filtered by access date and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector records. |
| @ToAccessDate | NVARCHAR(20) | The end of the access date range (inclusive). |
| @FromAccessDate | NVARCHAR(20) | The start of the access date range (inclusive). |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicant records. |
| @SectorID | INT | The ID of the sector for which to retrieve the applicant records. |

### Logic Flow
1. The procedure starts by declaring a variable `@CurrDate` with the current date and time.
2. It creates two temporary tables, `#TmpSector` and `#TmpAppList`, to store the filtered sector and applicant data, respectively.
3. The procedure truncates both temporary tables before inserting new data.
4. For the `#TmpSector` table, it selects rows from `TAMS_Sector` where the line number matches the input parameter `@Line`, the record is active, and the access date falls within the specified range. It also orders the results by sector order.
5. For the `#TmpAppList` table, it joins multiple tables (`TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector`) to filter the applicant records based on the input parameters. The join conditions include matching the TAR ID with the sector ID, accessing the correct record within the specified access date range, and filtering by TAR type.
6. After populating both temporary tables, the procedure selects the relevant columns from `#TmpAppList` where the sector ID matches the input parameter `@SectorID`. It groups the results by TAR ID and orders them in ascending order.
7. Finally, the procedure drops both temporary tables to clean up.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector
* **Writes:** #TmpSector, #TmpAppList