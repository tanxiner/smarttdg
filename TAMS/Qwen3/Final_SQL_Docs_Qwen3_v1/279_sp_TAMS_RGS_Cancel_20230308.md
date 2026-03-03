# Procedure: sp_TAMS_RGS_Cancel_20230308

### Purpose
This stored procedure cancels a Request for Goods Service (RGS) on TAMS due to inactivity.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Task Assignment Record) to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing the message sent via SMS. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Initialize variables for internal transactions and log messages.
3. Update the TOAStatus to 6 (Cancelled) and CancelRemark with @CancelRemarks in TAMS_TOA table where TARId matches @TARID.
4. Insert an audit record into TAMS_TOA_Audit table for the updated TOA record.
5. Retrieve the ID of the user from TAMS_User table based on @UserID.
6. Initialize variables for SMS message and cursor to iterate through OCC Auth records.
7. Check if all acknowledgement surrenders are acknowledged (TOAStatus = 5). If not, set @lv_IsAllAckSurrender to 0.
8. Iterate through OCC Auth records where TARId matches @TARID and Line is 'DTL' or 'NEL'. For each record:
	* Update the OCCAuthStatusId in TAMS_OCC_Auth table to a pending status (11, 13, or 9) based on the Level of the workflow.
	* Insert an audit record into [dbo].[TAMS_OCC_Auth_Workflow] table for the updated OCC Auth record.
9. If @Line is 'DTL', construct the SMS message with TOANo and send it via sp_api_send_sms procedure. Otherwise, construct the SMS message with TARNo and send it via SP_Call_SMTP_Send_SMSAlert procedure.
10. Check if any errors occurred during SMS sending or RGS cancellation. If so, return an error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_User, TAMS_OCC_Auth, [dbo].[TAMS_OCC_Auth_Workflow], TAMS_Action_Log, TAMS_TAR
* Writes: TAMS_TOA (TOAStatus and CancelRemark), TAMS_OCC_Auth (OCCAuthStatusId), [dbo].[TAMS_OCC_Auth_Workflow]