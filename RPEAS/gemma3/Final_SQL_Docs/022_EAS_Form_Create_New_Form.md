# Procedure: EAS_Form_Create_New_Form

### Purpose
This procedure creates a new form record within the EAS system, including its master data and initial approval levels.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_doctype | varchar(50) | Specifies the type of form being created. |
| @p_company | varchar(200) | Indicates the company associated with the form. |
| @p_Title | varchar(500) |  Stores the title or name of the form. |
| @p_Vendor | varchar(200) |  Represents the vendor associated with the form. |
| @p_Amt | decimal(18,2) |  Holds the amount related to the form. |
| @p_LoginID | varchar(15) |  The login ID of the user creating the form. |
| @p_formguid | nvarchar(225) | Output parameter containing the unique GUID for the newly created form. |
| @p_docruno | varchar(4) | Output parameter containing the run number assigned to the form. |
| @p_errormsg | varchar(500) | Output parameter to store any error messages that occur during the process. |

### Logic Flow
1.  **GUID Generation:** A unique GUID (Globally Unique Identifier) is generated and stored in the @p_guid variable.
2.  **Run Number Retrieval/Creation:**
    *   The procedure checks if a record already exists in the `EAS_Form_RefNo_Cntl` table with the specified year and prefix.
    *   If no record exists, it inserts a new record into this table, assigning a run number starting from 1.
    *   If a record does exist, it retrieves the next available run number from the table.
3.  **Form Master Record Creation:**
    *   The run number is converted to a string and assigned to the @p_docruno output parameter.
    *   A new record is inserted into the `EAS_Form_Master` table, populating fields with the generated GUID, retrieved run number, form type, company, title, status, vendor, amount, and active flag. The creation and update timestamps are set to the current login ID.
4.  **Approval Level Records Creation:**
    *   The procedure then inserts records into the `EAS_Form_Approve_Lvl` table to define the approval levels for the form.
    *   It inserts records for levels 1, 2, 3, and 4, depending on the values of the @p_PreparBy1, @p_SubmitBy, @p_SubmitThru, and @p_Approver parameters.
    *   Each approval level record specifies the form GUID, approval level, user ID, re-route type, remarks, conflict check flag, action, active flag, action by, action on, and creation details.
5.  **Log History Entry:** Finally, a record is inserted into the `EAS_Form_Log_History` table, documenting the preparation of the form by the user's login ID and timestamp.
6.  **Error Handling:** If any error occurs during the process, the error message is captured and stored in the @p_errormsg output parameter.

### Data Interactions
*   **Reads:** `EAS_Form_RefNo_Cntl`, `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
*   **Writes:** `EAS_Form_RefNo_Cntl`, `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`