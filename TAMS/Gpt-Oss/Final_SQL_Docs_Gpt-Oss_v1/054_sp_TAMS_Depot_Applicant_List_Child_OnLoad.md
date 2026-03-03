# Procedure: sp_TAMS_Depot_Applicant_List_Child_OnLoad

### Purpose
Retrieves a list of TAR applicants for a specified sector, filtered by line, track type, access date range, and TAR type, and returns the results ordered by TAR ID.

### Parameters
| Name            | Type          | Purpose |
| :-------------- | :------------ | :------ |
| @Line           | NVARCHAR(10)  | Target line identifier. |
| @TrackType      | NVARCHAR(50)  | Target track type. |
| @ToAccessDate   | NVARCHAR(20)  | Upper bound of access date filter. |
| @FromAccessDate | NVARCHAR(20)  | Lower bound of access date filter. |
| @TARType        | NVARCHAR(20)  | TAR type filter; empty string means all types. |
| @SectorID       | INT           | Sector identifier to limit results. |

### Logic Flow
1. Capture the current date in `@CurrDate`.  
2. Create a temporary table `#TmpAppList` to hold intermediate applicant data.  
3. Truncate `#TmpAppList` to ensure it starts empty.  
4. Populate `#TmpAppList` by selecting rows from `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector` where:  
   - The TAR and sector records are linked.  
   - The workflow status matches the TAR status.  
   - The line and track type match the supplied parameters.  
   - The TAR status is not zero.  
   - The sector is active and the current date falls within its effective period.  
   - The TAR access date falls between `@ToAccessDate` and `@FromAccessDate`.  
   - The TAR type matches `@TARType` or `@TARType` is empty.  
5. From `#TmpAppList`, select rows whose `SectorID` equals `@SectorID`.  
6. Group the selected rows by all columns to eliminate duplicates.  
7. Order the final result set by `TARID`.  
8. Drop the temporary table `#TmpAppList`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, `TAMS_Sector`  
* **Writes:** Temporary table `#TmpAppList` (created, truncated, populated, then dropped)