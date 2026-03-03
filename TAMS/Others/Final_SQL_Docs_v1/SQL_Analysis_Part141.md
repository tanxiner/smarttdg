# Procedure: sp_TAMS_RGS_Update_QTS_20230907
**Type:** Stored Procedure

The procedure updates the QTS status for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to update. |
| @InchargeNRIC | NVARCHAR(50) | The Incharge's NRIC. |
| @UserID | NVARCHAR(500) | The user ID updating the QTS status. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The message output for the procedure. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | The updated QTS code. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | The updated QTS line. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters
* **Writes:** TAMS_TOA_Audit