# Procedure: sp_TAMS_Depot_RGS_AckSurrender

### Purpose
Acknowledges the surrender of a TAR by RGS, updates the TOA status, logs the change, optionally triggers NEL‑specific workflow updates, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to process (default 0). |
| @UserID | NVARCHAR(500) | Login ID of the user performing the operation. |
| @Message | NVARCHAR(500) OUTPUT | Result message or error code returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag it for later commit/rollback.  
2. **Initialize** – Clear @Message and resolve the numeric user ID from TAMS_User.  
3. **Status Check** – Retrieve the current TOAStatus for the specified TAR.  
4. **Acknowledgement Path (TOAStatus = 4)**  
   1. Update TAMS_TOA: set status to 5, record surrender time, and audit fields.  
   2. Insert a copy of the updated TOA row into TAMS_TOA_Audit with action metadata.  
   3. Gather TAR and TOA details (numbers, line, dates, mobile number).  
   4. Verify that all TOA records for the same AccessDate and Line are already acknowledged; if any are not, flag that not all are acknowledged.  
   5. **NEL‑specific workflow** – If the line is NEL and a matching TOA record exists:  
      - Confirm the depot authentication status is 8; otherwise set an error message and exit.  
      - Determine the next workflow status from TAMS_WFStatus.  
      - Mark the current workflow record as Completed, insert a new workflow record, and update the depot authentication status.  
   6. Compose an SMS message for NEL lines.  
   7. If a mobile number and message exist, call sp_api_send_sms to deliver the notification.  
5. **Non‑Acknowledgement Path** – If the TOA status is not 4:  
   - If it is already 5, set @Message to '1' (already granted).  
   - Otherwise, set @Message to indicate an invalid TAR status.  
6. **Error Handling** – If any error occurs, set @Message to a generic error string.  
7. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise rollback on error.  
8. **Return** – Return the @Message value to the caller.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow.  
* **Writes:** TAMS_TOA (UPDATE), TAMS_TOA_Audit (INSERT), TAMS_Depot_Auth_Workflow (UPDATE/INSERT), TAMS_Depot_Auth (UPDATE).