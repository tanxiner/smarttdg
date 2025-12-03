# Procedure: sp_TAMS_TB_Gen_Report_20230904_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line number to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the specified line number, track type, and access date range.
3. The data is then joined with two other tables: dbo.TAMS_Get_Station and dbo.TAMS_Get_ES_NoBufferZone to retrieve additional information.
4. The procedure orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR, dbo.TAMS_Get_Station, dbo.TAMS_Get_ES_NoBufferZone