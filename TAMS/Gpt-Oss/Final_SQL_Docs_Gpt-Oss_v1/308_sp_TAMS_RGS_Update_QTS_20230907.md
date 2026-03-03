# Procedure: sp_TAMS_RGS_Update_QTS_20230907

### Purpose
Updates the QTS qualification status for a specific TAR record after validating the in‑charge NRIC against the QTS system, and records audit information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person in charge whose qualification is being checked |
| @UserID | NVARCHAR(500) | User performing the update, used for audit fields |
| @Message | NVARCHAR(500) OUTPUT | Result code: 0 = updated, 1 = invalid qualification, 2 = error updating, ERROR INSERTING INTO TAMS_TOA |
| @QTSQCode | NVARCHAR(50) OUTPUT | Final QTS qualification code applied to the record |
| @QTSLine | NVARCHAR(10) OUTPUT | Line value associated with the record |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark that this procedure owns the transaction.
2. **Temp Table Creation** – Create a temporary table `#tmpnric` to hold NRIC validation results.
3. **Retrieve Core Data** – From `TAMS_TOA` and `TAMS_TAR` fetch the line, access date, TOA ID, and access type for the given `@TARID`.
4. **Lookup QTS Codes** – From `TAMS_Parameters` obtain the mainline possession qualification code (`@QTSQualCode`) and the mainline protection qualification code (`@QTSQualCodeProt`) for the retrieved line, valid for the current date.
5. **Initial Qualification Check** – Convert the access date to `dd/mm/yyyy` format, build a call string for `sp_TAMS_TOA_QTS_Chk`, execute it, and capture the returned name and status into `@InChargeName` and `@InChargeStatus`.
6. **Determine Final Status**  
   * If the status is **InValid** and the access type is **Protection**, re‑run the check using the protection qualification code.  
   * If still **InValid**, set final status to **InValid** and clear the qualification code.  
   * If valid, set final status to **Valid** and use the appropriate qualification code (`@QTSQualCode` or `@QTSQualCodeProt`).  
   * If the initial status is **Valid**, keep it as **Valid** with the mainline possession code.
7. **Cleanup Temp Table** – Drop `#tmpnric`.
8. **Handle Invalid Qualification** – If final status is **InValid**, set `@Message` to `1`, clear `@QTSQCode` and `@QTSLine`, and skip further updates.
9. **Update Record on Valid Qualification**  
   * Update `TAMS_TOA` with current timestamps and `@UserID`.  
   * Insert a snapshot of the updated row into `TAMS_TOA_Audit`.  
   * Set `@Message` to `0`, assign `@QTSQCode` and `@QTSLine`.  
   * Call external procedure `sp_api_tams_qts_upd_accessdate` in the `QTSDB` database, passing the NRIC, qualification code, line, and user ID, capturing a return message.  
   * If the external call returns an empty message, repeat the update and audit steps to ensure consistency; otherwise set `@Message` to `2` to indicate an error from the external system.
10. **Error Check** – If any error flag is set, set `@Message` to `ERROR INSERTING INTO TAMS_TOA` and jump to error handling.
11. **Commit or Rollback** – If this procedure started the transaction, commit it; otherwise leave it to the caller. On error, rollback the transaction.
12. **Return** – Return the final `@Message` value.

### Data Interactions
* **Reads:** `TAMS_TOA`, `TAMS_TAR`, `TAMS_Parameters`
* **Writes:** `TAMS_TOA`, `TAMS_TOA_Audit`, external `QTSDB` procedure `sp_api_tams_qts_upd_accessdate` (writes to QTS system)