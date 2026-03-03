# Procedure: sp_TAMS_TB_Gen_Summary_20230904_M

### Purpose
Generate a line‑specific summary of TAR records, filtered by date range, track type and access type, and output detailed columns for each category of work.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., 'DTL', 'NEL') |
| @TrackType | NVARCHAR(50) | Filter by track type |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range |
| @AccessDateTo | NVARCHAR(20) | End of access date range |
| @AccessType | NVARCHAR(20) | Optional access type filter |

### Logic Flow
1. **Line Check** – The procedure first inspects the @Line parameter.  
   * If @Line equals 'DTL', it executes a series of ten SELECT statements (numbered 0–9).  
   * If @Line equals 'NEL', it executes six SELECT statements (numbered 0–5).  

2. **DTL Branch** – For each numbered query:  
   * The query selects TAR records where `TARStatusId = 8` and the access date falls within the supplied range.  
   * Additional filters vary by query:  
     * Query 0 and 1 join with `TAMS_TAR_AccessReq` and `TAMS_Access_Requirement` to capture specific operation requirements.  
     * Queries 2–5 filter by company patterns such as '%DTL SIG%', '%DTL POWER%', '%DTL COMMS%', and '%DTL Pway & FM%'.  
     * Query 6 filters by companies containing 'DTL RS'.  
     * Query 7 filters by companies containing 'DTL Operations', 'DTL Training', or 'DTL OPS'.  
     * Query 8 selects records whose company is not listed in `TAMS_Parameters` for the line.  
     * Query 9 selects all remaining DTL records, adding company and name columns.  
   * Each query orders results by access date and TAR number.  
   * Columns returned include formatted access date, TAR ID, electrical section (via `TAMS_Get_ES_NoBufferZone`), nature of work, and remarks.  
   * Query 5 additionally returns access stations via `TAMS_Get_Station`.  

3. **NEL Branch** – For each numbered query:  
   * Queries 0 and 1 join with `TAMS_TAR_AccessReq` and `TAMS_Access_Requirement` to capture specific operation requirements, returning power section, time ranges, and activities.  
   * Query 2 returns TVF‑related data, including company, TVF mode, direction, and time ranges.  
   * Query 3 focuses on signalling work, returning stations and time ranges.  
   * Queries 4 and 5 use `ROW_NUMBER` to number rows and return detailed work information for 'NEL ISCS and Systems' and 'NEL Communications', respectively.  
   * Each query orders by access date and TAR number.  
   * Columns include formatted dates, time ranges, TAR ID, company/department, stations, track sector, and remarks.  

4. **Completion** – After executing the appropriate set of queries, the procedure ends.

### Data Interactions
* **Reads:**  
  * TAMS_TAR  
  * TAMS_TAR_AccessReq  
  * TAMS_Access_Requirement  
  * TAMS_Parameters  

* **Writes:** None.