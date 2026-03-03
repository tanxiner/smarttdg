# Procedure: sp_TAMS_CancelTarByTarID

The purpose of this stored procedure is to cancel a TAR (TARWFStatus) by updating its status and logging the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be cancelled. |
| @UID | integer | The user ID who is cancelling the TAR. |

### Logic Flow

1. The procedure starts by declaring variables for the line, status ID, and name.
2. It then attempts to start a transaction and begins a new block of code within it.
3. Within this block, it selects the line from TAMS_TAR where the Id matches @TarId.
4. It then selects the status ID from TAMS_WFStatus where the line matches the one selected in step 3, and the WFType is 'TARWFStatus' and the WFStatus is 'Cancel'.
5. Next, it selects the name of the user who is cancelling the TAR from TAMS_User where the userid matches @UID.
6. The procedure then updates the TAR status ID in TAMS_TAR to match the one selected in step 4, where the Id is @TarId.
7. After updating the TAR status, it inserts a new log entry into TAMS_Action_Log with details of the cancellation action.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** TAMS_TAR, TAMS_Action_Log