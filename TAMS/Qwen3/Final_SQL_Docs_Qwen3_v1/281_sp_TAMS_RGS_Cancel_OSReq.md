# Procedure: sp_TAMS_RGS_Cancel_OSReq

### Purpose
This stored procedure cancels an Order Status Request (OSR) and updates the corresponding records in the TAMS database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR record to be canceled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for canceling the OSR. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing a message after execution. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Initialize variables for storing internal transactions and SMS messages.
3. Update the TOAStatus to 6 (Canceled) and CancelRemark in TAMS_TOA table where TARId matches @TARID.
4. Determine the line type ('DTL' or 'NEL') based on the TAR record's Line field.
5. If the line is 'DTL', perform the following steps:
	* Retrieve OCC Auth IDs with a specific status and update their status to 11 (Pending) and add an entry in TAMS_OCC_Auth_Workflow table.
	* Update the status of other OCC Auth IDs to 12 (Terminated) and add entries in TAMS_OCC_Auth_Workflow table.
6. If the line is 'NEL', perform the following steps:
	* Retrieve OCC Auth IDs with a specific status and update their status to 8 (Pending) and add an entry in TAMS_OCC_Auth_Workflow table.
7. Construct an SMS message based on the line type and TAR record details.
8. Send the SMS message using the @Message output parameter.
9. If any errors occur during execution, roll back the transaction and return an error message.
10. Commit the transaction if no errors occurred.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA