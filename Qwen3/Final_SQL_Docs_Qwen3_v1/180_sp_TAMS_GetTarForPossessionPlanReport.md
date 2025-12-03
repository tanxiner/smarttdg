# Procedure: sp_TAMS_GetTarForPossessionPlanReport

### Purpose
This stored procedure retrieves data from the TAMS_TAR table for a possession plan report, filtering by line number, track type, access type, and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @AccessType | nvarchar(50) | The access type to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access date range (inclusive). |
| @AccessDateTo | nvarchar(50) | The end date of the access date range (inclusive). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the results based on the provided line number, track type, and access type.
3. Additionally, it applies a date filter to only include records where the access date falls within the specified range (from @AccessDateFrom to @AccessDateTo).
4. The filtered data is then returned as part of the procedure's output.

### Data Interactions
* **Reads:** TAMS_TAR table