# Procedure: sp_TAMS_RGS_GrantTOA_001

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, updating the TOA status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID used in the SMS notification link. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be returned by the procedure, which will contain an error message if any errors occur during execution. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It then retrieves the TAR No, Line, Operation Date, Access Type, and Mobile No for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. The procedure generates a reference number (Ref Num) using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status in the TAMS_TOA table to 3, sets the new Ref Num, Grant TOA Time, Updated On, and Updated By fields.
5. An audit record is inserted into the TAMS_TOA_Audit table for the updated TAR ID.
6. The procedure then constructs an SMS message based on the Access Type (Possession or Non-Possession).
7. If the user has a Mobile No, it sends an SMS notification using the sp_api_send_sms stored procedure.
8. Finally, if any errors occur during execution, the procedure rolls back the transaction and returns an error message; otherwise, it commits the transaction and returns the output message.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA