# Procedure: sp_TAMS_Depot_RGS_OnLoad_Enq

### Purpose
This stored procedure is used to retrieve data for a Depot RGS (Railway Grouping System) on-load inquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to query. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @accessDate | Date | The access date to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and time, as well as a cutoff time for the operation.
2. It then retrieves the possession, protection, and cancellation background values from the TAMS_Parameters table based on the line number provided.
3. Next, it selects data from the TAMS_TAR and TAMS_TOA tables where the access date matches the provided value, the track type is 'DEPOT', and the line number matches the provided value.
4. The procedure then calculates various times (PowerOffTime, CircuitBreakOutTime, RadioMsgTime, LineClearMsgTime) based on the retrieved data.
5. It also retrieves additional information such as parties involved, work description, contact numbers, TOA status, and remarks for each TAR and TOA record.
6. Finally, the procedure orders the results by access type, TAR number, and then by other fields.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_TAR, TAMS_TOA