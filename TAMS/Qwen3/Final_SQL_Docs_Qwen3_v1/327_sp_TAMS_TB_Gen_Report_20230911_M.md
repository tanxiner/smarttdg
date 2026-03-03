# Procedure: sp_TAMS_TB_Gen_Report_20230911_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and other criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by (e.g., NEL). |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by (optional). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the specified line, track type, and access date range.
3. If a specific line is specified, it further filters by TAR status ID 9 for NEL lines or 8 for other lines.
4. The procedure also filters by access type if provided.
5. Finally, it orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No data is written to any tables; only read operations are performed.