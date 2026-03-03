# Procedure: sp_TAMS_TOA_Register_20230107

### Purpose
Register a TOA for a specified TAR, performing validation of TAR existence, location, line, access date, cutoff time, and QTS qualification, then inserting or updating TOA, audit, and parties records accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line (e.g., NEL) for the TOA. |
| @Type | NVARCHAR(20) | Type of TOA (e.g., BookIn, BookOut). |
| @Loc | NVARCHAR(20) | Station name where the TOA is registered. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be processed. |
| @NRIC | NVARCHAR(20) | NRIC of the person registering the TOA. |
| @TOAID | BIGINT OUTPUT | Identifier of the created or updated TOA record. |
| @Message | NVARCHAR(500) OUTPUT | Status code indicating success or specific error. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag internal transaction.  
2. **Temp Table Creation** – Create and truncate a temporary table #tmpnric for holding QTS check results.  
3. **Parameter Retrieval** –  
   - Fetch the cutoff time for the specified line from TAMS_Parameters.  
   - Retrieve the QTS qualification code for possession and for protection (if needed).  
4. **TAR Validation** –  
   - Count TAR records matching @TARNo, status (9 for NEL, 8 otherwise), and PowerOn=0.  
   - Count stations linked to that TAR and matching @Loc.  
   - If no TAR found, set @Message to '1'.  
   - If no matching station, set @Message to '10'.  
5. **TAR Detail Retrieval** – If both TAR and station exist, fetch TAR ID, line, access date, and access type.  
6. **Line Check** – If @Line differs from the TAR line, set @Message to '2'.  
7. **TOA Existence Check** –  
   - Look for an existing TOA record for the TAR.  
   - If none, proceed to create a new TOA; otherwise, handle updates.  
8. **New TOA Creation** –  
   - Determine operation date: if current time ≤ cutoff, use yesterday; otherwise today.  
   - Validate that the TAR access date matches the current date (or next day if after cutoff).  
   - Call sp_TAMS_TOA_QTS_Chk with NRIC, access date, line, and possession code; store result in #tmpnric.  
   - Extract InChargeName and InChargeStatus.  
   - If status is InValid and access type is Protection, re‑run the QTS check with the protection code; set final status accordingly.  
   - If final status is InValid, set @Message to '9'.  
   - If valid, insert a new record into TAMS_TOA with encrypted NRIC, default values, and the determined operation date.  
   - Capture the new TOAID.  
   - Insert an audit record into TAMS_TOA_Audit.  
   - Insert a party record into TAMS_TOA_Parties marking the InCharge.  
   - Set @Message to '99' (BookIn).  
9. **Existing TOA Handling** –  
   - Verify that the provided NRIC matches the InChargeNRIC of the existing TOA. If not, set @Message to '5'.  
   - Retrieve the current TOAStatus.  
   - If status is 0 (pending), update the operation date using the same cutoff logic and set @Message to '99'.  
   - If status is 3, 2, or 1:  
     - If 2 or 1, set @Message to '98' (AddParties).  
     - If 3, set @Message to '97' (BookOut).  
   - For any other status, set @Message to '8' (Invalid TAR Status).  
10. **Error Handling** – If any error occurs, set @Message to 'ERROR INSERTING INTO TAMS_TOA' and roll back if the transaction was internally started.  
11. **Commit/Rollback** – Commit the transaction if it was internally started; otherwise leave it to the caller. Return @Message.

### Data Interactions
* **Reads** – TAMS_Parameters, TAMS_TAR, TAMS_Station, TAMS_TAR_Station, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties.  
* **Writes** – TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, temporary table #tmpnric.