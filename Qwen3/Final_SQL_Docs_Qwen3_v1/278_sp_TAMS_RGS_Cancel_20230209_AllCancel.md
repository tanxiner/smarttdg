# Procedure: sp_TAMS_RGS_Cancel_20230209_AllCancel

### Purpose
This stored procedure cancels all RGS (Remote Gateway Server) operations for a given TARID (TAR ID), updates the TOA status, and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID to cancel all RGS operations for. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter to store the SMS message. |

### Logic Flow
1. Check if a transaction is already in progress and set an internal flag accordingly.
2. Initialize variables for storing the TOA status, Cancel Remarks, and User ID.
3. Update the TOA status, Cancel Remarks, and Updated By fields for all RGS operations with the given TARID.
4. Insert an audit record into TAMS_TOA_Audit for each updated TOA record.
5. Retrieve the user ID from TAMS_User based on the provided User ID.
6. Initialize variables for storing SMS message components (e.g., TARNo, TOANo, Line).
7. Query TAMS_TAR and TAMS_TOA to retrieve relevant data for the given TARID and current date/time.
8. Iterate through all RGS operations with a status not equal to 5 (i.e., not already cancelled) and update their status to 6 (cancelled).
9. For each RGS operation, check if it's the last one in the sequence and perform additional actions:
	* If it's a DTL (Detailed) line, update OCCAuthStatusId and insert an audit record.
	* If it's an NEL (Notification) line, update OCCAuthStatusId and insert an audit record.
10. Construct the SMS message based on the TARNo, TOANo, and Line values.
11. Send the SMS notification using sp_api_send_sms.
12. Check for any errors during the process and return a corresponding error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_User, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_Action_Log, TAMS_Action_Log
* Writes: TAMS_TOA (updated status), TAMS OCC_Auth (updated status and audit record), TAMS OCC_Auth_Workflow (audit record)