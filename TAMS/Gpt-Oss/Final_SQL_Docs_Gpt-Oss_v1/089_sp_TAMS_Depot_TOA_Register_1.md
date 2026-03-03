# Procedure: sp_TAMS_Depot_TOA_Register_1

### Purpose
Registers a TOA for a specified TAR and NRIC, performing validation against line, station, access dates, QTS codes, and existing TOA status, then logs the outcome.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line (e.g., DTL, NEL, NELD) |
| @TrackType | NVARCHAR(50) | Type of track – DEPOT or Mainline |
| @Type | NVARCHAR(20) | Operation type (used for date logic) |
| @Loc | NVARCHAR(20) | Station name (lookup in TAMS_Station) |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to process |
| @NRIC | NVARCHAR(20) | Personal identifier of the user |
| @TOAID | BIGINT OUTPUT | Identifier of the created or found TOA |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start one and mark it as internal.
2. **Temp Table Creation** – Create `#tmpnric` to hold QTS check results.
3. **Parameter Retrieval** –  
   a. Get `@CutOffTime` from `TAMS_Parameters` for the given line and track type.  
   b. Build comma‑separated `@QTSQualCode` and `@QTSQualCodeProt` lists from `TAMS_Parameters` based on line, track type, and whether the TAR requires Train or PC access.  
4. **TAR Count** – Count TARs matching the provided `@TARNo` and status (8 or 9) and `PowerOn` flag, storing in `@TARCtr`.  
5. **Station Validation** –  
   a. If `@TrackType` is DEPOT, set `@StationCtr` to 1.  
   b. Otherwise, count matching station records for the TAR and location, storing in `@StationCtr`.  
6. **Early Failure Checks** – If either `@TARCtr` or `@StationCtr` is zero, set `@Message` to '1', `@RecStatus` to 'F', and an appropriate error description.  
7. **TAR Retrieval** – If counts are valid, fetch TAR details (`ID`, `Line`, `AccessDate`, `AccessType`) into local variables.  
8. **Line Mismatch Check** – If the TAR line differs from `@Line`, set `@Message` to '2', `@RecStatus` to 'F'.  
9. **TOA Existence Check** – Look for an existing TOA for the TAR; store its ID in `@TOAID`.  
10. **TOA Creation Path (no existing TOA)** –  
    a. Determine operation date `@OPDate` based on track type, current time vs. `@CutOffTime`, and TAR access date.  
    b. For DEPOT, enforce a 3‑hour pre‑access window; if violated, set `@Message` to '11', rollback, and exit.  
    c. Verify that the TAR access date matches the expected date (current or next day). If not, set `@Message` to '4'.  
    d. Run QTS checks for each code in `@QTSQualCode` by executing the appropriate stored procedure (`sp_TAMS_Depot_TOA_QTS_Chk` or `sp_TAMS_TOA_QTS_Chk`) and inserting results into `#tmpnric`.  
    e. Extract the first record’s `namestr` and `qualstatus` into `@InChargeName` and `@InChargeStatus`.  
11. **TOA Update Path (existing TOA)** –  
    a. Count TOAs where the decrypted `InChargeNRIC` matches `@NRIC`. If none, set `@Message` to '5'.  
    b. Retrieve the TOA status `@TOStatus`.  
    c. If status is 0 (unbooked), update `OperationDate` to `@OPDate` and set `@Message` to '99' (BookIn).  
    d. If status is 1, 2, or 3, set `@Message` to '97' (BookOut) or '98' (AddParties) accordingly.  
    e. For any other status, set `@Message` to '8' (Invalid TAR Status).  
12. **Logging** – Insert a record into `TAMS_TOA_Registration_Log` with line, station, TARNo, encrypted NRIC, `@RecStatus`, `@ErrorDescription`, and current timestamp.  
13. **Error Handling** – If the insert fails, set `@Message` to an error string and jump to the error trap.  
14. **Commit/Rollback** – Commit the transaction if internal; otherwise rollback on error. Return `@Message`.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Station`  
  - `TAMS_Station`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_TOA`  
* **Writes:**  
  - `TAMS_TOA_Registration_Log` (insert)  
  - `TAMS_TOA` (update `OperationDate` when booking in)  

---