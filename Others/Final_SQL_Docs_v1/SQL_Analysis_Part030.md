# Procedure: sp_TAMS_Depot_RGS_Update_QTS
**Type:** Stored Procedure

The purpose of this stored procedure is to update the QTS (Qualification Tracking System) status for a specific train line and depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the train line. |
| @InchargeNRIC | NVARCHAR(50) | The National Registration Identity Card number of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the current user. |
| @TrackType | NVARCHAR(50) | The type of track (Mainline or Depot). Default value is Mainline. |
| @Message | NVARCHAR(500) | Output parameter to store the message. |
| @QTSQCode | NVARCHAR(50) | Output parameter to store the QTS qualification code. |
| @QTSLine | NVARCHAR(10) | Output parameter to store the train line number. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_QTS_Error_Log
* **Writes:** TAMS_TOA_Audit