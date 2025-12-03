# Procedure: sp_TAMS_RGS_GrantTOA_20230801_M

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, based on the provided user ID and message.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The message to be sent to the user after the TOA is granted. |

### Logic Flow
1. The procedure checks if a transaction has already started. If not, it starts one.
2. It retrieves the TAR and TOA status for the provided TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. If the TOA status is 2 (Pending), it generates a reference number using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status to 3 (Granted) in the TAMS_TOA table with the new reference number, grant time, and updated by fields.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR ID.
6. Depending on the access type ('Possession' or not), it sets a message to be sent to the user via SMS using the sp_api_send_sms stored procedure.
7. If the SMS sending process fails, it sets an error message and skips to the TRAP_ERROR label.
8. If the TOA status is 3 (Granted) after checking again, it sets a success message and exits the procedure.
9. If any errors occur during the procedure, it rolls back the transaction if one was started.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA