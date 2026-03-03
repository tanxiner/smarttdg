# Procedure: sp_TAMS_TOA_Register_20221117

### Purpose
Registers a Transfer of Authority (TOA) for a specified TAR, validating TAR status, location, line, access date, and qualification before inserting TOA and party records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line code for the TOA (e.g., NEL, TAMS). |
| @Type | NVARCHAR(20) | TOA type identifier. |
| @Loc | NVARCHAR(20) | Station name where the TOA is registered. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be processed. |
| @NRIC | NVARCHAR(20) | Personal identification number of the in‑charge person. |
| @TOAID | BIGINT OUTPUT | Returns the ID of the created or existing TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Returns a status code indicating success or the type of error encountered. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns the transaction.  
2. **Temporary Table Creation** – Create `#tmpnric` to hold qualification check results.  
3. **Parameter Retrieval** –  
   - Fetch `@CutOffTime` from `TAMS_Parameters` where `ParaCode='TOACutOffTime'` and the line matches `@Line`.  
   - Fetch `@QTSQualCode` where `ParaCode='QTSQualCode'`, line matches, `ParaValue3='Possession'`.  
   - Fetch `@QTSQualCodeProt` where `ParaCode='QTSQualCode'`, line matches, `ParaValue3=''`.  
4. **TAR Validation** –  
   - Count TARs with `TARNo=@TARNo`, status id 9 if `@Line='NEL'` else 8, and `PowerOn=0`.  
   - If none, set `@Message='1'` (Invalid TAR No).  
   - Count stations linked to that TAR where station name equals `@Loc`.  
   - If none, set `@Message='10'` (Invalid Location for selected TAR).  
5. **TAR Detail Retrieval** – If both counts are positive, select the TAR’s ID, line, access date, and access type into local variables.  
6. **Line Match Check** – If `@Line` differs from the TAR’s line, set `@Message='2'` (Invalid Line for selected TAR).  
7. **Existing TOA Check** –  
   - Look for a TOA record with the TAR’s ID.  
   - If none, proceed to create a new TOA; otherwise, handle updates or status changes.  
8. **New TOA Creation** –  
   - Determine `@OPDate` based on current time relative to `@CutOffTime` and compare `@TARAccessDate` to today or tomorrow.  
   - If the access date does not match the expected value, set `@Message='3'` or `'4'`.  
   - Perform qualification check by executing `sp_TAMS_TOA_QTS_Chk` with the NRIC, qualification date, line, and `@QTSQualCode`.  
   - If the result status is `InValid` and the access type is `Protection`, repeat the check with `@QTSQualCodeProt`.  
   - If the final qualification status is `InValid`, set `@Message='9'`.  
   - If qualification passes, insert a new record into `TAMS_TOA` with all relevant fields, encrypt the NRIC, and capture the new `@TOAID`.  
   - Insert a corresponding party record into `TAMS_TOA_Parties` marking the in‑charge person.  
   - Set `@Message='99'` (BookIn).  
9. **Existing TOA Handling** –  
   - Count TOA rows where the in‑charge NRIC matches `@NRIC`.  
   - If none, set `@Message='5'` (NRIC / Fin No does not match with InCharge).  
   - Retrieve the current `TOAStatus`.  
   - If status is 0 (pending), validate the access date as in the new case; if valid, update the operation date and set `@Message='99'`.  
   - If status is 3, 2, or 1, set `@Message='98'` (AddParties) for statuses 2 or 1, or `@Message='97'` (BookOut) for status 3.  
   - For any other status, set `@Message='8'` (Invalid TAR Status).  
10. **Error Handling** – If any error occurs during the process, set `@Message='ERROR INSERTING INTO TAMS_TOA'` and roll back the transaction.  
11. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise, leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Station`  
  - `TAMS_Station`  
  - `TAMS_TOA`  
  - `TAMS_TOA_Parties`  

* **Writes:**  
  - `TAMS_TOA`  
  - `TAMS_TOA_Parties`  

---