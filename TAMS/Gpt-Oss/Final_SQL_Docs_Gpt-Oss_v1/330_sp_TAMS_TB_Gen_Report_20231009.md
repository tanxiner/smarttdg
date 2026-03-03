# Procedure: sp_TAMS_TB_Gen_Report_20231009

### Purpose
Generate a TAR report filtered by line, track type, access date range, and access type, returning key details for each matching record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., NEL). |
| @TrackType | NVARCHAR(50) | Desired track type to filter on. |
| @AccessDateFrom | NVARCHAR(20) | Start of the access date range. |
| @AccessDateTo | NVARCHAR(20) | End of the access date range. |
| @AccessType | NVARCHAR(20) | Optional access type filter; ignored if NULL or empty. |

### Logic Flow
1. Convert the `@AccessDateFrom` and `@AccessDateTo` parameters to `DATETIME` values using style 103 (dd/mm/yyyy).  
2. Query the `TAMS_TAR` table selecting the TAR number, company, access type, name, and other descriptive fields.  
3. For each record, call `dbo.TAMS_Get_Station` with the record’s `Id` to retrieve the access stations, and call `dbo.TAMS_Get_ES_NoBufferZone` to obtain the electrical section.  
4. Convert the record’s `AccessDate` to a `DATETIME` (style 101) and then format it as `dd-mm-yyyy` (style 105) for display.  
5. Apply filters:  
   - `AccessDate` must fall between the converted `@AccessDateFrom` and `@AccessDateTo`.  
   - `TARStatusId` must equal 9 when `@Line` is 'NEL'; otherwise it must equal 8.  
   - If `@AccessType` is supplied, the record’s `AccessType` must match it; if `@AccessType` is NULL or empty, this filter is bypassed.  
   - The record’s `Line` must equal `@Line`.  
   - The record’s `TrackType` must equal `@TrackType`.  
6. Order the resulting rows first by the converted `AccessDate` (style 101) and then by `TARNo`.  
7. Return the ordered result set to the caller.

### Data Interactions
* **Reads:** `TAMS_TAR`  
* **Writes:** None

---