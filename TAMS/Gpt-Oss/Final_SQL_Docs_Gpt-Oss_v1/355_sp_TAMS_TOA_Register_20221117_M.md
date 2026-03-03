# Procedure: sp_TAMS_TOA_Register_20221117_M

### Purpose
Registers a Transfer of Authority (TOA) for a specified TAR, validating the TAR, location, line, access date, and qualification before inserting or updating TOA records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line code for the TAR (e.g., NEL, TAMS). |
| @Type | NVARCHAR(20) | Type of TOA to register. |
| @Loc | NVARCHAR(20) | Station name where the TOA is performed. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be registered. |
| @NRIC | NVARCHAR(20) | National registration identifier of the person in charge. |
| @TOAID | BIGINT OUTPUT | Identifier of the created or updated TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Status code indicating success or specific error. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start one and flag that the procedure owns the transaction.  
2. **Temp Table Creation** – Create `#tmpnric` to hold qualification check results.  
3. **Parameter Retrieval** –  
   * `@CutOffTime` is fetched from `TAMS_Parameters` where `ParaCode='TOACutOffTime'` and the line matches.  
   * `@QTSQualCode` and `@QTSQualCodeProt` are fetched for possession and protection checks respectively.  
4. **TAR Validation** –  
   * Count TARs matching `@TARNo`, correct status (NEL → 9, others → 8), and `PowerOn=0`.  
   * Count stations linked to that TAR where the station name equals `@Loc`.  
   * If either count is zero, set `@Message` to `'1'` (invalid TAR) or `'10'` (invalid location) and exit.  
5. **TAR Detail Retrieval** – Load TAR ID, line, access date, and access type into local variables.  
6. **Line Check** – If the supplied `@Line` differs from the TAR’s line, set `@Message` to `'2'` and exit.  
7. **Existing TOA Check** – Search `TAMS_TOA` for a record with the TAR ID.  
   * If none exists, proceed to create a new TOA.  
   * If one exists, proceed to update or validate the existing record.  
8. **New TOA Creation** –  
   * Determine `@OPDate`: yesterday if current time ≤ `@CutOffTime`, otherwise today.  
   * Validate that the TAR’s access date matches the current date or the next day, setting messages `'3'` or `'4'` on mismatch.  
   * Perform qualification check by executing `sp_TAMS_TOA_QTS_Chk` with the NRIC, qualification date, line, and the appropriate QTS code.  
   * If the first check returns `InValid` and the access type is `Protection`, run the protection‑code check.  
   * If qualification remains `InValid`, set `@Message` to `'9'`.  
   * If qualification is `Valid`, insert a new record into `TAMS_TOA` with all required fields, encrypting the NRIC.  
   * Insert a corresponding party record into `TAMS_TOA_Parties` marking the person as in‑charge.  
   * Set `@Message` to `'99'` (BookIn).  
9. **Existing TOA Update** –  
   * Verify that the NRIC matches the in‑charge NRIC of the existing TOA; if not, set `@Message` to `'5'`.  
   * Retrieve the current `TOAStatus`.  
   * If status is `0` (pending), perform the same date validation as in the new TOA path, update the operation date, and set `@Message` to `'99'`.  
   * If status is `1`, `2`, or `3`, set `@Message` to `'98'` (AddParties) for statuses `1` or `2`, or `'97'` (BookOut) for status `3`.  
   * For any other status, set `@Message` to `'8'` (Invalid TAR Status).  
10. **Error Handling** – If any error occurs during the procedure, set `@Message` to `'ERROR INSERTING INTO TAMS_TOA'` and roll back the transaction if it was started internally.  
11. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads**  
  * `TAMS_Parameters` – for cutoff time and QTS codes.  
  * `TAMS_TAR` – to validate TAR existence, status, and access details.  
  * `TAMS_TAR_Station` & `TAMS_Station` – to confirm the location is linked to the TAR.  
  * `TAMS_TOA` – to check for an existing TOA and to read its status.  
  * `TAMS_TOA_Parties` – to verify the NRIC matches the in‑charge party.  
* **Writes**  
  * `TAMS_TOA` – inserts a new TOA or updates the operation date of an existing one.  
  * `TAMS_TOA_Parties` – inserts a party record when a new TOA is created.  
* **Temp Table** – `#tmpnric` holds intermediate qualification check results.  
* **External Procedure** – `sp_TAMS_TOA_QTS_Chk` is called to perform qualification validation.