# Procedure: sp_TAMS_TB_Gen_Report_20230911

### Purpose
Generate a report of TAR records that match specified line, track type, access date range, and optional access type, including station and electrical section details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Filter TARs by the specified line; NULL returns all lines. |
| @TrackType | NVARCHAR(50) | Filter TARs by the specified track type; NULL returns all track types. |
| @AccessDateFrom | NVARCHAR(20) | Start of the access date range (inclusive). |
| @AccessDateTo | NVARCHAR(20) | End of the access date range (inclusive). |
| @AccessType | NVARCHAR(20) | Optional filter for the access type; if NULL or empty, all types are returned. |

### Logic Flow
1. Convert the `@AccessDateFrom` and `@AccessDateTo` parameters to `DATETIME` using style 103 (dd/mm/yyyy).  
2. Query the `TAMS_TAR` table for rows where:  
   - The `AccessDate` (converted to `DATETIME` with style 103) falls between the converted `@AccessDateFrom` and `@AccessDateTo`.  
   - `TARStatusId` equals 8.  
   - `AccessType` matches `@AccessType` or `@AccessType` is NULL/empty.  
   - `Line` equals `@Line`.  
   - `TrackType` equals `@TrackType`.  
3. For each qualifying row, select the following columns:  
   - `TARNo` as “TAR ID”.  
   - `Company` as “Company/Dept”.  
   - `AccessType` as “Access Type”.  
   - `Name` as “Name”.  
   - Result of `dbo.TAMS_Get_Station(a.Id)` as “Access Stations”.  
   - `AccessDate` converted to `DATETIME` with style 101, then to `NVARCHAR(20)` with style 105, as “TAR Date”.  
   - Result of `dbo.TAMS_Get_ES_NoBufferZone(a.Id)` as “Electrical Section”.  
   - `DescOfWork` as “Nature of Work”.  
   - `ARRemark` as “Remarks”.  
4. Order the result set by the converted `AccessDate` (style 101) and then by `TARNo`.

### Data Interactions
* **Reads:** `TAMS_TAR`  
* **Writes:** None  

---