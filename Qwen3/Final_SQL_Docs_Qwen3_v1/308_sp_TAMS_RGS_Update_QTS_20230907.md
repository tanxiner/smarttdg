# Procedure: sp_TAMS_RGS_Update_QTS_20230907

### Purpose
This stored procedure updates the qualification status of a TAR (Tender Acceptance Record) based on the QTS (Qualification Testing System) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC number of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the update. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter to store the QTS qualification code. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter to store the line number of the TAR. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal flag and begins a new transaction.
2. It creates a temporary table #tmpnric to store the in-charge person's details.
3. The procedure then selects the TAR ID, access date, TOA ID, and access type from the TAMS_TOA and TAMS_TAR tables based on the provided TAR ID.
4. It retrieves the QTS qualification code and protocol code for the selected line number from the TAMS_Parameters table.
5. If the in-charge person's status is 'InValid', it checks if they have access to the protection area. If not, it truncates the temporary table and sets the in-charge person's details again.
6. It then updates the TAR with the new QTS qualification code and line number, and inserts an audit record into the TAMS_TOA_Audit table.
7. The procedure then calls another stored procedure [mssqldevpsvr1].[QTSDB].[dbo].[sp_api_tams_qts_upd_accessdate] to update the access date of the in-charge person based on the new QTS qualification code.
8. If an error occurs during this process, it sets an error message and returns it to the caller.
9. Finally, if no errors occurred, it commits the transaction and returns a success message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* Writes: TAMS_TOA