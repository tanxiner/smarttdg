# Procedure: sp_TAMS_RGS_AckReg_20230807_M

### Purpose
This stored procedure acknowledges a registration request for a TAMS (Tracking and Management System) user, updating the status of their TOA (Temporary Authorization) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | TAR ID of the user requesting registration |
| @UserID		| NVARCHAR(500) | User ID of the person acknowledging the registration request |
| @Message	| NVARCHAR(500) | Output message to be returned |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag (@IntrnlTrans) accordingly.
2. It retrieves the current TOA status for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. If the TOA status is 1 (pending), it updates the TOA status to 2 (approved) in the TAMS_TOA table, setting the AckRegisterTime and UpdatedOn fields to the current date and time, and updating the UpdatedBy field with the user ID provided.
4. It retrieves additional information about the TAR record from the TAMS_TAR table, including the TAR No, Line, AckRegTime, and MobileNo (HPNo).
5. Based on the value of the Line field, it constructs a message to be sent via SMS to the user's mobile number using the sp_api_send_sms stored procedure.
6. If an error occurs during SMS sending, it sets the @Message parameter to 'Error SMS Sending' and jumps to the TRAP_ERROR label.
7. If the TOA status is 2 (already approved), it sets the @Message parameter to '1' (indicating success) and jumps to the TRAP_ERROR label.
8. If any other error occurs, it sets the @Message parameter to 'Invalid TAR status. Please refresh RGS.' and jumps to the TRAP_ERROR label.
9. Finally, if no errors occurred, it commits the transaction and returns the constructed message.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA