# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_CC

### Purpose
Updates a TVF acknowledge record for a specific station and dates, records verification details, and logs the change in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Target operation date for the record to update |
| @AccessDate | datetime | Target access date for the record to update |
| @UserID | int | Identifier of the user performing the update |
| @StationId | int | Identifier of the station whose record is updated |
| @TVFMode | varchar(10) | New TVF mode value |
| @TVFDirection1 | bit | New TVF direction 1 flag |
| @TVFDirection2 | bit | New TVF direction 2 flag |

### Logic Flow
1. Begin a transaction.  
2. Update the row in **TAMS_TVF_Acknowledge** that matches the supplied `@StationId`, `@OperationDate`, and `@AccessDate`.  
   - Set `TVFMode`, `TVFDirection1`, `TVFDirection2` to the supplied values.  
   - Record the verifier (`VerifiedBy = @UserID`) and timestamps (`VerifiedOn`, `UpdatedOn`) and the updater (`UpdatedBy = @UserID`).  
3. Insert a new audit record into **TAMS_TVF_Acknowledge_Audit**.  
   - Capture the action metadata: `ActionBy = @UserID`, `ActionOn = GETDATE()`, `AuditAction = 'V'`.  
   - Copy all columns from the updated **TAMS_TVF_Acknowledge** row into the audit row.  
4. Commit the transaction.  
5. If any error occurs, print the error message and roll back the transaction.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge  
* **Writes:** TAMS_TVF_Acknowledge (update), TAMS_TVF_Acknowledge_Audit (insert)