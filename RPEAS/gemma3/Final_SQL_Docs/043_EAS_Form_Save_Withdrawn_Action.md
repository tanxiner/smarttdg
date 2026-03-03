# Procedure: EAS_Form_Save_Withdrawn_Action

### Purpose
This procedure saves a form as withdrawn, updates related form and approval level records, and triggers an email notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form. |
| @P_Userid | varchar(15) | Identifier of the user initiating the action. |
| @P_GroupLvl | int | Level of the group associated with the form. |
| @P_Status | varchar(50) | The status applied to the form. |
| @P_Remarks | varchar(1000) |  Notes or comments regarding the withdrawal. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict check was performed. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins with a try-catch block to handle potential errors during the process.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  The `EAS_Form_Master` table is updated with the specified `FormStatus`, `UpdatedBy`, and `UpdatedOn` based on the provided `FormGuid`.
4.  The `EAS_Form_Approve_Lvl` table is updated with the ‘Withdrawn’ action, conflict check flag, remarks, `ActionBy`, and `ActionOn` based on the `FormGuid`, `UserID`, and active status.
5.  A record is inserted into the `EAS_Form_Log_History` table, capturing the `FormGuid`, remarks, action type ('Withdrawn by'), `ActionBy`, and `ActionOn`.
6.  The `EAS_Send_Withdrawn_Email` stored procedure is executed, passing the `FormGuid` and `UserID` to send a withdrawal notification email.
7.  If the try block completes without errors, the transaction is committed.
8.  If any error occurs within the try block, the transaction is rolled back, and the error message is captured and stored in the output parameter `@P_ErrorMsge`.

### Data Interactions
* **Reads:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History
* **Writes:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History