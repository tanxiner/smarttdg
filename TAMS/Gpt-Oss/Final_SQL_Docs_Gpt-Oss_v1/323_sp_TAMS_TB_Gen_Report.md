# Procedure: sp_TAMS_TB_Gen_Report

### Purpose
Generate a TAR report filtered by line, track type, access date range, and access type, returning key details for each TAR.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line identifier (e.g., 'DTL' or 'NEL') to filter TAR records. |
| @TrackType | NVARCHAR(50) | Filters TAR records by the track type. |
| @AccessDateFrom | NVARCHAR(20) | Start of the access date range for filtering. |
| @AccessDateTo | NVARCHAR(20) | End of the access date range for filtering. |
| @AccessType | NVARCHAR(20) | Optional filter for the access type; if null or empty, all types are included. |

### Logic Flow
1. Evaluate whether @Line equals 'DTL'.
2. If true, execute a SELECT that:
   - Retrieves TAR details from TAMS_TAR.
   - Calls TAMS_Get_Station to list access stations.
   - Calls TAMS_Get_ES_NoBufferZone to provide the electrical section.
   - Formats the access date.
   - Applies filters: date range, TARStatusId (8 for DTL, 9 for NEL), optional access type, matching line, and track type.
   - Orders results by access date and TAR number.
3. If false, execute a similar SELECT that:
   - Retrieves TAR details from TAMS_TAR.
   - Calls TAMS_Get_Station for access stations.
   - Calls TAMS_Get_ES_NoBufferZone for the track sector.
   - Formats the access date.
   - Applies the same filters as above.
   - Orders results by access date and TAR number.

### Data Interactions
* **Reads:** TAMS_TAR
* **Writes:** None

---