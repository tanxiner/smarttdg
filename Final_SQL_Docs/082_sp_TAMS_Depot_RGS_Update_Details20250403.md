# Procedure: sp_TAMS_Depot_RGS_Update_Details20250403

### Purpose
Updates the TOA record for a given TARID after validating the in‑charge NRIC against QTS qualification rules, and adjusts TOA parties accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person becoming in‑charge |
| @MobileNo | NVARCHAR(20) | Mobile number of the in‑charge |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number of the in‑charge |
| @UserID | NVARCHAR(500) | User performing the update |
| @TrackType | NVARCHAR(50) | Type of track; defaults to 'Mainline' |
| @Message | NVARCHAR(500) OUTPUT | Result code: '0' for success, '1' for invalid qualification, or error text |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns it.
2. **Temp Table Creation** – Create `#tmpnric` to hold QTS check results.
3. **Retrieve TOA Context** – From `TAMS_TOA` and `TAMS_TAR` fetch the line, access date, TOA ID, and access type for the supplied `@TARID`.
4. **Determine QTS Codes** – Query `TAMS_Parameters` to build two comma‑separated lists:
   * `@QTSQualCode` – codes relevant to the current access type and operation requirements.
   * `@QTSQualCodeProt` – codes for protection access when needed.
5. **Format Access Date** – Convert the access date to `dd/mm/yyyy` string in `@QualDate`.
6. **Primary QTS Validation Loop** – For each code in `@QTSQualCode`:
   * Build a dynamic call to either `sp_TAMS_Depot_TOA_QTS_Chk` or `sp_TAMS_TOA_QTS_Chk` based on `@TrackType`.
   * Execute the call and insert its result into `#tmpnric`.
7. **Extract In‑Charge Info** – From `#tmpnric` set `@InChargeName` and `@InChargeStatus`.
8. **Secondary Validation (Protection)** – If no record in `#tmpnric` has `qualstatus = 'Valid'`:
   * If the access type is 'Protection', repeat the QTS check loop using `@QTSQualCodeProt`.
   * After the loop, if any record is valid, aggregate its `qualcode` values into `@QTSFinQualCode` and set `@QTSFinStatus` to 'Valid'; otherwise set status to 'InValid'.
   * If the access type is not 'Protection', set status directly to 'InValid'.
9. **Cleanup** – Drop the temporary table.
10. **Handle Invalid Qualification** – If `@QTSFinStatus` is 'InValid', set `@Message` to '1' and skip further updates.
11. **Proceed with Valid Qualification** – If qualification is valid:
    * Count existing TOA parties for the TARID with the same decrypted `@InchargeNRIC`.
    * **No Existing In‑Charge** – Update `TAMS_TOA` with encrypted NRIC, name, mobile, tetra, and timestamps; audit the update; delete any existing in‑charge party records; insert a new party record with the in‑charge details and audit the insert.
    * **Existing In‑Charge Present** – Update only mobile and tetra fields in `TAMS_TOA`; audit the update.
    * Set `@Message` to '0' to indicate success.
12. **Error Handling** – If any error occurs, set `@Message` to an error string, rollback the transaction if it was started internally, and exit.
13. **Commit** – If the procedure started the transaction, commit it.
14. **Return** – Return the `@Message` value.

### Data Interactions
* **Reads**
  * `TAMS_TOA`
  * `TAMS_TAR`
  * `TAMS_Parameters`
  * `TAMS_TAR_AccessReq`
  * `TAMS_TOA_Parties`
* **Writes**
  * `TAMS_TOA`
  * `TAMS_TOA_Audit`
  * `TAMS_TOA_Parties_Audit`
  * `TAMS_TOA_Parties`

---