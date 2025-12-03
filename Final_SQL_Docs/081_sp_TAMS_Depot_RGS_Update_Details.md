# Procedure: sp_TAMS_Depot_RGS_Update_Details

### Purpose
Updates the TOA record for a given TARID after validating the in‑charge’s qualification, and returns a status code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record whose TOA is being updated |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the person becoming the in‑charge |
| @MobileNo | NVARCHAR(20) | Mobile number to store for the in‑charge |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number to store for the in‑charge |
| @UserID | NVARCHAR(500) | Identifier of the user performing the update |
| @TrackType | NVARCHAR(50) | Type of track; defaults to 'Mainline' |
| @Message | NVARCHAR(500) OUTPUT | Result code: '0' = updated, '1' = invalid qualification, error message otherwise |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns it.
2. **Temp Table Creation** – Create `#tmpnric` to hold qualification check results.
3. **Retrieve TOA Context** – From `TAMS_TOA` and `TAMS_TAR` fetch the line, access date, TOA ID, and access type for the supplied `@TARID`.
4. **Fetch Qualification Codes** –  
   * Query `TAMS_Parameters` for `QTSQualCode` values that match the line, track type, and current date, considering whether the TAR has operation requirements 43 or 45.  
   * Query the same table for protected codes (`QTSQualCodeProt`) that match the line and track type.
5. **Prepare Dates and Code Lists** – Convert the access date to `dd/mm/yyyy` format, append commas to the code strings for easier parsing.
6. **Primary Qualification Check Loop** – For each code in `@QTSQualCode`  
   * Build a dynamic call to either `sp_TAMS_Depot_TOA_QTS_Chk` or `sp_TAMS_TOA_QTS_Chk` based on `@TrackType`.  
   * Execute the call and insert its result rows into `#tmpnric`.
7. **Extract In‑Charge Details** – Set `@InChargeName` and `@InChargeStatus` from the first row of `#tmpnric`.
8. **Validate Qualification** –  
   * If no row in `#tmpnric` has `qualstatus = 'Valid'`:  
     * If `@AccessType` is 'Protection':  
       * Re‑run the qualification check loop using `@QTSQualCodeProt`.  
       * After the loop, if still no valid status, mark the final status as 'InValid'; otherwise aggregate the valid `qualcode` values.  
     * If `@AccessType` is not 'Protection', mark the final status as 'InValid'.
   * If a valid status exists from the first loop, set the final status to 'Valid'.
9. **Cleanup Temp Table** – Drop `#tmpnric`.
10. **Handle Invalid Qualification** – If the final status is 'InValid', set `@Message` to '1' and skip the update logic.
11. **Proceed with Update** – If qualification is valid:  
    * Count existing TOA parties for the TAR where the decrypted `InChargeNRIC` matches `@InchargeNRIC`.  
    * **New In‑Charge (count = 0)**:  
      * Update `TAMS_TOA` with encrypted NRIC, name, mobile, radio, and audit fields.  
      * Insert an audit record into `TAMS_TOA_Audit`.  
      * Audit delete of the current in‑charge party in `TAMS_TOA_Parties_Audit`.  
      * Delete the current in‑charge party from `TAMS_TOA_Parties`.  
      * Insert a new party record with the supplied details, book‑in time, and status 'In'.  
      * Audit insert of the new party.  
    * **Existing In‑Charge (count > 0)**:  
      * Update `TAMS_TOA` with new mobile, radio, and audit fields.  
      * Insert an audit record into `TAMS_TOA_Audit`.  
    * Set `@Message` to '0' to indicate success.
12. **Error Check** – If any error occurs (`@@ERROR <> 0`), set `@Message` to 'ERROR INSERTING INTO TAMS_TOA' and jump to error handling.
13. **Transaction Finalization** – Commit the transaction if the procedure started it; otherwise leave it open. Return `@Message`.

### Data Interactions
* **Reads** – `TAMS_TOA`, `TAMS_TAR`, `TAMS_Parameters`, `TAMS_TAR_AccessReq`
* **Writes** – `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties_Audit`, `TAMS_TOA_Parties` (insert, update, delete)