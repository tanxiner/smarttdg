# Procedure: sp_TAMS_RGS_Update_QTS

### Purpose
Updates the QTS qualification status for a specific TOA record and synchronises the change with the external QTS system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TOA record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person whose qualification is being checked |
| @UserID | NVARCHAR(500) | User performing the update |
| @TrackType | NVARCHAR(50) | Type of track (default “Mainline”) – not used in logic |
| @Message | NVARCHAR(500) OUTPUT | Result code: 0 = success, 1 = invalid qualification, 2 = error updating, “ERROR INSERTING INTO TAMS_TOA” = internal error |
| @QTSQCode | NVARCHAR(50) OUTPUT | Qualification code that was applied (empty if invalid) |
| @QTSLine | NVARCHAR(10) OUTPUT | Rail line that was processed |

### Logic Flow
1. **Transaction handling** – If the procedure is called outside an existing transaction, it starts a new one and marks that it owns the transaction.
2. **Temporary table** – Creates `#tmpnric` to hold the result of a qualification check.
3. **Retrieve TOA context** – Reads the rail line, access date, TOA ID and access type for the supplied `@TARID` from `TAMS_TOA` and `TAMS_TAR`.
4. **Get qualification codes** – Looks up two possible QTS qualification codes from `TAMS_Parameters`:
   * `@QTSQualCode` for “Mainline Possession”
   * `@QTSQualCodeProt` for “Mainline” (used only for protection access types)
5. **Initial qualification check** – Calls `sp_TAMS_TOA_QTS_Chk` with the NRIC, access date, line and `@QTSQualCode`. The result is inserted into `#tmpnric`. The NRIC name and qualification status are extracted.
6. **Handle invalid status** – If the status returned is “InValid”:
   * If the access type is “Protection”, the procedure repeats the check using `@QTSQualCodeProt`.  
     * If this second check is still “InValid”, the final status is set to “InValid” and the qualification code is cleared.  
     * Otherwise the final status becomes “Valid” and the qualification code is `@QTSQualCodeProt`.
   * If the access type is not “Protection”, the final status is set to “InValid” and the qualification code is cleared.
7. **Valid status** – If the initial check returned “Valid”, the final status is “Valid” and the qualification code is `@QTSQualCode`.
8. **Clean up temporary table** – Drops `#tmpnric`.
9. **Return on invalid qualification** – If the final status is “InValid”, sets `@Message` to ‘1’, clears `@QTSQCode` and `@QTSLine`, and skips the external update.
10. **External QTS update** – If the qualification is valid:
    * Sets `@Message` to ‘0’, assigns `@QTSQCode` and `@QTSLine`.
    * Builds a user identifier `TAMS-<@UserID>`.
    * Calls the external procedure `[flexnetskgsvr].[QTSDB].[dbo].[sp_api_tams_qts_upd_accessdate]` with the NRIC, qualification code, line and the constructed user ID.  
      * If the external call returns an empty message, the procedure updates `TAMS_TOA` with the current time and user, inserts an audit record into `TAMS_TOA_Audit`, and keeps `@Message` as ‘0’.  
      * If the external call returns a non‑empty message, sets `@Message` to ‘2’ (error updating).
11. **Error handling** – If any error occurs after the external call, the procedure rolls back the transaction (if it started one), logs the error details into `TAMS_QTS_Error_Log` (encrypting the NRIC), and returns the error message code.
12. **Commit** – If no error and the procedure owns the transaction, it commits.
13. **Return** – Returns the final `@Message` value.

### Data Interactions
* **Reads:**  
  * `TAMS_TOA` – to obtain line, access date, TOA ID and access type.  
  * `TAMS_TAR` – to link the TOA record.  
  * `TAMS_Parameters` – to fetch qualification codes.  
  * `TAMS_TOA_Audit` – not read, only written.  
  * `TAMS_QTS_Error_Log` – not read, only written.  

* **Writes:**  
  * `TAMS_TOA` – updates `UpdateQTSTime`, `UpdatedOn`, `UpdatedBy`.  
  * `TAMS_TOA_Audit` – inserts a record of the update.  
  * `TAMS_QTS_Error_Log` – inserts a log entry when an error occurs.  
  * Temporary table `#tmpnric` – created and dropped within the procedure.  
  * External procedure `sp_api_tams_qts_upd_accessdate` – updates the QTS system.