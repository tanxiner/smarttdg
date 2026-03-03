# Procedure: sp_TAMS_RGS_AckReg_20230807

### Purpose
This stored procedure acknowledges a registration and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | TAR ID of the registration to be acknowledged |
| @UserID	| NVARCHAR(500) | User ID who is sending the acknowledgement |

### Logic Flow

1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It then updates the TOAStatus of the TAMS_TOA table to 2 (acknowledged) for the specified TAR ID.
3. Next, it retrieves additional information about the registration from the TAMS_TAR table, including the TAR No, Line, Ack Register Time, and Mobile No.
4. Based on the Line value, it constructs an SMS message with a specific format.
5. If the Mobile No is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
6. After sending the SMS, it checks for any errors that may have occurred during this process.
7. If no errors were found, it commits the transaction and returns a success message. Otherwise, it rolls back the transaction and returns an error message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR
* **Writes:** TAMS_TOA