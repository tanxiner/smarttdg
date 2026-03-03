# Procedure: EAS_Form_Get_Detail_Info

### Purpose
This procedure retrieves comprehensive details related to a form, including its master data, attachments, approver information, log history, and any withdrawn information, based on a provided GUID and user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_UserID | varchar(15) | The user ID for context-specific data retrieval. |

### Logic Flow
1.  **Retrieve Form Master Data:** The procedure begins by selecting key details from the `EAS_Form_Master` table using the provided `@P_Guid`. This includes fields like document number, type, company, title, creation date, status, and approved amount. It also calls stored procedures `EAS_Form_Get_Approver_Name` to retrieve approver names based on the form GUID and level.  The `EAS_Form_Get_Form_Level` stored procedure is used to retrieve form level information based on the user ID.
2.  **Retrieve Attachments:** The procedure then executes the `EAS_Form_Get_Attach_Files` stored procedure, which likely retrieves associated document files linked to the form.
3.  **Retrieve Approver List:** The procedure selects data from the `EAS_Form_Approve_Lvl` table, joining it with the `EAS_Form_Log_History` table to capture approver actions and history. It uses the `@P_Guid` to filter the data. The `EAS_User_Name` stored procedure is called to display user names based on the user ID. The logic determines the status (Complete/Not Complete) and the true/false status of conflict declarations. It also uses the `GroupLevel` to determine the approver description.
4.  **Retrieve Current User Action:** The procedure selects the most recent action from the `EAS_Form_Approve_Lvl` table, filtering by the `@P_Guid` and ensuring it's the most recent action.
5.  **Retrieve Log History:** The procedure retrieves log history entries from the `EAS_Form_Log_History` table, filtering by the `@P_Guid`. It concatenates the action and the user name involved in the action to create a combined log remark.
6.  **Retrieve Withdrawn Information:** The procedure retrieves information related to withdrawn entries from the `EAS_Form_Log_History` table, filtering by the action being 'Withdrawn' and the `@P_Guid`.

### Data Interactions
* **Reads:**
    * `EAS_Form_Master`
    * `EAS_Form_Log_History`
    * `EAS_Form_Approve_Lvl`
    * `EAS_Form_Get_Attach_Files`
* **Writes:** None