# Procedure: sp_TAMS_GetTarForPossessionPlanReport

### Purpose
Retrieves TAR records that match specified line, track type, access type, and access date range for a possession plan report.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Filters records by the Line column. |
| @TrackType | nvarchar(50) | Filters records by the TrackType column. |
| @AccessType | nvarchar(50) | Filters records by the AccessType column. |
| @AccessDateFrom | nvarchar(50) | Lower bound of the AccessDate filter, converted to datetime. |
| @AccessDateTo | nvarchar(50) | Upper bound of the AccessDate filter, converted to datetime. |

### Logic Flow
1. Accepts optional filter parameters for line, track type, access type, and a date range.  
2. Converts the `@AccessDateFrom` and `@AccessDateTo` strings to datetime values using style 103 (dd/mm/yyyy).  
3. Executes a SELECT that returns all columns listed from the `TAMS_TAR` table.  
4. Applies a WHERE clause that enforces equality on `Line`, `TrackType`, and `AccessType`, and ensures `AccessDate` falls between the converted date bounds (inclusive).  
5. Returns the resulting rows to the caller.

### Data Interactions
* **Reads:** TAMS_TAR  
* **Writes:** None