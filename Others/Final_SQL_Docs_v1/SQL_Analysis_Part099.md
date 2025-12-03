# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters
**Type:** Stored Procedure

The procedure retrieves data from the TAMS system for a specific date range and returns the results in a formatted manner.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID to filter the results by. |
| @Line | nvarchar(10) | The line number to filter the results by. (Optional) |
| @TrackType | nvarchar(50) | The track type to filter the results by. (Optional) |
| @OperationDate | date | The operation date to filter the results by. |
| @AccessDate | date | The access date to filter the results by. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: [TAMS_TAR], [TAMS_TVF_Acknowledge], [TAMS_Station]
* Writes: #TMP_OCCTVF_Ack, #TMP_TVF_ToUpdate