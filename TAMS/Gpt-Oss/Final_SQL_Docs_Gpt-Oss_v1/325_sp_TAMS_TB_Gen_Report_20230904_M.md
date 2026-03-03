# Procedure: sp_TAMS_TB_Gen_Report_20230904_M

### Purpose
Generate a filtered TAR report with station and electrical section details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Filter TARs by line identifier. |
| @TrackType | NVARCHAR(50) | Filter TARs by track type. |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range (inclusive). |
| @AccessDateTo | NVARCHAR(20) | End of access date range (inclusive). |
| @AccessType | NVARCHAR(20) | Filter TARs by access type; ignored if null or empty. |

### Logic Flow
1. Convert the `@AccessDateFrom` and `@AccessDateTo` parameters to `DATETIME` using style 103 (dd/mm/yyyy).  
2. Query the `TAMS_TAR` table for rows where:  
   - The `AccessDate` (converted to `DATETIME` with style 103) falls between the converted date range.  
   - `TARStatusId` equals 8.  
   - `AccessType` matches `@AccessType` or `@AccessType` is null/empty.  
   - `Line` equals `@Line`.  
   - `TrackType` equals `@TrackType`.  
3. For each qualifying row, select:  
   - `TARNo` as TAR ID.  
   - `Company` as Company/Dept.  
   - `AccessType` as Access Type.  
   - `Name` as Name.  
   - Result of `dbo.TAMS_Get_Station(a.Id)` as Access Stations.  
   - `AccessDate` formatted as `dd-mm-yyyy` (style 105).  
   - Result of `dbo.TAMS_Get_ES_NoBufferZone(a.Id)` as Electrical Section.  
   - `DescOfWork` as Nature of Work.  
   - `ARRemark` as Remarks.  
4. Order the output by `AccessDate` (converted with style 101) and then by `TARNo`.

### Data Interactions
* **Reads:** TAMS_TAR  
* **Writes:** None