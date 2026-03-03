# Procedure: sp_TAMS_RGS_Update_QTS_bak20221229

### Purpose
Updates the QTS qualification status for a specific TAR record, records the change, and returns status information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person in charge whose qualification is being checked |
| @UserID | NVARCHAR(500) | User performing the update |
| @Message | NVARCHAR(500) OUTPUT | Result code: '0' = success, '1' = invalid qualification, '2' = error updating, 'ERROR INSERTING INTO TAMS_TOA' |
| @QTSQCode | NVARCHAR(50) OUTPUT | Final QTS qualification code applied |
| @QTSLine | NVARCHAR(10) OUTPUT | Line identifier associated with the qualification |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns the transaction.
2. **Temp Table Creation** – Create a temporary table `#tmpnric` to hold the result of a dynamic call to `sp_TAMS_TOA_QTS_Chk`.
3. **Retrieve TAR Context** – Select the line, access date, TOA ID, and access type for the given `@TARID` by joining `TAMS_TOA` and `TAMS_TAR`.
4. **Determine Qualification Codes** – Query `TAMS_Parameters` for the standard and protection qualification codes that apply to the line and current date.
5. **Initial Qualification Check** – Build an execution string for `sp_TAMS_TOA_QTS_Chk` using the in‑charge NRIC, access date, line, and standard qualification code. Execute it and capture the returned name and status into `@InChargeName` and `@InChargeStatus`.
6. **Handle Invalid Status** – If the status is `InValid`:
   - If the access type is `Protection`, repeat the check using the protection qualification code.
   - Set the final status and qualification code based on the second check’s result.
   - If still `InValid`, mark the final status as `InValid` with no qualification code.
   - If valid, mark the final status as `Valid` and use the protection code.
   - If the access type is not `Protection`, mark the final status as `InValid`.
7. **Handle Valid Status** – If the initial status is not `InValid`, set the final status to `Valid` and use the standard qualification code.
8. **Clean Up Temp Table** – Drop `#tmpnric`.
9. **Return or Apply Update** –  
   - If the final status is `InValid`, set `@Message` to '1', clear the output qualification code and line.  
   - If the final status is `Valid`:
     - Update `TAMS_TOA` with the current time, user, and updated timestamp for the TAR record.  
     - Insert a copy of the updated row into `TAMS_TOA_Audit` with action type 'U'.  
     - Set `@Message` to '0', return the final qualification code and line.  
     - (Optional external call to QTSDB is present but commented out.)
10. **Error Check** – If any error occurs after the update, set `@Message` to 'ERROR INSERTING INTO TAMS_TOA' and jump to error handling.
11. **Commit or Rollback** – Commit the transaction if it was started by the procedure; otherwise leave it open. Return the message code.

### Data Interactions
* **Reads:**  
  - `TAMS_TOA` (to fetch line, access date, TOA ID, access type, and to update)  
  - `TAMS_TAR` (to join with TOA for line and access type)  
  - `TAMS_Parameters` (to obtain qualification codes)  
  - `#tmpnric` (temporary result of `sp_TAMS_TOA_QTS_Chk`)  
  - `sp_TAMS_TOA_QTS_Chk` (dynamic call that reads qualification data)

* **Writes:**  
  - `TAMS_TOA` (updates timestamp, user, and update time)  
  - `TAMS_TOA_Audit` (audit record of the update)  
  - (Potential external write to QTSDB via `sp_api_tams_qts_upd_accessdate_m`, though currently commented out)