# Procedure: sp_TAMS_RGS_AckSMS_M

### Purpose
This stored procedure performs an acknowledgement of a SMS message for a specific TAMS (Transportation Asset Management System) record, updating the corresponding TAMS_TOA record with the latest information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the TAMS record to be acknowledged. |
| @EncTARID	| NVARCHAR(250) | The encrypted ID of the TAMS record to be acknowledged. |
| @SMSType	| NVARCHAR(5) | The type of SMS message being sent. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | The output parameter that stores the acknowledgement message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It then retrieves the necessary information from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID values.
3. Depending on the access type of the TAMS record, it determines whether to send an SMS message with a specific acknowledgement code (e.g., '2' for possession) or not.
4. If an SMS message is determined to be sent, it constructs the message by concatenating the TOANo and additional information.
5. The procedure then inserts a new audit record into the TAMS_TOA_Audit table to track changes made to the TAMS_TOA record.
6. It sends the constructed SMS message using the sp_api_send_sms stored procedure, which returns an error code.
7. If an error occurs during SMS sending, it sets the @Message output parameter to 'Error SMS Sending' and commits or rolls back the transaction accordingly.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA_Audit