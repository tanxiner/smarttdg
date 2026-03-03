# Procedure: sp_TAMS_TB_Gen_Report_20230911_M

### Purpose
Generates a TAR report filtered by line, track type, access date range, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier (e.g., NEL) |
| @TrackType | NVARCHAR(50) | Track type filter |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range |
| @AccessDateTo | NVARCHAR(20) | End of access date range |
| @AccessType | NVARCHAR(20) | Access type filter (optional) |

### Logic Flow
1. Convert the supplied date strings to `DATETIME` using style 103 (dd/mm/yyyy).  
2. Select rows from `TAMS_TAR` where:
   - The `AccessDate` falls between the converted `@AccessDateFrom` and `@AccessDateTo`.  
   - `TARStatusId` equals 9 if `@Line` is 'NEL'; otherwise it equals 8.  
   - `AccessType` matches `@AccessType` if provided; otherwise any type is accepted.  
   - `Line` equals `@Line`.  
   - `TrackType` equals `@TrackType`.  
3. For each qualifying row, project the following columns:
   - `TAR ID` from `TARNo`.  
   - `Company/Dept` from `Company`.  
   - `Access Type` from `AccessType`.  
   - `Name` from `Name`.  
   - `Access Stations` via `dbo.TAMS_Get_Station(Id)`.  
   - `TAR Date` formatted as dd-mm-yyyy.  
   - `Electrical Section` via `dbo.TAMS_Get_ES_NoBufferZone(Id)`.  
   - `Nature of Work` from `DescOfWork`.  
   - `Remarks` from `ARRemark`.  
4. Order the result set by `AccessDate` (converted to datetime) and `TARNo`.

### Data Interactions
* **Reads:** `TAMS_TAR`  
* **Writes:** None

---