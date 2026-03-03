# Procedure: EAS_Form_Update_Binary_File

### Purpose
This procedure updates a document attachment record within the EAS_Form_Attach_Document table with the provided binary file content and associated metadata.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_formguid | nvarchar(225) |  Unique identifier for the form. |
| @p_FileName | nvarchar(255) | Name of the file being attached. |
| @p_FileContentType | nvarchar(50) |  The MIME type of the file. |
| @p_FileContent | varbinary(MAX) | The binary data of the file. |
| @p_errormsg | varchar(500) | Output parameter to hold any error messages. |

### Logic Flow
The procedure begins by initializing an output parameter, @p_errormsg, to an empty string. It then executes a transaction block. Inside this block, it updates a record in the EAS_Form_Attach_Document table. The update sets the FileContent column to the provided binary file data, the FileContentType column to the specified MIME type, and it filters the update to only affect the record where the FormGuid matches the input @p_formguid and the FileName matches the input @p_FileName.  If an error occurs during the update process, the error message is captured and stored in the @p_errormsg output parameter.  The transaction block is implicitly handled, ensuring atomicity.

### Data Interactions
* **Reads:** EAS_Form_Attach_Document
* **Writes:** EAS_Form_Attach_Document