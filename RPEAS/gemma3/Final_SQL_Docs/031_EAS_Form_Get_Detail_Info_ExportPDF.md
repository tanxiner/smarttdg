# Procedure: EAS_Form_Get_Detail_Info_ExportPDF

### Purpose
This procedure retrieves detailed information about a form, including its master data, attached documents (approval and support), and approval history, preparing the data for potential PDF export.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |

### Logic Flow
1.  **Retrieve Form Master Data:** The procedure begins by selecting data from the `EAS_Form_Master` table using the provided `@P_Guid`. This selection includes fields like form identifier, document reference number, document type, company, title, form status, vendor name, approved amount, and an active flag.
2.  **Retrieve Approval Documents:** The procedure then retrieves approval-related documents from the `EAS_Form_Attach_Document` table where the `FileType` is ‘ApprovalDoc’ and the `FormGuid` matches the input `@P_Guid`. It selects fields such as document sort order, document identifier, filename, file type, file URL, file size, creation date, creator, file content, and file content type.
3.  **Retrieve Support Documents:**  The procedure retrieves support-related documents from the `EAS_Form_Attach_Document` table where the `FileType` is ‘SupportDoc’ and the `FormGuid` matches the input `@P_Guid`. It selects fields such as document sort order, document identifier, filename, file type, file URL, file size, creation date, creator, file content, and file content type.
4.  **Retrieve Approval History:** The procedure retrieves the approval history associated with the form. It joins the `EAS_Form_Approve_Lvl` table with the `EAS_Form_Log_History` table based on the `FormGuid` and `ActionBy` columns. This join captures approval-level information, including the user who performed the action, the action date, and any associated remarks. The output includes the user's name, department, design, action, action date, remarks, and the role associated with the approval level.
5.  **Combine Results:** The results from the three sections (form master, approval documents, and approval history) are combined into a single result set. The approval history is ordered by the action date and action by.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_Form_Attach_Document`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
*   **Writes:** None