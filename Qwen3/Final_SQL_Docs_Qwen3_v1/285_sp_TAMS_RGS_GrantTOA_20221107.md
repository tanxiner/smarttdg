# Procedure: sp_TAMS_RGS_GrantTOA_20221107

### Purpose
This stored procedure grants a TOA (Temporary Access Authorization) to a user for a specific TAR (Track and Record) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error messages. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal transaction flag and begins a new transaction.
2. It then retrieves the TAR ID, Line, Operation Date, Access Type, and HP No from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID.
3. The procedure generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status in the TAMS_TOA table to 3, sets the TOANo to the generated reference number, and sets the GrantTOATime and UpdatedOn fields to the current date and time.
5. Depending on the Access Type, it constructs an SMS message with a link to acknowledge the TOA.
6. If the HP No is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during the process, it sets the @Message output parameter to an error message and either commits or rolls back the transaction depending on whether an internal transaction was started.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA