# Procedure: sp_TAMS_RGS_AckSurrender

### Purpose
Acknowledges the surrender of a TAR, updates TOA and OCC authorization records, logs audit entries, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to acknowledge. |
| @UserID | NVARCHAR(500) | Login ID of the user performing the acknowledgment. |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag it as internal.  
2. **Initialization** – Clear @Message, set a newline character, and resolve @UserIDID from TAMS_User using @UserID.  
3. **TOA Status Check** – Retrieve the current TOAStatus for the given @TARID.  
4. **Proceed if Status 4** –  
   1. Update TAMS_TOA to status 5, set AckSurrenderTime, UpdatedOn, and UpdatedBy.  
   2. Insert a corresponding audit record into TAMS_TOA_Audit.  
   3. Gather TAR and TOA details (TARNo, TOANo, Line, AckSurrenderTime, AccessDate, OperationDate, HPNo).  
   4. Determine Endorser1 and Endorser2 IDs based on the Line (DTL or NEL).  
   5. **Check All Acknowledged** – Scan all TOA records for the same AccessDate and Line; if any status is not 5, flag that not all are acknowledged.  
   6. **DTL Path (All Acknowledged)** –  
      - Update OCC_Auth records with PowerOn = 0 to status 11, audit, and insert a pending workflow with Endorser1.  
      - Update OCC_Auth records with IsBuffer = 1 to status 13, audit, and insert a pending workflow with Endorser2.  
   7. **NEL Path** –  
      - Update OCC_Auth records with status 8 to status 9, audit, and insert a pending workflow with Endorser1.  
      - For each distinct TractionPowerId linked to the TAR’s power sectors, if no TOA exists with a non‑terminal status for that sector, insert a pending workflow for OCC_Auth status 8, audit, and update the OCC_Auth status to 9 with audit.  
   8. **SMS Preparation** – Build a message string that includes the TOANo, current time, and date, prefixed with “DTL OCC” or “NEL OCC” based on the Line.  
   9. **SMS Sending** – If a mobile number and message exist, call sp_api_send_sms to transmit the notification.  
5. **Error Handling** – If any error occurs, set @Message accordingly, rollback the transaction if it was internal, and exit.  
6. **Commit** – If the internal transaction flag is set, commit the transaction.  
7. **Return** – Return the @Message value.

### Data Interactions
* **Reads**  
  - TAMS_User  
  - TAMS_TAR  
  - TAMS_TOA  
  - TAMS_Endorser  
  - TAMS_Workflow  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Auth_Workflow  
  - TAMS_Traction_Power_Detail  
  - TAMS_TAR_Power_Sector  

* **Writes**  
  - TAMS_TOA (UPDATE)  
  - TAMS_TOA_Audit (INSERT)  
  - TAMS_OCC_Auth (UPDATE)  
  - TAMS_OCC_Auth_Audit (INSERT)  
  - TAMS_OCC_Auth_Workflow (INSERT)  
  - TAMS_OCC_Auth_Workflow_Audit (INSERT)  

---