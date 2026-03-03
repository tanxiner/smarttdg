**Purpose**  
Cancels a Railway Goods Surrender (RGS) for a specified TARID, updates the surrender status, records audit and action logs, manages OCC authorisation workflows for DTL or NEL lines, handles depot‑level cancellations, sends an SMS notification to the train owner, and returns a status message.

---

**Parameters**

| Name          | Type                | Purpose |
|---------------|---------------------|---------|
| @TARID        | BIGINT (default 0)  | Identifier of the TAR record to cancel. |
| @CancelRemarks| NVARCHAR(1000) (default NULL) | Text supplied by the user describing the reason for cancellation. |
| @UserID       | NVARCHAR(500)       | Login ID of the user performing the cancellation. |
| @tracktype    | NVARCHAR(50) (default 'MAINLINE') | Indicates whether the cancellation is for a main‑line or depot operation. |
| @Message      | NVARCHAR(500) OUTPUT | Returns a status string; empty on success, error code on failure. |

---

**Logic Flow**

1. **Transaction Setup** – If no outer transaction exists, start an internal transaction and set @Message to an empty string.  
2. **Update TOA Record** – In `TAMS_TOA`, set `TOAStatus` to 6 (cancelled), store `CancelRemark`, and record the update timestamp and user.  
3. **Audit TOA** – Insert the updated row into `TAMS_TOA_Audit`.  
4. **Resolve User ID** – Look up the numeric user ID (`@IDUserID`) from `TAMS_User` using the supplied `@UserID`.  
5. **Prepare SMS Variables** – Initialise an empty SMS message string.  
6. **Main‑Line Processing** (`@tracktype = 'MAINLINE'`)  
   1. Retrieve `TARNo`, `TOANo`, `Line`, `AccessDate`, `OperationDate`, and the train owner’s phone (`HPNo`) from `TAMS_TAR` and `TAMS_TOA`.  
   2. Log the cancellation action in `TAMS_Action_Log`.  
   3. Determine the appropriate endorser IDs (`@Endorser1`, `@Endorser2`) by joining `TAMS_Endorser` with `TAMS_Workflow`, selecting the endorser for the current `Line` (DTL or NEL).  
   4. Scan all TOA records for the same `AccessDate` and `Line` to verify whether every status is 5 (acknowledged) or 6 (cancelled); set a flag `@lv_IsAllAckSurrender` accordingly.  
   5. **DTL Line** – If all surrender statuses are acknowledged:  
      * Update every `TAMS_OCC_Auth` record with `PowerOn = 0` to status 11, audit the change, and insert a workflow entry using `@Endorser1`.  
      * Update every `TAMS_OCC_Auth` record with `IsBuffer = 1` to status 13, audit the change, and insert a workflow entry using `@Endorser2`.  
   6. **NEL Line** – For each distinct traction power ID linked to the TAR’s power sectors:  
      * If no TOA exists with a status other than 0, 5, or 6 for that sector, insert a pending workflow record for the corresponding `TAMS_OCC_Auth` (status 8 → 9) and audit the update.  
7. **Depot Path** – If `@tracktype` is not 'MAINLINE':  
   1. Retrieve the `Line` value from `TAMS_TAR`.  
   2. If the line is NEL and a depot‑auth record exists for the TAR:  
      * If the current depot auth status is 1, delete all related power‑zone, DTC‑SPKS, and workflow rows and remove the depot auth record.  
      * Otherwise, if not all TOA records have status 5, advance the depot workflow to the next active status, insert a new workflow entry, and update the depot auth status.  
      * If all TOA records are already status 5, set `@Message` to '-2' and jump to error handling.  
8. **Contact Information** – Fetch the OCC contact number for the current line from `TAMS_Parameters`.  
9. **SMS Message Construction** – Build a cancellation notification string that includes the TOA number if present; otherwise use the TAR number. The message ends with a prompt to contact OCC immediately or if required, depending on the line.  
10. **Send SMS** – If a phone number (`HPNo`) is available, invoke `sp_api_send_sms` with the constructed message.  
11. **Error Check** – If any SQL error occurs, set `@Message` to 'Error RGS Cancel' and jump to the error trap.  
12. **Commit/Rollback** – Commit the internal transaction if it was started; otherwise rollback on error.  
13. **Return** – Return the final `@Message` string; on error return -1.

---

**Data Interactions**

*Tables read (SELECTed from)*  
- `TAMS_TOA`  
- `TAMS_User`  
- `TAMS_TAR`  
- `TAMS_TAR_Power_Sector`  
- `TAMS_Endorser`  
- `TAMS_Workflow`  
- `TAMS_OCC_Auth`  
- `TAMS_Traction_Power_Detail`  
- `TAMS_Depot_Auth`  
- `TAMS_Depot_Auth_Powerzone`  
- `TAMS_Depot_DTCAuth_SPKS`  
- `TAMS_Depot_Auth_Workflow`  
- `TAMS_WFStatus`  
- `TAMS_Parameters`  
- `TAMS_Action_Log`

*Tables written (INSERT/UPDATE/DELETE)*  
- `TAMS_TOA` (UPDATE)  
- `TAMS_TOA_Audit` (INSERT)  
- `TAMS_Action_Log` (INSERT)  
- `TAMS_OCC_Auth` (UPDATE/DELETE)  
- `TAMS_OCC_Auth_Audit` (INSERT)  
- `TAMS_OCC_Auth_Workflow` (INSERT/UPDATE)  
- `TAMS_OCC_Auth_Workflow_Audit` (INSERT)  
- `TAMS_Depot_Auth_Powerzone` (DELETE)  
- `TAMS_Depot_DTCAuth_SPKS` (DELETE)  
- `TAMS_Depot_Auth_Workflow` (DELETE/INSERT/UPDATE)  
- `TAMS_Depot_Auth` (DELETE/UPDATE)  
- `TAMS_WFStatus` (UPDATE)  
- `TAMS_Parameters` (SELECT only)  
- `TAMS_Action_Log` (INSERT)  

All other tables are referenced only in control‑flow logic or stored‑procedure calls.