# Procedure: sp_TAMS_TB_Gen_Summary_20230904_M

### Purpose
This stored procedure generates a summary of TAMS data for a specific date range, filtered by line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter on (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter on |
| @AccessDateFrom | NVARCHAR(20) | Start date for access data filtering |
| @AccessDateTo | NVARCHAR(20) | End date for access data filtering |
| @AccessType | NVARCHAR(20) | Access type to filter on |

### Logic Flow
The procedure first checks if the line is 'DTL'. If it is, it generates three sets of results based on different conditions:
- Condition 1: Power Off With Rack Out / 22KV Isolation
- Condition 2: Use of Tunnel Ventilation
- Condition 3: Other operations (including electrical section and nature of work)

If the line is not 'DTL', the procedure checks if it is 'NEL'. If it is, it generates five sets of results based on different conditions:
- Condition 1: Power Off With Rack Out / 22KV Isolation
- Condition 2: Use of Tunnel Ventilation
- Condition 3: Electrical section and nature of work
- Condition 4: NEL ISCS and Systems
- Condition 5: NEL Communications

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone (for NEL), TAMS_Get_TVF_Station, TAMS_Get_Station_Dir
* **Writes:** None