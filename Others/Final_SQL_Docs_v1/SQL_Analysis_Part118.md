# Procedure: sp_TAMS_RGS_Cancel_20221107
**Type:** Stored Procedure

The purpose of this stored procedure is to cancel a TAMS RGS (Request for Goods and Services) by updating its status, inserting audit logs, and sending SMS notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAMS RGS to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing a message after the procedure is executed. |

### Logic Flow
1. Checks if a transaction has been started.
2. Updates the TAMS_TOA table with the new status, cancel remarks, and updated by fields for the specified TAMS RGS ID.
3. Retrieves the user ID from the TAMS_User table based on the provided user ID.
4. Iterates through the TAMS_OCC_Auth table to find OCCAuth records that match the current date and time, and updates their status and inserts audit logs accordingly.
5. Sends SMS notifications based on the line type (DTL or NEL) and the TOANo value.
6. If a transaction has been started, commits it; otherwise, rolls back.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_TOA, TAMS_Action_Log