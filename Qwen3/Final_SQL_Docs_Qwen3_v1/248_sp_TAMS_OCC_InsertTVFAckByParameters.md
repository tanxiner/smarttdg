# Procedure: sp_TAMS_OCC_InsertTVFAckByParameters

### Purpose
This stored procedure performs an insert operation into the TAMS_TVF_Acknowledge table, creating a new record for TVF acknowledgement. It also updates existing records and inserts audit logs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Date of the operation |
| @AccessDate | datetime | Date of access |
| @UserID | int | ID of the user performing the action |
| @StationId | int | ID of the station involved |
| @TVFMode | varchar(10) | Mode of TVF |
| @TVFDirection1 | bit | Direction 1 of TVF |
| @TVFDirection2 | bit | Direction 2 of TVF |

### Logic Flow
The procedure starts by declaring a new ID variable. It then attempts to execute the following steps within a transaction block:

1. Insert a new record into TAMS_TVF_Acknowledge with the provided parameters.
2. Select the newly generated ID from the inserted record.
3. Update existing records in TAMS_TVF_Acknowledge where TVFMode is 'Select' by setting AcknowledgedBy, AcknowledgedOn, CreatedOn, and CreatedBy to NULL.
4. Insert an audit log for the new record into TAMS_TVF_Acknowledge_Audit.

If any errors occur during this process, the transaction is rolled back; otherwise, it is committed.

### Data Interactions
* Reads: TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* Writes: TAMS_TVF_Acknowledge