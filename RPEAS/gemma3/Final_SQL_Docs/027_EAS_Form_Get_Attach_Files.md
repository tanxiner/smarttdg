# Procedure: EAS_Form_Get_Attach_Files

### Purpose
This procedure retrieves attachment files associated with a specific form, categorized as either ApprovalDocuments or SupportDocuments.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormGuid | nvarchar(225) | The unique identifier for the form. |

### Logic Flow
The procedure filters attachment documents from the `EAS_Form_Attach_Document` table based on the provided form identifier. It specifically selects documents where the `FormGuid` matches the input `@P_FormGuid`.  The selection includes the document’s unique identifier (`SNO`), the form’s unique identifier (`FormGuid`), the file name (`FileName`), the file type (`FileType`), the URL to access the file (`FileURL`), the file size (`FileSize`), the date and time the file was created (`CreatedOn`), the user who created the file (`Createdby`), the file content itself (`FileContent`), and the file content type (`FileContentType`). The procedure returns all selected attachment documents.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`
* **Writes:** None