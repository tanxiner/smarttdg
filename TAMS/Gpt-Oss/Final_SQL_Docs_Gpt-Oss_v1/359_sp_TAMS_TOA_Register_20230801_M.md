# Procedure: sp_TAMS_TOA_Register_20230801_M

### Purpose
Registers a Transfer of Authority (TOA) for a specified TAR, validating all business rules and recording the outcome.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Code of the line (e.g., NEL, TAMS). |
| @Type | NVARCHAR(20) | Type of TOA (e.g., BookIn, BookOut). |
| @Loc | NVARCHAR(20) | Station name where the TOA is requested. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be transferred. |
| @NRIC | NVARCHAR(20) | NRIC of the person initiating the TOA. |
| @TOAID | BIGINT OUTPUT | Identifier of the created or updated TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Status code or descriptive message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark that the procedure owns the transaction.  
2. **Temp Table Creation** – Create and truncate a temporary table `#tmpnric` to hold qualification check results.  
3. **Parameter Retrieval** –  
   * Fetch the cut‑off time for the line from `TAMS_Parameters`.  
   * Retrieve the QTS qualification codes for possession and protection for the line.  
4. **TAR Validation** –  
   * Count TARs matching the supplied `@TARNo`, correct status (9 for NEL, 8 otherwise), and `PowerOn = 0`.  
   * Count stations linked to that TAR that match `@Loc`.  
   * If either count is zero, set `@Message` to `'1'`, mark status as failure, and exit the validation block.  
5. **Line Match Check** – Retrieve the TAR’s line and access date. If the TAR’s line differs from `@Line`, set `@Message` to `'2'` and fail.  
6. **TOA Existence Check** –  
   * Look for an existing TOA record for the TAR.  
   * If none exists, proceed to create a new TOA; otherwise, handle updates or status changes.  
7. **New TOA Creation** –  
   * Determine the operation date based on the current time relative to the cut‑off.  
   * Validate that the TAR’s access date matches the expected date (today or tomorrow).  
   * Perform a QTS qualification check by executing `sp_TAMS_TOA_QTS_Chk` with the NRIC, access date, line, and possession code.  
   * If the result is invalid and the access type is “Protection”, retry with the protection code.  
   * If qualification fails, set `@Message` to `'9'` and fail.  
   * If qualification succeeds, insert a new record into `TAMS_TOA` with all relevant fields, encrypt the NRIC, and capture the new `@TOAID`.  
   * Insert an audit record into `TAMS_TOA_Audit` and a party record into `TAMS_TOA_Parties` marking the NRIC as the in‑charge party.  
   * Set `@Message` to `'99'` and status to success.  
8. **Existing TOA Update** –  
   * Verify that the NRIC matches the in‑charge NRIC for the TAR. If not, set `@Message` to `'5'`.  
   * Retrieve the current TOA status.  
   * If the status is 0 (pending), update the operation date following the same cut‑off logic and validate the access date. On success, set `@Message` to `'99'`.  
   * If the status is 1, 2, or 3, determine whether to add parties (`'98'`) or book out (`'97'`).  
   * For any other status, set `@Message` to `'8'`.  
9. **Logging** – Insert a record into `TAMS_TOA_Registration_Log` capturing the line, station, TAR number, encrypted NRIC, result status, and error description.  
10. **Error Handling** – If any error occurs during the insert into the log, set `@Message` to `'ERROR INSERTING INTO TAMS_TOA'` and roll back the transaction if owned.  
11. **Commit/Rollback** – Commit the transaction if it was started by the procedure; otherwise, leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads** – `TAMS_Parameters`, `TAMS_TAR`, `TAMS_Station`, `TAMS_TAR_Station`, `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties`.  
* **Writes** – `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties`, `TAMS_TOA_Registration_Log`.  

---