# Procedure: sp_TAMS_RGS_GrantTOA_20230801

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, updating the TOA status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID used in the SMS notification link. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output parameter that stores any error message if an issue occurs during the procedure execution. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It retrieves the TAR No, Line, Operation Date, Access Type, and Mobile No for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. It generates a reference number (Ref Num) using the sp_Generate_Ref_Num_TOA stored procedure.
4. The procedure updates the TOA status in the TAMS_TOA table with the new Ref Num, Grant TOA time, updated on date, and updated by user.
5. An audit record is inserted into the TAMS_TOA_Audit table for the updated TAR ID.
6. It sets the current date and time.
7. Depending on the access type ('Possession' or not), it constructs an SMS message with a link to acknowledge the TOA.
8. If the user has a Mobile No, it sends an SMS notification using the sp_api_send_sms stored procedure.
9. If any errors occur during the procedure execution, it sets an error message in the @Message output parameter and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA