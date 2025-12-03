# Procedure: sp_TAMS_RGS_Cancel_20250403
**Type:** Stored Procedure

The purpose of this stored procedure is to cancel a Request for Goods (RGS) on TAMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR sector being cancelled. |
| @CancelRemarks | NVARCHAR(1000) | A remark to be associated with the cancellation. |
| @UserID | NVARCHAR(500) | The ID of the user performing the cancellation. |
| @tracktype | nvarchar(50)='MAINLINE' | The type of track being used (in this case, 'MAINLINE'). |
| @Message | NVARCHAR(500) | An output parameter to store any error messages. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Depot_Auth, TAMS_Parameters
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_Depot_Auth, TAMS_Parameters