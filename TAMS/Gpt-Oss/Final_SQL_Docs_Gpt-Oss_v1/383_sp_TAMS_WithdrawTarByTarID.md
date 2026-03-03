# Procedure: sp_TAMS_WithdrawTarByTarID

### Purpose
Withdraw a TAR record identified by @TarId, recording the action and updating status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | Identifier of the TAR to withdraw |
| @UID | integer | User performing the withdrawal |
| @Remark | nvarchar(1000) | Optional comment for the withdrawal |

### Logic Flow
1. Begin a transaction.  
2. Retrieve the TAR's line number into @Line.  
3. Find the workflow status ID for a 'Withdraw' status on that line and store it in @StatusId.  
4. Get the name of the user identified by @UID into @Name.  
5. Update the TAR record: set its status to @StatusId, store @Remark, record @UID as the withdrawing user, set the withdrawal date to the current time, and update audit fields.  
6. Insert a log entry into TAMS_Action_Log noting the withdrawal, including the user's name and the current date.  
7. Commit the transaction.  
8. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User  
* **Writes:** TAMS_TAR, TAMS_Action_Log