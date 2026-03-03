# Procedure: sp_TAMS_WithdrawTarByTarID

### Purpose
This stored procedure performs a withdrawal of a TAR (Tender And Request) by updating its status and recording the action in the TAMS_Action_Log table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be withdrawn. |
| @UID | integer | The user ID of the person withdrawing the TAR. |
| @Remark | nvarchar(1000) | A remark or comment for the withdrawal. |

### Logic Flow
1. The procedure starts by declaring variables to store line numbers, status IDs, and names.
2. It then attempts to begin a transaction and execute the following steps within it:
   - Selects the line number from TAMS_TAR where the TAR ID matches @TarId.
   - Retrieves the status ID for the selected line from TAMS_WFStatus based on certain conditions.
   - Finds the user name associated with the provided UID in TAMS_User.
3. If all previous steps are successful, it updates the TAR's status and records the withdrawal action in TAMS_Action_Log:
   - Updates TARStatusId to the retrieved status ID.
   - Sets WithdrawRemark to the provided remark.
   - Records the withdrawal by setting WithdrawBy to @UID and WithdrawDate to the current date and time.
4. If any step fails, it rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** TAMS_TAR (updated), TAMS_Action_Log