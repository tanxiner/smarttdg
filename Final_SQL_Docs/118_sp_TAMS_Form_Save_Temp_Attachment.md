# Procedure: sp_TAMS_Form_Save_Temp_Attachment

### Purpose
Saves a temporary attachment for a TAR request when no duplicate exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | Identifier of the TAR record |
| @TARAccessReqId | INTEGER | Identifier of the TAR access request |
| @FileName | NVARCHAR(50) | Name of the file being uploaded |
| @FileType | NVARCHAR(50) | MIME type of the file |
| @FileUpload | VARBINARY(MAX) | Binary content of the uploaded file |

### Logic Flow
1. Initialise a return string `@ret` to an empty value.  
2. Begin a TRY block and start a database transaction.  
3. Execute a `SELECT COUNT(*)` on `TAMS_TAR_Attachment_Temp` filtering by `TARId` and `TARAccessReqId`.  
4. If the count is zero, perform an `INSERT` into `TAMS_TAR_Attachment_Temp` with the supplied parameters.  
5. Commit the transaction.  
6. If any error occurs, enter the CATCH block:  
   - Print a diagnostic message.  
   - Return the error number and message.  
   - Roll back the transaction.  
   - Set `@ret` to the string `'Errror'`.  
7. After the TRY/CATCH, output the value of `@ret` as `ReturnValue`.

### Data Interactions
* **Reads:** `TAMS_TAR_Attachment_Temp` (via `SELECT COUNT(*)`)  
* **Writes:** `TAMS_TAR_Attachment_Temp` (via `INSERT`)