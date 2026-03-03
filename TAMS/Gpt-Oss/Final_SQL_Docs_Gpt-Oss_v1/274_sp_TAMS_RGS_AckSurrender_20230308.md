# Procedure: sp_TAMS_RGS_AckSurrender_20230308

### Purpose
Acknowledges a surrender request for a TAR record, updates related status tables, logs the action, updates OCC authorization records, and sends SMS notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to acknowledge. |
| @UserID | NVARCHAR(500) | Login identifier of the user performing the acknowledgment. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Initialize Variables** – Clear the output message, set a newline character, and resolve the numeric user ID from the login ID.  
3. **Update TOA Record** – Set the TOA status to 5 (acknowledged), record the acknowledgment time, and update audit fields.  
4. **Audit Logging** – Insert a copy of the updated TOA row into the audit table with the user and timestamp.  
5. **Gather Context** – Retrieve TAR number, TOA number, line type, acknowledgment time, access and operation dates, and the mobile number for SMS.  
6. **Determine Endorsers** – Based on the line (DTL or NEL), look up the appropriate endorser IDs from the Endorser and Workflow tables.  
7. **Check All TOAs Acknowledged** – Scan all TOA rows for the same access date and line; if any status is not 5, flag that not all are acknowledged.  
8. **If All Acknowledged** –  
   - **DTL Line**  
     - Update OCC_Auth rows with status 10 to 11 (power‑on pending) and insert a workflow record with Endorser1.  
     - For buffer zone rows (status 7, IsBuffer=1), update status to 13 and insert a workflow record with Endorser2.  
   - **NEL Line**  
     - Update OCC_Auth rows with status 8 to 9 (power‑on pending) and insert a workflow record with Endorser1.  
9. **Compose SMS Message** – Build a message string that includes the TOA number, acknowledgment time, and date, prefixed with the appropriate line label.  
10. **Send SMS** – If a mobile number and message exist, call the SMS API to send the notification.  
11. **Trigger SMTP Alert** – Call the SMTP helper procedure; if it returns an error message, set the output message to “Error SMS Sending” and jump to error handling.  
12. **Error Check** – If any error flag is set, set the output message to “Error RGS Ack Surrender” and jump to error handling.  
13. **Commit or Rollback** – If the procedure started the transaction, commit on success; otherwise rollback on error.  
14. **Return** – Return the output message to the caller.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TOA, TAMS_TAR, TAMS_Endorser, TAMS_Workflow, TAMS_OCC_Auth  
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow