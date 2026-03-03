# Procedure: sp_TAMS_TOA_Register_bak20230801

### Purpose
Registers a TAR (Temporary Access Request) for a specified line and location, performing validation, qualification checks, and creating or updating TOA (Temporary Operation Authorization) records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line (e.g., NEL, TAMS) for the operation |
| @Type | NVARCHAR(20) | Type of TOA (e.g., BookIn, BookOut) |
| @Loc | NVARCHAR(20) | Station name where the operation will occur |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be processed |
| @NRIC | NVARCHAR(20) | National registration identifier of the person in charge |
| @TOAID | BIGINT OUTPUT | Identifier of the created or updated TOA record |
| @Message | NVARCHAR(500) OUTPUT | Result code indicating success, failure, or specific error condition |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new transaction and mark that the procedure owns it.
2. **Temporary Table Creation** – Create and truncate a temporary table `#tmpnric` to hold qualification check results.
3. **Parameter Retrieval** – Load cut‑off time, QTS qualification codes (for possession and protection) from `TAMS_Parameters` based on the line and current date.
4. **TAR Validation** – Count matching TAR records with the required status (9 for NEL, 8 otherwise) and power‑on flag 0.  
   *If no matching TAR or the specified location is not linked to the TAR, set error message ‘1’ or ‘10’ and exit.*
5. **TAR Details Fetch** – Retrieve TAR ID, line, access date, and access type for the matched TAR.
6. **Line Match Check** – If the requested line differs from the TAR’s line, set error message ‘2’ and exit.
7. **TOA Existence Check** – Look for an existing TOA record linked to the TAR.  
   *If none exists, proceed to create a new TOA; otherwise, handle updates or party additions.*
8. **New TOA Creation Path**  
   a. Determine operation date based on current time versus cut‑off time and TAR access date.  
   b. Validate that the TAR access date matches the expected date (today or tomorrow).  
   c. Perform QTS qualification check by executing `sp_TAMS_TOA_QTS_Chk` with the NRIC, qualification date, line, and appropriate QTS code.  
   d. If the first check fails and the access type is Protection, retry with the protection QTS code.  
   e. If qualification remains invalid, set error message ‘9’.  
   f. If qualification succeeds, insert a new record into `TAMS_TOA` with operation details, encrypted NRIC, and default values.  
   g. Capture the new TOA ID, insert an audit record into `TAMS_TOA_Audit`, and add the in‑charge party to `TAMS_TOA_Parties`.  
   h. Set success message ‘99’ (BookIn).
9. **Existing TOA Update Path**  
   a. Verify that the NRIC matches the in‑charge NRIC of the existing TOA.  
   b. If not matched, set error message ‘5’.  
   c. Retrieve current TOA status.  
   d. If status is 0 (pending), adjust operation date similarly to the new TOA path and update the `OperationDate`.  
   e. If status is 1, 2, or 3, determine whether to add parties (status 1 or 2 → message ‘98’) or book out (status 3 → message ‘97’).  
   f. If status is any other value, set error message ‘8’.
10. **Logging** – Insert a record into `TAMS_TOA_Registration_Log` capturing line, station, TAR number, encrypted NRIC, result status, and error description.
11. **Error Handling** – If any error occurs during the insert, set a generic error message and roll back the transaction if it was started by the procedure.
12. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise, leave it to the caller. Return the message code.

### Data Interactions
* **Reads:**  
  - TAMS_Parameters  
  - TAMS_TAR  
  - TAMS_TAR_Station  
  - TAMS_Station  
  - TAMS_TOA  
  - TAMS_TOA_Audit (for audit insertion)  
  - TAMS_TOA_Parties (for party count)  

* **Writes:**  
  - TAMS_TOA  
  - TAMS_TOA_Audit  
  - TAMS_TOA_Parties  
  - TAMS_TOA_Registration_Log  
  - Temporary table `#tmpnric` (created and truncated within the procedure)