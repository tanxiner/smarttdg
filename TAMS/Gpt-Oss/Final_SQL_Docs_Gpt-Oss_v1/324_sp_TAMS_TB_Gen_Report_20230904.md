# Procedure: sp_TAMS_TB_Gen_Report_20230904

### Purpose
Generate a filtered TAR report based on line, track type, access date range, and access type, returning key details and related station and electrical section information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Optional filter for the TAR line identifier. |
| @TrackType | NVARCHAR(50) | Optional filter for the TAR track type. |
| @AccessDateFrom | NVARCHAR(20) | Start of the access date range (inclusive). |
| @AccessDateTo | NVARCHAR(20) | End of the access date range (inclusive). |
| @AccessType | NVARCHAR(20) | Optional filter for the TAR access type. |

### Logic Flow
1. Convert the `@AccessDateFrom` and `@AccessDateTo` parameters to `DATETIME` using style 103 (dd/mm/yyyy).  
2. Query the `TAMS_TAR` table for rows where:  
   - The `AccessDate` (converted to `DATETIME` with style 103) falls between the converted `@AccessDateFrom` and `@AccessDateTo`.  
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
   - Result of `dbo.TAMS_Get_ES(a.Id)` as Electrical Section.  
   - `DescOfWork` as Nature of Work.  
   - `ARRemark` as Remarks.  
4. Order the result set by `AccessDate` (converted to `DATETIME` with style 101) and then by `TARNo`.  
5. Return the ordered list to the caller.

### Data Interactions
* **Reads:** TAMS_TAR  
* **Writes:** None

---