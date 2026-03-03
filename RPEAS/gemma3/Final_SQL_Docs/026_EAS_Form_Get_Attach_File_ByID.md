# Procedure: EAS_Form_Get_Attach_File_ByID

### Purpose
This procedure retrieves information about a specific attachment file associated with a form, based on the form’s unique identifier and the attachment’s unique identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormGuid | nvarchar(225) | The unique identifier for the form. |
| @P_FileID | int | The unique identifier for the attachment file. |

### Logic Flow
The procedure begins by selecting data from the `EAS_Form_Attach_Document` table. The selection is filtered based on two criteria: the `FormGuid` column must match the input parameter `@P_FormGuid`, and the `ID` column must match the input parameter `@P_FileID`. The selected data includes the attachment’s `SNO`, `FormGuid`, `FileName`, `FileType`, `FileURL`, `FileSize`, `CreatedOn`, `Createdby`, `FileContent`, and `FileContentType`.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`
* **Writes:** None