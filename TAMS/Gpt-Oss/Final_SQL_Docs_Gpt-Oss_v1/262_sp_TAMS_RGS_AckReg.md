# Procedure: sp_TAMS_RGS_AckReg

### Purpose
Acknowledges a TAR registration, updates its status, creates depot‑auth records when required, and sends an SMS notification to the associated mobile number.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR record to acknowledge. |
| @UserID   | NVARCHAR(500) | User performing the acknowledgment. |
| @Message  | NVARCHAR(500) | Output parameter that returns a status or error message. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Reset Output** – Clear @Message.  
3. **Retrieve Status** – Load the current TOAStatus and TrackType for the specified @TARID.  
4. **Process Pending TOA (TOAStatus = 1)**  
   1. Update the TAMS_TOA record to status 2, set AckRegisterTime, UpdatedOn, and UpdatedBy.  
   2. **Depot‑specific handling** – If TrackType is DEPOT:  
      - Verify no existing depot‑auth record for this TARID; if one exists, exit.  
      - Insert a new TAMS_Depot_Auth row with line, track type, operation date, access date, status 1, creation timestamp, creator, and TARID.  
      - Retrieve the workflow ID for a pending DTCAuth workflow.  
      - Insert a corresponding TAMS_Depot_Auth_Workflow row linking the new auth ID to the workflow.  
      - For each SPKS zone linked to the TAR, insert a TAMS_Depot_DTCAuth_SPKS row unless a duplicate already exists.  
      - For each power sector linked to the TAR (excluding sectors 48‑50), insert a TAMS_Depot_Auth_Powerzone row unless a duplicate already exists.  
   3. **SMS Preparation** – Build a message that includes the TAR number, acknowledgment time, current date, and the instruction “DO NOT GO DOWN TO TRACK YET.” The wording differs for DTL lines versus other track types.  
   4. **SMS Sending** – If a mobile number and message are present, call sp_api_send_sms to transmit the SMS.  
5. **Handle Already Granted TOA (TOAStatus = 2)** – Set @Message to “1” and jump to error handling.  
6. **Handle Invalid Status** – Set @Message to “Invalid TAR status. Please refresh RGS.” and jump to error handling.  
7. **Error Check** – If any SQL error occurred, set @Message to “Error RGS Ack Reg” and jump to error handling.  
8. **Commit or Rollback** – If the procedure started the transaction, commit on success; otherwise rollback on error.  
9. **Return** – Return the @Message value.

### Data Interactions
* **Reads** – TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus, TAMS_TAR_SPKSZone, TAMS_TAR_Power_Sector, TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone.  
* **Writes** – TAMS_TOA, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone.