# Procedure: sp_TAMS_RGS_Update_QTS

### Purpose
This stored procedure updates the qualification status of a train's access date and retrieves the corresponding QTS (Qualification Time System) code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the train to update. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the current user. |
| @TrackType | NVARCHAR(50)='Mainline' | The track type of the train (default: Mainline). |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message indicating the result of the update operation. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | The QTS code corresponding to the updated qualification status. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | The line number corresponding to the updated qualification status. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Create a temporary table `#tmpnric` to store the results of the QTS check.
3. Truncate the temporary table and insert a record into it using the `sp_TAMS_TOA_QTS_Chk` stored procedure.
4. Retrieve the in-charge name and status from the temporary table.
5. Check if the in-charge status is 'InValid'. If so, perform additional checks:
	* If the access type is 'Protection', truncate the temporary table and insert a new record using `sp_TAMS_TOA_QTS_Chk`.
	* Otherwise, set the QTS fin status to 'InValid' and the QTS fin qualification code to an empty string.
6. If the in-charge status is not 'InValid', update the QTS fin status and qualification code based on the retrieved values from the temporary table.
7. Call the `sp_api_tams_qts_upd_accessdate` stored procedure to update the access date of the train.
8. Insert an audit record into the `TAMS_TOA_Audit` table.
9. If any errors occur during the update operation, log the error and return a message indicating the result.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, QTSDB (for storing audit records)
* Writes: TAMS_TOA_Audit