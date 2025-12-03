# Procedure: sp_TAMS_RGS_AckReg_20221107

### Purpose
This stored procedure acknowledges a registration and sends an SMS notification to the registered user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Target Area Record) being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user who is sending the acknowledgement. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag to indicate that a new transaction has begun.
2. It then updates the TOAStatus in the TAMS_TOA table to 2 (Acknowledged) and sets the AckRegisterTime and UpdatedOn fields to the current date and time, along with the ID of the user who made the update.
3. The procedure then retrieves additional information from the TAMS_TAR table based on the TARID provided, including the TARNo, Line, AckRegTime, and MobileNo (HPNo).
4. Depending on the value of the Line field, it constructs an SMS message that includes the TARNo, AckRegTime, and current date.
5. If the HPNo is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
6. If there are any errors during this process, it sets a message indicating the error and exits the procedure.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR
* **Writes:** TAMS_TOA