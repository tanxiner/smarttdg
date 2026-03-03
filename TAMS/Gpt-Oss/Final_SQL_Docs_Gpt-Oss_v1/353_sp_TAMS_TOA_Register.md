# Procedure: sp_TAMS_TOA_Register

### Purpose
Registers a Transfer of Authority (TOA) for a specified TAR, performing validation, qualification checks, and recording the outcome.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Type of track for the TOA. |
| @Type | NVARCHAR(20) | Category of the TOA (e.g., QRLocation). |
| @Loc | NVARCHAR(20) | Station name where the TOA is registered. |
| @TARNo | NVARCHAR(30) | Reference number of the TAR to be transferred. |
| @NRIC | NVARCHAR(20) | National registration identifier of the operator. |
| @TOAID | BIGINT OUTPUT | Identifier of the created or updated TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Status code or error description returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns it.
2. **Temp Table Creation** – Create `#tmpnric` to hold qualification check results.
3. **Parameter Retrieval** – Load `@CutOffTime`, `@QTSQualCode`, and `@QTSQualCodeProt` from `TAMS_Parameters` based on line, track type, and current date.
4. **TAR Validation**  
   * Count TARs matching `@TARNo` and the required status (8 for DTL/NEL, 9 for NEL).  
   * Verify that the specified station `@Loc` is linked to the TAR.  
   * If either check fails, set `@Message = '1'`, `@RecStatus = 'F'`, and `@ErrorDescription` accordingly.
5. **TAR Detail Retrieval** – If the TAR exists, fetch its ID, line, access date, and access type.
6. **Line Match Check** – If `@Line` differs from the TAR’s line, set error `@Message = '2'`.
7. **TOA Existence Check** – Look for an existing TOA for the TAR.  
   * If none exists, proceed to create one.  
   * If one exists, proceed to update or add parties based on status.
8. **Creation Path**  
   * Determine `@OPDate` based on current time relative to `@CutOffTime` and the TAR’s access date.  
   * Validate that the TAR’s access date matches today or tomorrow; otherwise set error `@Message = '3'` or `'4'`.  
   * Execute `sp_TAMS_TOA_QTS_Chk` with the NRIC, access date, line, and qualification code to populate `#tmpnric`.  
   * Extract `@InChargeName` and `@InChargeStatus`.  
   * If the status is `InValid` and the access type is `Protection`, retry with the protection code.  
   * If still invalid, set error `@Message = '9'`.  
   * If valid, insert a new record into `TAMS_TOA`, audit the insertion into `TAMS_TOA_Audit`, and add the in‑charge party to `TAMS_TOA_Parties`.  
   * Set `@Message = '99'`, `@RecStatus = 'S'`, and `@ErrorDescription = 'BookIn'`.
9. **Update Path (Existing TOA)**  
   * Verify that the NRIC matches the in‑charge NRIC of the existing TOA. If not, set error `@Message = '5'`.  
   * Retrieve the current `TOAStatus`.  
   * If status is 0 (pending), update the operation date using the same cutoff logic as in creation and set `@Message = '99'`.  
   * If status is 1 or 2, set `@Message = '98'` (AddParties).  
   * If status is 3, set `@Message = '97'` (BookOut).  
   * For any other status, set error `@Message = '8'`.
10. **Logging** – Insert a record into `TAMS_TOA_Registration_Log` capturing line, station, TAR number, encrypted NRIC, result status, and error description.
11. **Error Handling** – If any insert fails, set `@Message = 'ERROR INSERTING INTO TAMS_TOA'` and roll back the transaction if it was started by the procedure.
12. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Station`  
  - `TAMS_Station`  
  - `TAMS_TOA` (for existence and status checks)  
  - `sp_TAMS_TOA_QTS_Chk` (via dynamic execution)

* **Writes**  
  - `TAMS_TOA` (INSERT or UPDATE)  
  - `TAMS_TOA_Audit` (INSERT)  
  - `TAMS_TOA_Parties` (INSERT)  
  - `TAMS_TOA_Registration_Log` (INSERT)  
  - Temporary table `#tmpnric` (created, truncated, dropped)