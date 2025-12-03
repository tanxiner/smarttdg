# Procedure: sp_TAMS_OCC_GetOCCTVFAckFromTableByParameters

### Purpose
This stored procedure retrieves data from various tables to generate a report of TVF (Traffic Video Feedback) acknowledgments for a specific date range, taking into account user permissions and station IDs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number (DTL or other). |
| @OperationDate | date | The operation date for which to retrieve data. |
| @AccessDate | date | The access date for which to retrieve data. |

### Logic Flow
1. If the `@Line` parameter is 'DTL', the procedure proceeds with retrieving data.
2. It counts the number of TVF acknowledgments for the specified `@OperationDate`.
3. If no acknowledgments are found, it truncates a temporary table (`#TMP_TVF_ToUpdate`) and inserts new records from the `TAMS_TAR` table based on the `AccessDate`.
4. The procedure then iterates through each record in the `#TMP_TVF_ToUpdate` table, updating the corresponding records in the `#TMP_OCCTVF_Ack` table.
5. If no acknowledgments are found for the specified line and date range, it inserts new records into both tables.

### Data Interactions
* **Reads:**
	+ [TAMS_TAR]
	+ [TAMS_TVF_Acknowledge]
	+ [TAMS_Station]
	+ [TAMS_User]
* **Writes:**
	+ #TMP_OCCTVF_Ack
	+ #TMP_TVF_ToUpdate