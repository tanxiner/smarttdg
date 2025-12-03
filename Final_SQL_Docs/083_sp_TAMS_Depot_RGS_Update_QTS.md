# Procedure: sp_TAMS_Depot_RGS_Update_QTS

### Purpose
Updates the QTS qualification status for a TAR record, validates the in‑charge NRIC against QTS parameters, and records audit and error information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person in charge |
| @UserID | NVARCHAR(500) | User performing the update |
| @TrackType | NVARCHAR(50) | Type of track; defaults to 'Mainline' |
| @Message | NVARCHAR(500) OUTPUT | Result code: '0' updated, '1' invalid qualification, '2' error updating, 'ERROR INSERTING INTO TAMS_TOA' on failure |
| @QTSQCode | NVARCHAR(50) OUTPUT | Comma‑separated list of valid QTS qualification codes |
| @QTSLine | NVARCHAR(10) OUTPUT | Rail line associated with the TAR |

### Logic Flow
1. **Transaction Setup** – If no outer transaction, start a new one and flag internal transaction.
2. **Temp Table Creation** – Create `#tmpnric` to hold NRIC validation results.
3. **Retrieve TAR Context** – Pull line, access date, TOA ID, and access type from `TAMS_TOA` and `TAMS_TAR`.
4. **Determine QTS Qualification Codes** –  
   * Query `TAMS_Parameters` for `QTSQualCode` matching the line, track type, and a pattern that depends on whether the TAR has selected operation requirements 43 or 45.  
   * Query `TAMS_Parameters` for `QTSQualCodeProt` using a similar filter but with a different track type label.  
   * Append a trailing comma to each code list.
5. **Validate NRIC Against QTS Codes** –  
   * Split `@QTSQualCode` by commas.  
   * For each code, build a call to either `sp_TAMS_Depot_TOA_QTS_Chk` or `sp_TAMS_TOA_QTS_Chk` (based on `@TrackType`) with the NRIC, qualification date, line, and the current code.  
   * Execute the call and insert the result rows into `#tmpnric`.  
   * After all codes, capture the first row’s `namestr` and `qualstatus` into `@InChargeName` and `@InChargeStatus`.
6. **Handle Invalid Qualification** –  
   * If no row in `#tmpnric` has `qualstatus = 'Valid'` (or the status is invalid), and the access type is 'Protection', repeat step 5 using `@QTSQualCodeProt`.  
   * If still no valid status, set `@QTSFinStatus` to 'InValid' and clear `@QTSFinQualCode`.  
   * If a valid status is found, set `@QTSFinStatus` to 'Valid' and aggregate all `qualcode` values from valid rows into `@QTSFinQualCode`.
7. **Set Output Messages** –  
   * If `@QTSFinStatus` is 'InValid', set `@Message` to '1', clear `@QTSQCode` and `@QTSLine`.  
   * If valid, proceed to update QTS:
     * Build a user identifier `TAMS-<@UserID>`.  
     * Append a trailing comma to `@QTSFinQualCode`.  
     * Split `@QTSFinQualCode` by commas and for each code call `sp_api_tams_qts_upd_accessdate` on the `QTSDB` server, passing the NRIC, code, line, and the TAMS user. Capture the returned message in `@RetMsg`.  
     * If `@RetMsg` is empty after all calls, update `TAMS_TOA` with current timestamps and insert an audit row; set `@Message` to '0'.  
     * If `@RetMsg` contains text, set `@Message` to '2'.
8. **Error Handling** –  
   * If any error occurs, roll back the transaction if it was started internally, log the error into `TAMS_QTS_Error_Log` with encrypted NRIC, and return the error message via `@Message`.
9. **Commit or Rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller.

### Data Interactions
* **Reads:**  
  * `TAMS_TOA` – to obtain line, access date, TOA ID, and access type.  
  * `TAMS_TAR` – to match TAR ID.  
  * `TAMS_Parameters` – to fetch QTS qualification codes.  
  * `TAMS_TAR_AccessReq` – to determine operation requirement flags.  
  * `TAMS_QTS_Error_Log` – for error logging (write only).  
* **Writes:**  
  * `TAMS_TOA` – update timestamps when QTS is successfully updated.  
  * `TAMS_TOA_Audit` – audit record of the update.  
  * `TAMS_QTS_Error_Log` – error details on failure.  
  * Temporary table `#tmpnric` – holds intermediate NRIC validation results.  
* **External Calls:**  
  * `sp_TAMS_Depot_TOA_QTS_Chk` / `sp_TAMS_TOA_QTS_Chk` – validate NRIC against each QTS code.  
  * `sp_api_tams_qts_upd_accessdate` on `QTSDB` – update QTS access dates for each valid code.