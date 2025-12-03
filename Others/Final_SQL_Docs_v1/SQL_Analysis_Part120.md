# Procedure: sp_TAMS_RGS_Cancel_20230308
**Type:** Stored Procedure

### Purpose
This stored procedure cancels a Request for Goods Service (RGS) and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the RGS to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user who initiated the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter that contains the SMS message to be sent. |

### Logic Flow
1. Checks if a transaction is already active.
2. If not, sets an internal flag and begins a new transaction.
3. Updates the RGS status to cancelled and inserts an audit record.
4. Retrieves the user's ID from the TAMS_User table.
5. Iterates through the OCC_Auth table to update the status of each authentication record.
6. For each authentication record, updates the status in the TAMS_OCC_Auth table and inserts a new workflow record.
7. If the RGS was cancelled due to TPO/PC inactivity, sends an SMS notification to the user.
8. If the RGS was cancelled due to NEL OCC, sends an SMS notification to the user.
9. If any errors occur during the process, rolls back the transaction and returns an error message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_Action_Log, TAMS_Action_Log_Workflow
* **Writes:** TAMS_TAR, TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_Action_Log