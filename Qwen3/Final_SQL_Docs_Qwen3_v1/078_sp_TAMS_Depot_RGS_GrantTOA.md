# Procedure: sp_TAMS_Depot_RGS_GrantTOA

### Purpose
This stored procedure grants a Temporary Authorization (TOA) to a Road Geographical Section (RGS) for a specific TAR ID, based on the provided parameters and business rules.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the action. |
| @toacallbacktiming | datetime | The callback timing for the TOA grant. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It then retrieves the TAR ID, Line, Operation Date, Access Type, Mobile No, and TOA Status from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID.
3. If the TOA status is 2 (Pending), it generates a reference number for the TOA grant using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status to 3 (Granted) in the TAMS_TOA table, sets the TOANo, GrantTOATime, and UpdatedOn fields accordingly.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR ID.
6. Based on the Access Type, it constructs a message to be sent via SMS to the user's mobile number.
7. If the @HPNo field is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
8. If any errors occur during the process, it sets an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA