# Procedure: sp_TAMS_Applicant_List_Child_OnLoad

### Purpose
Retrieve a distinct list of TAR applicants for a specified sector within a line, filtered by access date range and optional TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier |
| @TrackType | NVARCHAR(50) | (unused in current logic) |
| @ToAccessDate | NVARCHAR(20) | Upper bound of access date filter |
| @FromAccessDate | NVARCHAR(20) | Lower bound of access date filter |
| @TARType | NVARCHAR(20) | Optional TAR type filter |
| @SectorID | INT | Sector identifier to return records for |

### Logic Flow
1. Determine the current date (`@CurrDate`) truncated to day precision.  
2. Create a temporary table `#TmpAppList` to hold intermediate applicant data.  
3. Clear any existing rows from `#TmpAppList`.  
4. Populate `#TmpAppList` by selecting records from `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector` where:  
   - The TAR is linked to a sector and a workflow status.  
   - The workflow status type is `TARWFStatus`.  
   - The TAR’s line matches `@Line`.  
   - The TAR status is not zero.  
   - The sector is active and the current date falls within its effective period.  
   - The TAR’s access date lies between `@ToAccessDate` and `@FromAccessDate`.  
   - The TAR type matches `@TARType` if supplied.  
   - The direction of the sector is mapped to a numeric flag (1 for `BB`/`NB`, otherwise 2).  
   - The sector’s colour code is captured, defaulting to an empty string if null.  
5. From `#TmpAppList`, select rows where `SectorID` equals `@SectorID`.  
6. Group the selected rows by all columns except `SectorID`, `SectorStr`, and `Direction` to eliminate duplicates.  
7. Order the result set by `TARID`.  
8. Drop the temporary table `#TmpAppList`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, `TAMS_Sector`  
* **Writes:** Temporary table `#TmpAppList` (inserted, then dropped)