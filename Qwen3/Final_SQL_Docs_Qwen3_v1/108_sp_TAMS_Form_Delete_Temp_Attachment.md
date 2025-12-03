# Procedure: sp_TAMS_Form_Delete_Temp_Attachment

### Purpose
This stored procedure deletes a temporary attachment record from the TAMS_TAR_Attachment_Temp table based on the provided TARId and TARAccessReqId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | The ID of the attachment to be deleted. |
| @TARAccessReqId | INTEGER | The access request ID associated with the attachment to be deleted. |

### Logic Flow
1. The procedure starts by declaring a variable @ret to store the return value.
2. It then attempts to begin a transaction, which will ensure that either all changes are committed or none are if an error occurs.
3. Within the transaction block, it deletes the specified attachment record from the TAMS_TAR_Attachment_Temp table based on the provided TARId and TARAccessReqId.
4. If the deletion is successful, the procedure commits the transaction, making the changes permanent.
5. If any errors occur during the deletion process, the procedure catches the exception, prints an error message, rolls back the transaction to maintain data consistency, and sets @ret to 'Error'.
6. Finally, the procedure selects the value of @ret as the return value.

### Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp table
* **Writes:** TAMS_TAR_Attachment_Temp table