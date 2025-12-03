# Procedure: sp_TAMS_RGS_Cancel_20230209_AllCancel
**Type:** Stored Procedure

The purpose of this stored procedure is to cancel a Request for Goods Service (RGS) and send an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the RGS to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | The remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user who initiated the cancellation. |
| @Message	| NVARCHAR(500) | The output message that will be sent to the user. |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets a flag and begins a new transaction.
3. Updates the status of the RGS to cancelled and inserts an audit record.
4. Retrieves the ID of the user who initiated the cancellation from the TAMS_User table.
5. Iterates through the OCC_Auth table to update the status of each authentication record and insert workflow records for pending and buffer zone operations.
6. If the line is 'DTL', sends an SMS notification to the user with a specific message based on the TOA status.
7. If the line is not 'DTL', sends an SMS notification to the user with a different message.
8. Checks if there are any errors during the procedure and returns an error message if necessary.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_Action_Log, TAMS OCC_Auth_Workflow
* Writes: TAMS_TAR, TAMS_TOA, TAMS_User, TAMS_OCC_Auth