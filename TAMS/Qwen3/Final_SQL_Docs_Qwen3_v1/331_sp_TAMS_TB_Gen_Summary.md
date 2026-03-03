# Procedure: sp_TAMS_TB_Gen_Summary

### Purpose
This stored procedure generates a summary of TAMS data based on input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access data filtering |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access data filtering |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by |

### Logic Flow
The procedure first checks if the `@Line` parameter is 'DTL'. If it is, it generates three separate result sets based on different conditions. The conditions are:
- Power Off With Rack Out / 22KV Isolation
- Use of Tunnel Ventilation
- Electrical Section (Electrical Section and Nature of Work)

If the `@Line` parameter is not 'DTL', the procedure checks if it is 'NEL'. If it is, it generates five separate result sets based on different conditions. The conditions are:
- Power Off With Rack Out / 22KV Isolation
- Use of Tunnel Ventilation
- Electrical Section (Electrical Section and Nature of Work)
- NEL ISCS and Systems
- NEL Communications

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone (for NEL), TAMS_Get_TVF_Station