# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters

### Purpose
This stored procedure retrieves and updates data from various tables to provide a comprehensive view of TVF (Traffic Video Feedback) acknowledgments for a specific set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number to filter the data (default is NULL). |
| @TrackType | nvarchar(50) | The track type to filter the data (default is NULL). |
| @OperationDate | date | The operation date to filter the data. |
| @AccessDate | date | The access date to filter the data. |

### Logic Flow
The procedure follows these steps:

1. It checks if the `@Line` parameter is 'DTL'. If it is, it proceeds with the filtering and processing of the data.
2. It retrieves the count of TVF acknowledgments for the specified `@AccessDate`.
3. If there are no acknowledgments, it truncates a temporary table (`#TMP_TVF_ToUpdate`) and inserts new records from the `TAMS_TAR` table based on the `TrackType` and `OperationDate`.
4. It loops through each record in the `#TMP_TVF_ToUpdate` table and updates the corresponding records in the `#TMP_OCCTVF_Ack` table.
5. If there are no acknowledgments, it inserts new records into the `#TMP_OCCTVF_Ack` table directly.

### Data Interactions
* **Reads:**
	+ [TAMS_TAR]
	+ [TAMS_TAR_TVF]
	+ [TAMS_TVF_Acknowledge]
	+ [TAMS_Station]
	+ [TAMS_User]
* **Writes:**
	+ #TMP_Station
	+ #TMP_OCCTVF_Ack
	+ #TMP_TVF_ToUpdate