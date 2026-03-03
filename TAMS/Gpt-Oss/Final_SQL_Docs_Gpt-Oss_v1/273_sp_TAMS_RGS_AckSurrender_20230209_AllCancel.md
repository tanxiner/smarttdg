# Procedure: sp_TAMS_RGS_AckSurrender_20230209_AllCancel

### Purpose
Acknowledges the surrender of a TOA for a specified TARID, updates related status records, logs the change, updates OCC authorization states, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR whose TOA is being acknowledged. |
| @UserID | NVARCHAR(500) | Login identifier of the user performing the acknowledgment. |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error details. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag it as internal.  
2. **Initialization** – Clear the output message and set a newline character for later use.  
3. **User Identification** – Retrieve the internal `Userid` for the supplied `@UserID` from `TAMS_User`.  
4. **TOA Status Update** – Set `TOAStatus` to 5 (acknowledged), record the acknowledgment time, and update audit fields for the TOA linked to `@TARID`.  
5. **Audit Logging** – Insert a copy of the updated TOA row into `TAMS_TOA_Audit`.  
6. **Variable Preparation** – Declare and initialize variables for SMS content, status checks, and date/time formatting.  
7. **Data Retrieval** – Pull TAR number, TOA number, line type, acknowledgment time, access and operation dates, and mobile number from `TAMS_TAR` and `TAMS_TOA`.  
8. **Endorser Selection** –  
   * If line is `DTL`, fetch endorser IDs for levels 10 and 12 from `TAMS_Endorser`/`TAMS_Workflow`.  
   * If line is `NEL`, fetch the endorser ID for level 8.  
9. **TOA Status Verification** – Use a cursor to scan all TOAs sharing the same access date and line. If any status is not 5, flag that not all TOAs are acknowledged.  
10. **OCC Authorization Updates (if all TOAs acknowledged)** –  
    * **DTL Line**  
      - Update all `TAMS_OCC_Auth` records with `PowerOn = 0` to status 11 and log a workflow entry with `Endorser1`.  
      - Update all buffer zone records (`IsBuffer = 1`) to status 13 and log a workflow entry with `Endorser2`.  
    * **NEL Line**  
      - Update all `TAMS_OCC_Auth` records with `PowerOn = 0` to status 9 and log a workflow entry with `Endorser1`.  
11. **SMS Message Construction** – Build a message that includes the TOA number, line type, current time, and date.  
12. **SMS Dispatch** –  
    * If a mobile number and message exist, call `sp_api_send_sms`.  
    * Trigger a quick SMS alert via `SP_Call_SMTP_Send_SMSAlert`; if it returns an error message, set the output message to “Error SMS Sending” and jump to error handling.  
13. **Error Checking** – If any SQL error occurred, set the output message to “Error RGS Ack Surrender” and jump to error handling.  
14. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it untouched. Return the output message.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_TOA`  
  - `TAMS_TAR`  
  - `TAMS_Endorser`  
  - `TAMS_Workflow`  
  - `TAMS_OCC_Auth`  

* **Writes:**  
  - `TAMS_TOA` (status and timestamps)  
  - `TAMS_TOA_Audit` (audit record)  
  - `TAMS_OCC_Auth` (status updates for power‑on and buffer zones)  
  - `TAMS_OCC_Auth_Workflow` (workflow entries for each status change)  

---