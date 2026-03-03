# Procedure: sp_TAMS_Form_Cancel

### Purpose
Cancels a form by removing its main record and any temporary attachments.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the form to cancel (overridden to 0 inside the procedure). |
| @Message  | NVARCHAR(500) | Output message indicating success or error. |

### Logic Flow
1. Initialise variables: set @TARID to 0, clear @ErrorMsg, set @IntrnlTrans to 0.  
2. If no active transaction, mark that the procedure will manage its own transaction and begin a new one.  
3. Delete the record from TAMS_TAR where Id equals @TARID (which is 0).  
4. Delete any temporary attachments from TAMS_TAR_Attachment_Temp where TARId equals @TARID.  
5. If any delete operation caused an error, set @Message to 'ERROR DELETING TAMS_TAR' and jump to the error handling section.  
6. On successful completion, commit the transaction if it was started internally and return @Message.  
7. In the error handling section, roll back the transaction if it was started internally and return @Message.

### Data Interactions
* **Reads:** none  
* **Writes:** deletes from TAMS_TAR, deletes from TAMS_TAR_Attachment_Temp