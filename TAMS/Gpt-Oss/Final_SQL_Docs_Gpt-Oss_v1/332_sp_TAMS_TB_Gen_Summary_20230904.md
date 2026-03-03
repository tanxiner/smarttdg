# Procedure: sp_TAMS_TB_Gen_Summary_20230904

### Purpose
Generate a line‑specific summary of TAR records within a date range, optionally filtered by access type and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (DTL or NEL). |
| @TrackType | NVARCHAR(50) | Filter by track type. |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range. |
| @AccessDateTo | NVARCHAR(20) | End of access date range. |
| @AccessType | NVARCHAR(20) | Optional access type filter. |

### Logic Flow
1. **Determine Line Context** – The procedure first checks the value of @Line.  
2. **DTL Path** – If @Line equals DTL, the procedure executes a series of ten SELECT statements (labeled 0 through 9).  
   - Each statement selects formatted access date, TAR ID, electrical section or station information, nature of work, and remarks.  
   - All statements filter records where AccessDate falls between @AccessDateFrom and @AccessDateTo, TARStatusId is 8, and the optional AccessType matches @AccessType (or @AccessType is null).  
   - The first two statements additionally join with TAMS_TAR_AccessReq and TAMS_Access_Requirement to enforce specific OperationRequirement values.  
   - Statements 3 to 8 apply company‑based LIKE filters to narrow the result set to particular DTL departments (POWER, COMMS, Pway & FM, RS, Operations, etc.).  
   - Statement 9 excludes companies listed in TAMS_Parameters for the DTL line.  
   - Each query orders results by AccessDate and TARNo.  
3. **NEL Path** – If @Line equals NEL, the procedure runs six SELECT statements (labeled 0 through 5).  
   - These statements format the date with day abbreviation, include power section or station details, and present time ranges.  
   - Filters mirror those in the DTL path: date range, TARStatusId 8, optional AccessType, line NEL, and track type.  
   - Statement 0 and 1 join with TAMS_TAR_AccessReq and TAMS_Access_Requirement to enforce OperationRequirement conditions.  
   - Statement 1 further filters on Is13ASocket.  
   - Statements 2 to 5 target specific NEL departments (Signalling, ISCS and Systems, Communications) and use ROW_NUMBER for sequencing.  
   - All queries order by AccessDate and TARNo.  
4. **No Write Operations** – The procedure only retrieves data; it does not modify any tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters  
* **Writes:** None