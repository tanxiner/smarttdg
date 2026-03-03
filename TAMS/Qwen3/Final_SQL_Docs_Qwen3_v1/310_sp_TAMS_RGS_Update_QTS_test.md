# Procedure: sp_TAMS_RGS_Update_QTS_test

### Purpose
This stored procedure updates the qualification status of a user's access to a TAR (Technical Access Record) based on their QTS (Qualification and Testing System) code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record being updated. |
| @InchargeNRIC | NVARCHAR(50) | The National Registration Identification Number (NRIC) of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the user whose access is being updated. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that returns a message indicating the result of the update operation. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter that returns the QTS qualification code for the user's access. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter that returns the line number associated with the user's access. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal transaction flag to 1 and begins a new transaction.
2. It creates a temporary table #tmpnric to store the in-charge person's details.
3. The procedure then selects the TAR record associated with the given @TARID and retrieves the user's access date, TOA ID, and access type from TAMS_TOA and TAMS_TAR tables respectively.
4. It then checks if the user has a valid QTS qualification code for their access. If not, it sets an error message and returns without updating the TAR record.
5. If the user has a valid QTS qualification code, it updates the TAR record with the new QTS qualification code and inserts an audit record into TAMS_TOA_Audit table.
6. The procedure then checks if there are any errors during the update operation. If so, it rolls back the transaction and returns an error message.
7. If no errors occur, it commits the transaction and returns a success message with the updated QTS qualification code and line number.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* Writes: #tmpnric (temporary table), TAMS_TOA (TAR record)