# Procedure: sp_TAMS_Applicant_List_OnLoad

### Purpose
This stored procedure retrieves a list of applicants for a specific line, sector, and access date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to retrieve applicants for. |

### Logic Flow
1. The procedure starts by determining the current date.
2. It then truncates two temporary tables, #TmpSector and #TmpAppList, which will be used to store sector data and applicant information, respectively.
3. The procedure inserts data into #TmpSector from TAMS_Sector table based on the specified line number, track type, and access date range.
4. Next, it inserts data into #TmpAppList from TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables based on the same criteria as #TmpSector.
5. The procedure then selects applicant information from #TmpAppList and joins it with #TmpSector to retrieve sector data for each applicant.
6. Finally, the procedure drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables.
* **Writes:** #TmpSector and #TmpAppList tables.