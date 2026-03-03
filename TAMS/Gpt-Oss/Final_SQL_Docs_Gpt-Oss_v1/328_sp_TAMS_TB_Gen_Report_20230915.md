# Procedure: sp_TAMS_TB_Gen_Report_20230915

### Purpose
Generate a formatted report of TAR records filtered by line, track type, access dates, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., 'NEL') |
| @TrackType | NVARCHAR(50) | Desired track type |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range |
| @AccessDateTo | NVARCHAR(20) | End of access date range |
| @AccessType | NVARCHAR(20) | Specific access type to filter, or NULL for all |

### Logic Flow
1. Convert the supplied `@AccessDateFrom` and `@AccessDateTo` strings to `DATETIME` values using style 103 (dd/mm/yyyy).  
2. Query the `TAMS_TAR` table for rows where the `AccessDate` (converted to `DATETIME` with style 103) falls between the two converted dates.  
3. Apply a status filter: if `@Line` equals 'NEL', require `TARStatusId = 9`; otherwise require `TARStatusId = 8`.  
4. If `@AccessType` is supplied, include only rows where `AccessType` matches; if it is NULL or empty, ignore this condition.  
5. Ensure the row’s `Line` equals the supplied `@Line` and its `TrackType` equals the supplied `@TrackType`.  
6. For each qualifying row, project the following columns:  
   - `TAR ID` from `TARNo`  
   - `Company/Dept` from `Company`  
   - `Access Type` from `AccessType`  
   - `Name` from `Name`  
   - `Access Stations` by calling the scalar UDF `TAMS_Get_Station` with the row’s `Id`  
   - `TAR Date` by converting `AccessDate` to `DATETIME` (style 101) and then to a string in style 105 (dd-mm-yyyy)  
   - `Electrical Section` by calling the scalar UDF `TAMS_Get_ES_NoBufferZone` with the row’s `Id`  
   - `Nature of Work` from `DescOfWork`  
   - `Remarks` from `ARRemark`  
7. Order the result set first by the converted `AccessDate` (style 101) and then by `TARNo`.

### Data Interactions
* **Reads:** TAMS_TAR  
* **Writes:** None

---