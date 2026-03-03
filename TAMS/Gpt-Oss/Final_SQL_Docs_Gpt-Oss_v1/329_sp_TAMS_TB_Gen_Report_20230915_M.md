# Procedure: sp_TAMS_TB_Gen_Report_20230915_M

### Purpose
Generate a TAR report filtered by line, track type, access dates, and access type, returning different column aliases for DTL versus other lines.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier (e.g., 'DTL', 'NEL') |
| @TrackType | NVARCHAR(50) | Track type filter |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range |
| @AccessDateTo | NVARCHAR(20) | End of access date range |
| @AccessType | NVARCHAR(20) | Optional access type filter |

### Logic Flow
1. Check if @Line equals 'DTL'.
2. If true, execute a SELECT that:
   - Retrieves TAR details from TAMS_TAR.
   - Filters rows where AccessDate falls between @AccessDateFrom and @AccessDateTo.
   - Requires TARStatusId to be 8 (or 9 if @Line were 'NEL', but this branch never occurs here).
   - Matches AccessType if provided, otherwise ignores the filter.
   - Matches Line and TrackType to the supplied parameters.
   - Orders results by AccessDate and TARNo.
   - Uses TAMS_Get_Station to list access stations and TAMS_Get_ES_NoBufferZone for the electrical section.
3. If @Line is not 'DTL', execute a similar SELECT with the same filters and ordering, but:
   - Uses TAMS_Get_ES_NoBufferZone for the track sector instead of the electrical section.
4. Return the resulting rows.

### Data Interactions
* **Reads:** TAMS_TAR
* **Writes:** None

---