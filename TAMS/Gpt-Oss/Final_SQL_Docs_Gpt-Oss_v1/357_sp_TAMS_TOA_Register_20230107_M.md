# Procedure: sp_TAMS_TOA_Register_20230107_M

### Purpose
Registers a Transfer of Authority (TOA) for a specified TAR, performing validation of TAR status, location, line, access date, and qualification, then inserting or updating TOA records and related audit and party information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Code of the line (e.g., NEL, TAMS) to which the TOA applies. |
| @Type | NVARCHAR(20) | Type of TOA being requested. |
| @Loc | NVARCHAR(20) | Station name where the TOA is to be registered. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR for which the TOA is being processed. |
| @NRIC | NVARCHAR(20) | Personal identification number of the individual requesting the TOA. |
| @TOAID | BIGINT OUTPUT | Identifier of the newly created or existing TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Status code indicating success or the type of error encountered. |

### Logic Flow
1. **Transaction Setup** – If no active transaction exists, start a new one and flag that the procedure owns the transaction.  
2. **Temporary Table Creation** – Create `#tmpnric` to hold results from the QTS qualification check.  
3. **Parameter Retrieval** – Load the cutoff time for the specified line, the QTS qualification code for possession, and the protection code (if any) from `TAMS_Parameters`.  
4. **TAR Validation**  
   * Count TARs matching `@TARNo` with the required status (9 for NEL, 8 otherwise) and `PowerOn = 0`.  
   * Count stations linked to that TAR that match `@Loc`.  
   * If either count is zero, set `@Message` to `1` (invalid TAR) or `10` (invalid location) and exit.  
5. **TAR Detail Retrieval** – Fetch the TAR’s ID, line, access date, and access type.  
6. **Line Check** – If `@Line` differs from the TAR’s line, set `@Message` to `2` (invalid line) and exit.  
7. **Existing TOA Check** – Look for a TOA record for the TAR.  
   * **No Existing TOA**  
     * Determine the operation date: if the current time is before the cutoff, use the previous day; otherwise use today.  
     * Validate that the TAR’s access date matches the expected date (today or tomorrow depending on cutoff). If not, set `@Message` to `3` or `4`.  
     * Execute the QTS qualification check via `sp_TAMS_TOA_QTS_Chk` using the appropriate qualification code.  
     * If the result is “InValid” and the access type is “Protection”, re‑run the check with the protection code.  
     * If the final qualification status is “InValid”, set `@Message` to `9`.  
     * Otherwise, insert a new TOA record with the gathered data, create an audit entry, and add a party record for the in‑charge person. Set `@Message` to `99` (BookIn).  
   * **Existing TOA Present**  
     * Verify that the supplied `@NRIC` matches the in‑charge NRIC in the TOA. If not, set `@Message` to `5`.  
     * Retrieve the current TOA status.  
     * If the status is `0` (pending), update the operation date using the same cutoff logic as above and set `@Message` to `99`.  
     * If the status is `1` or `2`, set `@Message` to `98` (AddParties).  
     * If the status is `3`, set `@Message` to `97` (BookOut).  
     * For any other status, set `@Message` to `8` (invalid TAR status).  
8. **Error Handling** – If any error occurs during the process, set `@Message` to `ERROR INSERTING INTO TAMS_TOA` and roll back the transaction if it was started by the procedure.  
9. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it to the caller. Return the final `@Message`.

### Data Interactions
* **Reads** – `TAMS_Parameters`, `TAMS_TAR`, `TAMS_TAR_Station`, `TAMS_Station`, `TAMS_TOA`.  
* **Writes** – `TAMS_TOA`, `TAMS_TOA_Audit`, `TAMS_TOA_Parties`, temporary table `#tmpnric`.  
* **External Procedure Call** – `sp_TAMS_TOA_QTS_Chk` for qualification validation.