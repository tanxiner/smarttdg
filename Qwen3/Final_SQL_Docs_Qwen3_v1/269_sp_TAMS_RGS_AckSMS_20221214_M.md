# Procedure: sp_TAMS_RGS_AckSMS_20221214_M

### Purpose
This stored procedure performs a series of actions to acknowledge SMS messages for a specific TAR (Transportation Asset Record) and update the corresponding records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the TAR being processed. |
| @EncTARID	| NVARCHAR(250) | The encrypted TAR ID. |
| @SMSType	| NVARCHAR(5) | The type of SMS message (e.g., 2 for acknowledgement). |
| @Message	| NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID values.
3. Depending on the access type (Possession or not), it updates the corresponding records in the TAMS_TOA table with the current date and time.
4. If the SMS message is not empty, it sends an SMS notification to the mobile number associated with the TAR using the sp_api_send_sms stored procedure.
5. After sending the SMS, it checks if any errors occurred during this process. If so, it sets a failure message and exits the transaction.
6. If no errors occurred, it commits the transaction and returns the output message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA tables
* **Writes:** TAMS_TOA table (for updates)