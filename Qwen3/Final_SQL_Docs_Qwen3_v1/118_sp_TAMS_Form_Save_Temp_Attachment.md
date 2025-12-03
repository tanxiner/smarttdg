# Procedure: sp_TAMS_Form_Save_Temp_Attachment

### Purpose
This stored procedure saves a temporary attachment to the TAMS database, creating a new record if one does not already exist for the specified TARId and TARAccessReqId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | The ID of the TAR (Temporary Attachment Record) to save. |
| @TARAccessReqId | INTEGER | The ID of the access request for which the attachment is being saved. |
| @FileName | NVARCHAR(50) | The name of the file being uploaded. |
| @FileType | NVARCHAR(50) | The type of file being uploaded (e.g., image, document). |
| @FileUpload | VARBINARY(MAX) | The binary data of the file being uploaded. |

### Logic Flow
1. The procedure checks if a record already exists in TAMS_TAR_Attachment_Temp for the specified TARId and TARAccessReqId.
2. If no record exists, it inserts a new record into TAMS_TAR_Attachment_Temp with the provided file information.
3. Regardless of whether a new record is inserted or not, the procedure commits the transaction.
4. If any error occurs during the execution of the stored procedure, it prints an error message and rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp table
* **Writes:** TAMS_TAR_Attachment_Temp table