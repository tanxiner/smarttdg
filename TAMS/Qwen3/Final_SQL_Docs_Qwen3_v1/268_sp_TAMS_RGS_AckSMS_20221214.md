# Procedure: sp_TAMS_RGS_AckSMS_20221214

### Purpose
This stored procedure performs the business task of sending an acknowledgement SMS to a TAR (Transportation Asset Record) after it has been granted or protection limit has been set up.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR being acknowledged. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @SMSType | NVARCHAR(5) | The type of SMS to be sent (e.g., 2 for acknowledgement). |
| @Message | NVARCHAR(500) = NULL OUTPUT | The message to be sent in the SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID.
3. Depending on the access type of the TAR (Possession or not), it updates the corresponding fields in the TAMS_TOA table with the current date and time.
4. If the SMS type is 2, it updates the AckGrantTOATime field and sets up a link to report once protection limit has been set up.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR details.
6. If a message is generated, it sends an SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during the process, it sets an error message and commits or rolls back the transaction accordingly.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA