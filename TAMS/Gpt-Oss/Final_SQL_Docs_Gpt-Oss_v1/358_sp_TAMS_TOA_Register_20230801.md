# Procedure: sp_TAMS_TOA_Register_20230801

### Purpose
Register a TOA for a TAR, performing validation of TAR status, location, line, access date, and qualification, then inserting the TOA, audit, party, and log records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., NEL, TAMS) |
| @Type | NVARCHAR(20) | TOA type |
| @Loc | NVARCHAR(20) | Station name (must exist in TAMS_Station) |
| @TARNo | NVARCHAR(30) | TAR number to register |
| @NRIC | NVARCHAR(20) | NRIC of the person registering |
| @TOAID | BIGINT OUTPUT | ID of the created or existing TOA |
| @Message | NVARCHAR(500) OUTPUT | Result code and description |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start one and flag internal transaction.
2. **Temp Table Creation** – Create and truncate `#tmpnric` for qualification results.
3. **Parameter Retrieval** – Load `@CutOffTime`, `@QTSQualCode`, and `@QTSQualCodeProt` from `TAMS_Parameters` for the given line and current date.
4. **TAR Validation**  
   a. Count TARs with the supplied `@TARNo`, correct status (9 for NEL, 8 otherwise), and `PowerOn = 0`.  
   b. Count stations linked to that TAR where `StationName = @Loc`.  
   c. If either count is zero, set error message 1 (invalid TAR or location) and exit.
5. **TAR Detail Retrieval** – Get `TARId`, `Line`, `AccessDate`, and `AccessType` for the TAR.
6. **Line Match Check** – If supplied `@Line` differs from the TAR line, set error message 2 and exit.
7. **Existing TOA Check** – Look for a TOA with the TAR ID.  
   - If none, proceed to create a new TOA.  
   - If one exists, handle based on its status.
8. **New TOA Creation**  
   a. Determine `@OPDate` based on current time vs `@CutOffTime` and compare `@TARAccessDate` to today or tomorrow.  
   b. If dates mismatch, set error messages 3 or 4 and exit.  
   c. Run `sp_TAMS_TOA_QTS_Chk` with NRIC, qualification date, line, and `@QTSQualCode` to populate `#tmpnric`.  
   d. Extract `InChargeName` and `InChargeStatus`.  
   e. If status is `InValid` and `AccessType` is `Protection`, rerun the check with `@QTSQualCodeProt`.  
   f. If final status remains `InValid`, set error message 9 and exit.  
   g. Insert a new record into `TAMS_TOA` with encrypted NRIC, timestamps, status 0, and other defaults.  
   h. Capture the new `@TOAID`.  
   i. Insert an audit record into `TAMS_TOA_Audit`.  
   j. Insert a party record into `TAMS_TOA_Parties` for the in‑charge person.  
   k. Set message 99, status `S`, description `BookIn`.
9. **Existing TOA Handling**  
   a. Verify that the NRIC matches the in‑charge NRIC of the TOA. If not, set error message 5.  
   b. Retrieve the TOA status.  
   c. If status is 0, perform the same date validation as in step 8a, update `OperationDate`, and set message 99.  
   d. If status is 3, 2, or 1, set message 98 (`AddParties`) for statuses 2 or 1, or message 97 (`BookOut`) for status 3.  
   e. For any other status, set error message 8.
10. **Logging** – Insert a record into `TAMS_TOA_Registration_Log` with encrypted NRIC, line, station, TAR number, status, and error description.
11. **Error Handling** – If any insert fails, set message `ERROR INSERTING INTO TAMS_TOA` and rollback if internal transaction.
12. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads** – `TAMS_Parameters`, `TAMS_TAR`, `TAMS_TAR_Station`, `TAMS_Station`, `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties`, `TAMS_TOA_Registration_Log`, and the procedure `sp_TAMS_TOA_QTS_Chk`.
* **Writes** – `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties`, `TAMS_TOA_Registration_Log`, and the temporary table `#tmpnric`.