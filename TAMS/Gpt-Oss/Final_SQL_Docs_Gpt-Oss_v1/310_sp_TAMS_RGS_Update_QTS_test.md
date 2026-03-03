# Procedure: sp_TAMS_RGS_Update_QTS_test

### Purpose
Updates the QTS qualification status for a TAR record by validating the in‑charge NRIC against QTS rules and invoking the QTS API to record the access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person in charge whose qualification is being checked |
| @UserID | NVARCHAR(500) | User performing the operation |
| @Message | NVARCHAR(500) OUTPUT | Result code: 0 = success, 1 = invalid qualification, 2 = error updating, ERROR INSERTING INTO TAMS_TOA |
| @QTSQCode | NVARCHAR(50) OUTPUT | Qualification code returned from QTS validation |
| @QTSLine | NVARCHAR(10) OUTPUT | Line identifier associated with the TAR record |

### Logic Flow
1. **Transaction handling** – If no active transaction, start a new one and mark that the procedure owns it.  
2. **Temp table setup** – Create a temporary table `#tmpnric` to hold the result of the QTS check.  
3. **Retrieve TAR context** – From `TAMS_TOA` and `TAMS_TAR` fetch the line, access date, TOA ID, and access type for the given `@TARID`.  
4. **Get QTS qualification codes** – Query `TAMS_Parameters` for the possession code (`@QTSQualCode`) and the protection code (`@QTSQualCodeProt`) that apply to the line and are currently effective.  
5. **Initial QTS check** – Build a dynamic call to `sp_TAMS_TOA_QTS_Chk` with the in‑charge NRIC, access date, line, and possession code; execute it and insert the result into `#tmpnric`.  
6. **Read check result** – Extract `namestr` and `qualstatus` from `#tmpnric` into `@InChargeName` and `@InChargeStatus`.  
7. **Handle invalid status** –  
   * If `@InChargeStatus` is `InValid` and the access type is `Protection`, re‑run the QTS check using the protection code.  
   * Update `@QTSFinStatus` and `@QTSFinQualCode` based on the second check result.  
   * If still invalid, set `@QTSFinStatus` to `InValid`.  
8. **Handle valid status** – If the first check returned `Valid`, set `@QTSFinStatus` to `Valid` and `@QTSFinQualCode` to the possession code.  
9. **Clean up temp table** – Drop `#tmpnric`.  
10. **Determine outcome** –  
    * If `@QTSFinStatus` is `InValid`, set `@Message` to `1`, clear `@QTSQCode` and `@QTSLine`.  
    * If valid, set `@Message` to `0`, assign `@QTSQCode` and `@QTSLine`, then call the external QTS API `sp_api_tams_qts_upd_accessdate` with the NRIC, qualification code, line, and user ID.  
    * If the API returns an empty message, keep `@Message` as `0`; otherwise set it to `2` to indicate an error updating QTS.  
11. **Error handling** – If any error occurs, set `@Message` to `ERROR INSERTING INTO TAMS_TOA` and jump to the error trap.  
12. **Commit or rollback** – Commit the transaction if the procedure started it; otherwise leave the transaction unchanged. Return the final `@Message`.

### Data Interactions
* **Reads:**  
  - `TAMS_TOA`  
  - `TAMS_TAR`  
  - `TAMS_Parameters`  
  - `sp_TAMS_TOA_QTS_Chk` (via dynamic execution)  

* **Writes:**  
  - Temporary table `#tmpnric` (session‑only)  
  - External QTS database via `sp_api_tams_qts_upd_accessdate` (updates QTS access date)  
  - (Optional, currently commented) updates to `TAMS_TOA` and inserts into `TAMS_TOA_Audit` could occur if uncommented.