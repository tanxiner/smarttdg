# Procedure: EAS_Form_Save_Approved_Action

### Purpose
This procedure updates form master data and form approval level data, logs the approval action, and optionally sends approval and final approval emails based on the form's status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form being updated. |
| @P_Userid | varchar(15) | Identifier for the user performing the action. |
| @P_GroupLvl | int | Level of the user submitting the form. |
| @P_ActionID | int | Identifier for the approval level record. |
| @P_Status | varchar(50) | The status of the form after approval. |
| @P_Remarks | varchar(1000) | Additional remarks related to the approval. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict check was performed. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  Initialize the `@P_ErrorMsge` output parameter to an empty string.
2.  Determine the appropriate descriptive text based on the `@P_GroupLvl` value for logging the action.
3.  Begin a transaction to ensure atomicity of operations.
4.  Update the `EAS_Form_Master` table, setting the `FormStatus` to the provided `@P_Status`, updating the `UpdatedBy` field with the `@P_Userid`, and recording the update timestamp using `GETDATE()`. This update is performed where the `FormGuid` matches the input `@P_Guid`.
5.  Update the `EAS_Form_Approve_Lvl` table, setting the `Action` to 'Approved', the `ChkDeclareConflit` flag to the provided `@P_ChkConflict`, the `Remarks` field to the `@P_Remarks` value, the `ActionBy` field to the `@P_Userid`, and the `ActionOn` timestamp to `GETDATE()`. This update is performed where the `FormGuid` matches the input `@P_Guid` and the `id` field matches the input `@P_ActionID`.
6.  Insert a record into the `EAS_Form_Log_History` table, logging the form's approval action, the descriptive text determined by `@P_GroupLvl`, the `@P_Userid`, and the timestamp `GETDATE()`.
7.  If the `FormStatus` is not 'Closed', execute the stored procedure `EAS_Send_Approval_Email` with the form's GUID, the user ID, and the `@P_ErrorMsge` output parameter.
8.  If the `FormStatus` is 'Closed', execute the stored procedure `EAS_Send_Final_Approved_Email` with the form's GUID, the user ID, and the `@P_ErrorMsge` output parameter.
9.  Commit the transaction.
10. If an error occurs, rollback the transaction and set the `@P_ErrorMsge` with the error message.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
* **Writes:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`