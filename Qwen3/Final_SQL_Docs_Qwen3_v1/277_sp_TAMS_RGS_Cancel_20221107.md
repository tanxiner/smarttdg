# Procedure: sp_TAMS_RGS_Cancel_20221107

### Purpose
This stored procedure cancels a Request for Goods (RGS) by updating the status of related records and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the RGS to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for cancellation. |
| @UserID		| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing the message sent via SMS. |

### Logic Flow
1. Check if a transaction is already in progress and set an internal flag accordingly.
2. Initialize variables for storing messages and IDs.
3. Update the status of related records (TAMS_TOA) to reflect cancellation.
4. Retrieve user IDs from TAMS_User table based on the provided user ID.
5. Determine the line type ('DTL' or 'NEL') and retrieve endorser IDs accordingly.
6. Iterate through a cursor of TOAStatus values, checking if any are not in the expected range (0 or 6). If so, set @lv_IsAllAckSurrender to 0.
7. Based on the line type, perform different actions:
	* For 'DTL', update OCC_Auth records and insert workflow entries for each related record.
	* For 'NEL', update OCC_Auth records and insert workflow entries for each related record.
8. Construct an SMS message based on the TOANo value.
9. Send the SMS notification using sp_api_send_sms stored procedure.
10. If any errors occur, rollback the transaction and return an error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA