# Procedure: sp_TAMS_OCC_InsertTVFAckByParameters

### Purpose
Insert a new TVF acknowledgement record, clear certain fields for “Select” mode, and log the action in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Date of the operation to record |
| @AccessDate | datetime | Date the acknowledgement was accessed |
| @UserID | int | Identifier of the user performing the action |
| @StationId | int | Identifier of the station involved |
| @TVFMode | varchar(10) | Mode of the TVF (e.g., “Select”) |
| @TVFDirection1 | bit | Direction flag 1 |
| @TVFDirection2 | bit | Direction flag 2 |

### Logic Flow
1. Begin a transaction.  
2. Insert a new row into **TAMS_TVF_Acknowledge** using the supplied parameters; set `AcknowledgedBy`, `AcknowledgedOn`, `VerifiedBy`, `VerifiedOn`, `OperatedBy`, `TVFOnTime` to NULL, and populate `AcknowledgedOn`, `CreatedOn` with the current date.  
3. Capture the identity value of the inserted row into `@NewID`.  
4. Update any rows in **TAMS_TVF_Acknowledge** where `TVFMode` equals `'Select'`, setting `AcknowledgedBy`, `AcknowledgedOn`, `CreatedOn`, and `CreatedBy` to NULL.  
5. Insert a new audit record into **TAMS_TVF_Acknowledge_Audit**:  
   - `ActionBy` = `@UserID`  
   - `ActionOn` = current date  
   - `AuditAction` = `'A'` (indicating an insert)  
   - `TVFAckId` = `@NewID`  
   - Copy all other columns from the newly inserted **TAMS_TVF_Acknowledge** row identified by `@NewID`.  
6. Commit the transaction.  
7. If any error occurs, print the error message and roll back the transaction.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge (select for audit)  
* **Writes:** TAMS_TVF_Acknowledge (insert, update), TAMS_TVF_Acknowledge_Audit (insert)