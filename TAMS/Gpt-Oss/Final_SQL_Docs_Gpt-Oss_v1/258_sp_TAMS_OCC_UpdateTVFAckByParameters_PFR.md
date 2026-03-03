# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_PFR

### Purpose
Updates a TVF acknowledgment record for a specific station and timestamps, then logs the change in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Identifier for the operation date of the acknowledgment record |
| @AccessDate | datetime | Identifier for the access date of the acknowledgment record |
| @UserID | int | User performing the operation |
| @StationId | int | Identifier for the station whose record is updated |
| @TVFMode | varchar(10) | New TVF mode value |
| @TVFDirection1 | bit | New value for the first TVF direction flag |
| @TVFDirection2 | bit | New value for the second TVF direction flag |

### Logic Flow
1. Begin a transaction.  
2. Update the `TAMS_TVF_Acknowledge` row that matches the supplied `@StationId`, `@OperationDate`, and `@AccessDate`, setting the TVF mode and direction flags, recording the operator and timestamps.  
3. Insert a new audit row into `TAMS_TVF_Acknowledge_Audit` capturing the state of the updated record, including the operator, action type, and all relevant fields.  
4. Commit the transaction.  
5. If any error occurs, print the error message and roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_TVF_Acknowledge` (to retrieve the updated row for audit insertion)  
* **Writes:** `TAMS_TVF_Acknowledge` (update), `TAMS_TVF_Acknowledge_Audit` (insert)