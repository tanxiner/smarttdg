# Procedure: sp_TAMS_Block_Date_Save

### Purpose
Insert a new block date for a specified line and track type after validating that the date is at least five weeks in the future, not already active, and log the action in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line to block |
| @TrackType | NVARCHAR(50) | Type of track for which the block applies |
| @BlockDate | NVARCHAR(20) | Date string of the block, converted to DATE |
| @BlockReason | NVARCHAR(100) | Reason for blocking |
| @UserLI | NVARCHAR(50) | Login ID of the user performing the operation |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message returned to caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction exists, start a new one and flag that the procedure owns the transaction.
2. **Initialize Message** – Clear the output message variable.
3. **User Identification** – Retrieve the numeric UserID from TAMS_User where LoginId matches @UserLI.
4. **Current and Block Date Metrics** –  
   - Determine the current week number and year.  
   - Convert @BlockDate to a DATE, then determine its week number and year.
5. **Future‑Date Validation** –  
   - If the block year equals the current year, ensure the block week is at least five weeks ahead; otherwise set message code '1'.  
   - If the block year is the next year, adjust the block week by adding 52 and again ensure a five‑week lead; otherwise set message code '2'.  
   - If the block year is earlier than the current year, set message code '3' indicating the date is not in the future.
6. **Duplicate Check** – Query TAMS_Block_TARDate for an active record with the same Line, TrackType, and BlockDate. If found, set message code '4'.
7. **Insert New Block** – If no message code has been set:  
   - Insert a new row into TAMS_Block_TARDate with the supplied values, marking it active and recording timestamps and user IDs.  
   - Capture the new record’s identity value.  
   - Insert a corresponding audit row into TAMS_Block_TARDate_Audit, copying all fields from the newly inserted record and prefixing with UserID, timestamp, and action code 'I'.
8. **Error Check** – If any error flag is set during the procedure, set the message to a generic error string and jump to the error handling section.
9. **Commit or Rollback** –  
   - On normal exit, commit the transaction if it was started by the procedure.  
   - On error, rollback the transaction if it was started by the procedure.  
10. **Return** – Return the message string to the caller.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_Block_TARDate
* **Writes:**  
  - TAMS_Block_TARDate  
  - TAMS_Block_TARDate_Audit

---