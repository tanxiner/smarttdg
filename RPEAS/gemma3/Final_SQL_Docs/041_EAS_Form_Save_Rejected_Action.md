# Procedure: EAS_Form_Save_Rejected_Action

### Purpose
This procedure records a form rejection action, updates related form and approval level records, and triggers an email notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form being rejected. |
| @P_Userid | varchar(15) | Identifier of the user initiating the rejection. |
| @P_GroupLvl | int | Level of the group associated with the form. |
| @P_ActionID | int | Identifier for the specific approval action. |
| @P_Status | varchar(50) | The status assigned to the form upon rejection. |
| @P_Remarks | varchar(1000) |  Notes or comments regarding the rejection. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict was detected. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins with a check to ensure the `@P_ErrorMsge` output parameter is initialized to an empty string.
2.  A `TRY...CATCH` block is used to handle potential errors during the process.
3.  Inside the `TRY` block, a transaction is started to ensure atomicity – either all changes are committed, or none are.
4.  The `EAS_Form_Master` table is updated with the specified rejection status, the user who performed the action, and the current date and time. The update is performed using the form's unique identifier (`@P_Guid`).
5.  The `EAS_Form_Approve_Lvl` table is updated with the rejection status, conflict check flag, remarks, the user who performed the action, and the current date and time. The update is performed using the form's unique identifier (`@P_Guid`) and the action identifier (`@P_ActionID`).
6.  A new record is inserted into the `EAS_Form_Log_History` table, capturing the form's unique identifier, the rejection remarks, the action type ('Rejected by'), the user who performed the action, and the current date and time.
7.  The stored procedure `EAS_Send_Rejected_Email` is executed, passing the form's unique identifier, the user identifier, the action identifier, and the output parameter for error messages.
8.  If the transaction completes successfully, the transaction is committed.
9.  If any error occurs within the `TRY` block, the `CATCH` block is executed.
10. The `CATCH` block captures the error message using `ERROR_MESSAGE()` and stores it in the `@P_ErrorMsge` output parameter.
11. The transaction is rolled back to undo any changes made during the process.
12. Finally, the `@P_ErrorMsge` output parameter is set to the value of `@P_ErrorMsge` if it's not already empty.

### Data Interactions
* **Reads:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History
* **Writes:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History