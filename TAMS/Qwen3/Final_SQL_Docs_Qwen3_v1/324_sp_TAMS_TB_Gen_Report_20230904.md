# Procedure: sp_TAMS_TB_Gen_Report_20230904

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | The end date of the access date range. |
| @AccessType | NVARCHAR(20) | The access type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the provided access date range, track type, and access type.
3. If no access type is specified, it defaults to an empty string.
4. The procedure then joins with two other tables: dbo.TAMS_Get_Station and dbo.TAMS_Get_ES.
5. It orders the results by the access date in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR table, dbo.TAMS_Get_Station table, dbo.TAMS_Get_ES table