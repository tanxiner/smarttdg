# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_CC

### Purpose
This stored procedure updates the TVF acknowledge status for a specific station based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The user ID. |
| @StationId | int | The station ID. |
| @TVFMode | varchar(10) | The TVF mode. |
| @TVFDirection1 | bit | The first direction of the TVF. |
| @TVFDirection2 | bit | The second direction of the TVF. |

### Logic Flow
The procedure starts by beginning a transaction. It then updates the TAMS_TVF_Acknowledge table with the provided parameters for the specified station and operation date. If an update is successful, it inserts a new record into the TAMS_TVF_Acknowledge_Audit table with the updated information.

If any errors occur during the procedure, it catches the error message and rolls back the transaction to maintain data consistency.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge