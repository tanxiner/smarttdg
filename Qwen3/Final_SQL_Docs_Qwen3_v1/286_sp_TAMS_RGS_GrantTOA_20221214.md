# Procedure: sp_TAMS_RGS_GrantTOA_20221214

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a TAR (Track and Record) for a specific user, updating the TAR's status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to grant TOA to. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The ID of the user granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message for the procedure, which will be populated with an error message if an error occurs. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It retrieves the TAR's details from the TAMS_TAR table based on the provided @TARID and @EncTARID.
3. It generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. The procedure updates the TAR's status to 3 (granted) in the TAMS_TOA table, sets the TOANo field to the generated reference number, and records the grant time and updated by fields.
5. It inserts a new record into the TAMS_TOA_Audit table for the granted TAR.
6. Depending on the access type ('Possession' or not), it constructs an SMS message with a link to acknowledge the TOA.
7. If @HPNo is not empty, it sends an SMS notification using the sp_api_send_sms stored procedure.
8. It checks if any errors occurred during the execution of the procedure and returns an error message if so.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA