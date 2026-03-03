# Procedure: sp_TAMS_RGS_AckReg_20230807

### Purpose
Acknowledges a TAR registration, updates its status, and sends an SMS notification to the associated mobile number.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR to acknowledge. |
| @UserID   | NVARCHAR(500) | User performing the acknowledgment. |
| @Message  | NVARCHAR(500) | Output message indicating success or error. |

### Logic Flow
1. Initialise an internal transaction flag and begin a transaction if none is active.  
2. Clear the output message.  
3. Update the TAMS_TOA record for the supplied @TARID: set TOAStatus to 2, record the acknowledgment time, and log the updater.  
4. Retrieve the TAR number, line code, acknowledgment time, and mobile number from TAMS_TAR and TAMS_TOA.  
5. Build a human‑readable SMS message that includes the TAR number, the line (DTL or NEL), the acknowledgment time, and the current date, with a standard footer.  
6. If a mobile number and message exist, call sp_api_send_sms to transmit the SMS.  
7. Trigger an additional SMTP SMS alert via SP_Call_SMTP_Send_SMSAlert; if it returns a non‑empty message, set @Message to “Error SMS Sending” and jump to error handling.  
8. If any error occurs during the process, set @Message to “Error RGS Ack Reg” and jump to error handling.  
9. On successful completion, commit the transaction (if it was started internally) and return the (empty) @Message.  
10. In the error path, roll back the transaction (if it was started internally) and return the @Message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR  
* **Writes:** TAMS_TOA (status update)  

---