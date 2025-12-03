# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_PFR

The procedure updates TVF acknowledge records based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The ID of the user performing the action. |
| @StationId | int | The ID of the station. |
| @TVFMode | varchar(10) | The mode of TVF. |
| @TVFDirection1 | bit | The direction of TVF 1. |
| @TVFDirection2 | bit | The direction of TVF 2. |

### Logic Flow
The procedure first attempts to execute the update operation within a transaction block. If successful, it updates the TAMS_TVF_Acknowledge table with the provided values and commits the transaction. If an error occurs during this process, the transaction is rolled back.

1. The procedure starts by beginning a new transaction.
2. It then selects the records from TAMS_TVF_Acknowledge that match the specified StationId, OperationDate, and AccessDate.
3. For each matching record, it updates the TVFMode, TVFDirection1, and TVFDirection2 fields with the provided values.
4. The procedure also updates the OperatedBy field with the @UserID value and sets the TVFOnTime to the current date and time.
5. After updating the records, the procedure inserts a new record into TAMS_TVF_Acknowledge_Audit for each matching record.
6. The audit record includes information about the action performed (O), the ID of the user performing the action (@UserID), the current date and time (GETDATE()), and other relevant fields.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge