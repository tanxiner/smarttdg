# Procedure: sp_TAMS_RGS_Update_Details

### Purpose
Updates the in‑charge details for a TAR record, validating the in‑charge’s qualification before applying changes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to update |
| @InchargeNRIC | NVARCHAR(50) | NRIC of the proposed in‑charge |
| @MobileNo | NVARCHAR(20) | Mobile number of the in‑charge |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number of the in‑charge |
| @UserID | NVARCHAR(50) | User performing the update |
| @Message | NVARCHAR(500) OUTPUT | Result code: '0' = success, '1' = invalid qualification, error message otherwise |

### Logic Flow
1. **Transaction handling** – If no active transaction, start one and mark it as internal.
2. **Temp table setup** – Create and truncate `#tmpnric` to hold qualification check results.
3. **Retrieve TAR context** – From `TAMS_TOA` and `TAMS_TAR` fetch the line, access date, TOA ID, and access type for the given `@TARID`.
4. **Get qualification codes** – From `TAMS_Parameters` obtain `QTSQualCode` for “Mainline Possession” and `QTSQualCodeProt` for “Mainline” that are currently effective.
5. **Initial qualification check** – Build a call to `sp_TAMS_TOA_QTS_Chk` with the in‑charge NRIC, formatted access date, line, and `QTSQualCode`. Execute it, inserting results into `#tmpnric`.
6. **Read check result** – Extract `namestr` and `qualstatus` into `@InChargeName` and `@InChargeStatus`.
7. **Determine final qualification status**  
   - If `@InChargeStatus` is `InValid` and the access type is `Protection`, run the check again using `QTSQualCodeProt`.  
   - Set `@QTSFinStatus` to `Valid` if the second check passes, otherwise `InValid`.  
   - If the first check passes, set `@QTSFinStatus` to `Valid`.  
   - If the first check fails and the access type is not `Protection`, set `@QTSFinStatus` to `InValid`.
8. **Clean up temp table** – Drop `#tmpnric`.
9. **Handle invalid qualification** – If `@QTSFinStatus` is `InValid`, set `@Message` to `'1'` and skip further updates.
10. **Proceed with update** – If qualification is valid:  
    a. Count existing TOA parties for the TAR whose decrypted NRIC matches `@InchargeNRIC`.  
    b. **No existing in‑charge** (`@InchargeCtr = 0`):  
       - Update `TAMS_TOA` with encrypted NRIC, name, mobile, tetra, and audit fields.  
       - Insert audit record into `TAMS_TOA_Audit`.  
       - Audit and delete any existing in‑charge party records in `TAMS_TOA_Parties`.  
       - Insert a new party record with `IsInCharge = 1`, book‑in time now, status `'In'`.  
       - Audit the new party insertion.  
    c. **Existing in‑charge** (`@InchargeCtr > 0`):  
       - Update only mobile and tetra fields in `TAMS_TOA`.  
       - Insert audit record into `TAMS_TOA_Audit`.  
    d. Set `@Message` to `'0'` to indicate success.
11. **Error check** – If any error occurred, set `@Message` to an error string and jump to error handling.
12. **Commit or rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller. Return `@Message`.

### Data Interactions
* **Reads:**  
  - `TAMS_TOA`  
  - `TAMS_TAR`  
  - `TAMS_Parameters`  
  - `TAMS_TOA_Parties`

* **Writes:**  
  - `TAMS_TOA`  
  - `TAMS_TOA_Audit`  
  - `TAMS_TOA_Parties`  
  - `TAMS_TOA_Parties_Audit`  
  - Temporary table `#tmpnric` (created and dropped within the procedure)