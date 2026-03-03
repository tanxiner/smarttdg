# Procedure: sp_TAMS_RGS_AckSMS

### Purpose
This stored procedure sends an SMS acknowledgement to a TAMS user, depending on their access type and the status of their protection limit.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the user to send the SMS to. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID of the user to send the SMS to. |
| @SMSType | NVARCHAR(5) | The type of SMS message to send (e.g., '2' for acknowledgement). |
| @Message | NVARCHAR(500) | The output parameter that stores the success or error message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal transaction flag accordingly.
2. It retrieves the TAR ID, line number, access type, TOA number, and HP number from the TAMS_TAR and TAMS_TOA tables based on the provided TAR ID.
3. If the access type is 'Possession', it updates the AckGrantTOATime and ReqProtectionLimitTime fields in the TAMS_TOA table if the SMSType is '2'. Otherwise, it updates the AckProtectionLimitTime field.
4. It sets an SMS message based on the TOA number and sends an SMS using the sp_api_send_sms stored procedure.
5. If any errors occur during the process, it sets an error message in the @Message output parameter.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA