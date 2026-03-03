# Procedure: sp_TAMS_OCC_RejectTVFAckByParameters_PFR

### Purpose
Reject a TVF acknowledgment by updating its status and recording the change in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Target operation date for the acknowledgment record |
| @AccessDate | datetime | Target access date for the acknowledgment record |
| @UserID | int | Identifier of the user performing the rejection |
| @StationId | int | Identifier of the station whose acknowledgment is being rejected |
| @TVFMode | varchar(10) | New TVF mode value to apply |
| @TVFDirection1 | bit | New TVF direction 1 value to apply |
| @TVFDirection2 | bit | New TVF direction 2 value to apply |

### Logic Flow
1. Begin a transaction.  
2. Update the row in **TAMS_TVF_Acknowledge** that matches the supplied `@StationId`, `@OperationDate`, and `@AccessDate`.  
   - Set `TVFMode`, `TVFDirection1`, and `TVFDirection2` to the supplied values.  
   - Clear `VerifiedBy` and `VerifiedOn`.  
   - Record the current timestamp in `UpdatedOn` and the user ID in `UpdatedBy`.  
3. Insert a new audit record into **TAMS_TVF_Acknowledge_Audit**.  
   - Use the updated row’s current values as the audit snapshot.  
   - Set `ActionBy` to the user ID, `ActionOn` to the current timestamp, and `AuditAction` to `'R'`.  
4. Commit the transaction.  
5. If any error occurs, print the error message and roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_TVF_Acknowledge` (to capture the updated row for auditing)  
* **Writes:** `TAMS_TVF_Acknowledge` (update), `TAMS_TVF_Acknowledge_Audit` (insert)