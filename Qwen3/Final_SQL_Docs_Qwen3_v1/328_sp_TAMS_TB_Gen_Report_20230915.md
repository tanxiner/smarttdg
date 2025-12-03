# Procedure: sp_TAMS_TB_Gen_Report_20230915

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and other specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (e.g., 'NEL') |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table based on the specified parameters.
2. It filters the data by access date range, using the provided start and end dates.
3. It also applies additional filters based on the line type, track type, and access type specified in the parameters.
4. The procedure then joins with other tables (TAMS_Get_Station and TAMS_Get_ES_NoBufferZone) to retrieve additional data for each record.
5. Finally, it orders the results by access date and TAR ID.

### Data Interactions
* **Reads:** TAMS_TAR table, TAMS_Get_Station table, TAMS_Get_ES_NoBufferZone table