# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_Hnin

### Purpose
Retrieves a list of TAR records for a specified sector, filtered by line, track type, access dates, and TAR type, and returns distinct entries with status and colour information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier for TAR and sector filtering. |
| @TrackType | NVARCHAR(50) | Target track type used to match TAR and workflow status. |
| @ToAccessDate | NVARCHAR(20) | Upper bound of the access date range (converted to DATE). |
| @FromAccessDate | NVARCHAR(20) | Lower bound of the access date range (converted to DATE). |
| @TARType | NVARCHAR(20) | Optional TAR type filter; if null or empty, all types are included. |
| @SectorID | INT | Identifier of the sector whose TARs are to be returned. |

### Logic Flow
1. **Current Date Setup** – `@CurrDate` is set to today’s date (time truncated).  
2. **Temporary Table Creation** – `#TmpAppList` is created to hold intermediate TAR data.  
3. **Clear Temporary Table** – Any existing rows in `#TmpAppList` are removed.  
4. **Populate Temporary Table** – A join across `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector` pulls TAR records that satisfy:  
   * Matching line, track type, and workflow status.  
   * Active sector (`IsActive = 1`) within its effective date range.  
   * TAR status not zero.  
   * Access date between `@ToAccessDate` and `@FromAccessDate`.  
   * TAR type matches `@TARType` if supplied.  
   * Workflow type is `TARWFStatus`.  
   The selected fields include TAR identifiers, numbers, types, access details, company, workflow status, sector information, direction flag (1 for 'BB'/'NB', 2 otherwise), and colour code.  
5. **Final Selection** – From `#TmpAppList`, rows where `SectorID` equals `@SectorID` are selected.  
   * The result set is grouped by all selected columns to eliminate duplicates.  
   * Rows are ordered by `TARID`.  
6. **Cleanup** – `#TmpAppList` is dropped.

### Data Interactions
* **Reads:**  
  * `TAMS_TAR`  
  * `TAMS_TAR_Sector`  
  * `TAMS_WFStatus`  
  * `TAMS_Sector`  

* **Writes:**  
  * Temporary table `#TmpAppList` (created, truncated, populated, then dropped).