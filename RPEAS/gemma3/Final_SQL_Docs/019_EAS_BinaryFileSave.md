# Procedure: EAS_BinaryFileSave

### Purpose
This procedure saves a binary file associated with a specific form, updating the corresponding record in the EAS_Form_Attach_Document table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FileID | int | The unique identifier for the file. |
| @p_FileRefNo | varchar(225) | The reference number identifying the form. |
| @p_FileContent | varbinary(max) | The binary data of the file. |
| @p_FileType | varchar(500) | The type of the file. |
| @p_ErrorMsg | varchar(500) | An output parameter to store any error messages. |

### Logic Flow
The procedure updates a record within the EAS_Form_Attach_Document table. It sets the `FileContent` column to the provided binary file data. Simultaneously, it updates the `FileContentType` column with the specified file type. The update is performed based on a matching `ID` value (representing the file) and a `FormGuid` value (representing the form). The `ErrorMsg` output parameter is intended to capture any potential errors during the update process, although it is not explicitly used within the procedure's logic.

### Data Interactions
* **Reads:** EAS_Form_Attach_Document
* **Writes:** EAS_Form_Attach_Document