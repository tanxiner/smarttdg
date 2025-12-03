# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303

### Purpose
This stored procedure generates a list of applicants for a specific sector, based on access dates and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @ToAccessDate | NVARCHAR(20) | The end date for access. |
| @FromAccessDate | NVARCHAR(20) | The start date for access. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @SectorID | INT | The sector ID to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and truncating two temporary tables: #TmpSector and #TmpAppList.
2. It then inserts data into #TmpSector, which contains information about sectors, including their order and direction.
3. Next, it inserts data into #TmpAppList, which contains information about applicants, including their TAR ID, access date, and sector ID.
4. The procedure then selects data from #TmpAppList where the sector ID matches the input @SectorID, and orders the results by TAR ID.
5. Finally, it drops the temporary tables.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus
* Writes: None