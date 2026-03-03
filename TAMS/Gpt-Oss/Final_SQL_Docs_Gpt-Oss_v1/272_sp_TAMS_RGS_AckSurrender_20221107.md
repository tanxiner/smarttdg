# Procedure: sp_TAMS_RGS_AckSurrender_20221107

### Purpose
Acknowledges a surrender for a specified TAR, updates related TOA and OCC authorization records, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to acknowledge (default 0). |
| @UserID | NVARCHAR(500) | Login ID of the user performing the acknowledgment. |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark it as internal.  
2. **Initialize Variables** – Clear the output message and set up control variables.  
3. **Resolve User ID** – Look up the numeric UserIDID from TAMS_User using the supplied @UserID.  
4. **Update TOA Status** – Set TOAStatus to 5, record the acknowledgment time, and update audit fields for the TOA row matching @TARID.  
5. **Gather TAR Context** – Retrieve TARNo, TOANo, Line, AckSurrenderTime, AccessDate, OperationDate, and the mobile number (HPNo) from TAMS_TAR and TAMS_TOA for the given TAR.  
6. **Determine Endorsers** – Based on the Line value (DTL or NEL), fetch Endorser1 and Endorser2 IDs from TAMS_Endorser joined with TAMS_Workflow, selecting the appropriate workflow level.  
7. **Check All TOAs Acknowledged** – Scan all TOA rows for the same AccessDate and Line; if any status is not 5, flag that not all are acknowledged.  
8. **If All Acknowledged** –  
   - **DTL Path**  
     - For each OCC_Auth record with status 10 and PowerOn = 0, update status to 11 and log a workflow entry with Endorser1.  
     - For each OCC_Auth record with status 7, update status to 13 and log a workflow entry with Endorser2.  
   - **NEL Path**  
     - For each OCC_Auth record with status 7 and PowerOn = 0, update status to 9 and log a workflow entry with Endorser1.  
9. **Compose SMS** – Build a message string that includes the TOANo, the acknowledging line (DTL or NEL), current time, and date.  
10. **Send SMS** – If a mobile number and message exist, call sp_api_send_sms to transmit the notification.  
11. **Error Handling** – If any error occurs during the process, set @Message to an error string and roll back the transaction if it was internally started.  
12. **Commit & Return** – Commit the transaction if it was internally started and return the @Message output.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TOA, TAMS_TAR, TAMS_Endorser, TAMS_Workflow, TAMS_OCC_Auth  
* **Writes:** TAMS_TOA (UPDATE), TAMS_OCC_Auth (UPDATE), TAMS_OCC_Auth_Workflow (INSERT)