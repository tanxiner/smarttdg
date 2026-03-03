# Procedure: sp_TAMS_RGS_Cancel_20250403

### Purpose
Cancels a RGS (Railway Goods Service) transaction, updates related status records, logs the action, adjusts OCC authorisation states, and sends a cancellation notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to cancel |
| @CancelRemarks | NVARCHAR(1000) | Text describing the reason for cancellation |
| @UserID | NVARCHAR(500) | User performing the cancellation |
| @tracktype | NVARCHAR(50) | Type of track; defaults to MAINLINE |
| @Message | NVARCHAR(500) OUTPUT | Result status or error code |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark that the procedure owns the transaction.
2. **Reset Message** – Initialise the output message to an empty string.
3. **Update TOA Status** – Set the TOA record for the given TAR to status 6 (cancelled), store remarks, and update audit fields.
4. **Audit TOA** – Insert a copy of the updated TOA row into the TOA audit table with action ‘U’.
5. **Resolve User ID** – Look up the numeric user ID that matches the supplied login ID.
6. **Prepare Variables** – Initialise variables for later use (line, dates, phone, etc.).
7. **If @tracktype = MAINLINE** –  
   a. Retrieve TAR and TOA details (TARNo, TOANo, line, access date, operation date, mobile number).  
   b. Log an action record for the cancellation.  
   c. Determine the appropriate endorser IDs based on the line (DTL or NEL).  
   d. Scan all TOA records for the same access date and line; if any status is not 5, flag that not all acknowledgements are surrendered.  
   e. **If line is DTL and all acknowledgements surrendered** –  
      i. For each OCC authorisation that is still active (PowerOn = 0) on the same line, operation and access dates, set status to 11, audit the change, and create a pending workflow entry for the first endorser.  
      ii. For each OCC authorisation that is in the buffer phase (OCCAuthStatusId = 8) on the same line, operation and access dates, set status to 9, audit the change, and create a pending workflow entry for the first endorser.  
   f. **If line is NEL** –  
      i. For each traction power that belongs to the TAR’s power sectors, check that all TOA records for that sector are cancelled or surrendered.  
      ii. If the sector is clear, insert a pending workflow entry for the first endorser, update the OCC authorisation status to 9, and audit the change.
8. **Else (tracktype ≠ MAINLINE)** –  
   a. Identify the line from the TAR record.  
   b. If the line is NEL, perform depot‑level cancellation logic:  
      i. If the depot authorisation is in the initial certification state, delete all related power‑zone, DTC‑SPKS, workflow, and the authorisation record itself.  
      ii. If the depot authorisation is pending but no train movement has occurred, transition the workflow to the next active status, mark the previous workflow as cancelled, insert a new workflow entry, and update the authorisation status.  
      iii. If the status is unsupported, set @Message to ‘‑2’ and jump to error handling.
9. **Retrieve OCC Contact** – Query the parameters table for the OCC contact number that matches the line.
10. **Compose SMS Message** – Build a cancellation message that includes the TOANo or TARNo, the OCC contact number, and urgency wording based on whether a TOANo exists.
11. **Send SMS** – If a mobile number is present, call the SMS API with the composed message.
12. **Error Check** – If any error flag is set, set @Message to ‘Error RGS Cancel’ and roll back the transaction.
13. **Commit or Rollback** – Commit the transaction if the procedure started it; otherwise roll back on error.
14. **Return** – Return the @Message string on success or –1 on failure.

### Data Interactions

**Tables Read**
- TAMS_TOA
- TAMS_Depot_Auth
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_DTCAuth_SPKS
- TAMS_Depot_Auth_Workflow
- TAMS_Depot_Auth
- TAMS_Depot_Auth_Workflow
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth_Powerzone
- TAMS_Depot_Auth