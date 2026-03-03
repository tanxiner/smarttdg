# Procedure: sp_TAMS_RGS_GrantTOA

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a RGS (Railway Grade Signal) for a specific TAR (Track Access Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR being granted TOA. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It then retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID.
3. If the TOA status is 2 (Pending), it generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. It then updates the TOA status to 3 (Granted) in the TAMS_TOA table, sets the new TOANo and GrantTOATime fields, and inserts an audit record into the TAMS_TOA_Audit table.
5. Depending on the access type ('Possession' or not), it constructs a message for sending an SMS to the user with the reference number.
6. It then sends the SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during this process, it sets the @Message output parameter to an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA