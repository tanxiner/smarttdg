# Procedure: EAS_Send_ProcdNxtLvl_Email

### Purpose
This stored procedure sends an email notification related to a form approval process, directing recipients to a specific URL for further action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being processed. |
| @p_FormUserID | varchar(15) | The user ID associated with the form. |
| @p_FormLevel | int |  Indicates the level of the form in the approval hierarchy. |
| @p_NextLevel | int |  Specifies the next level in the approval process. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure initializes variables for the email subject, recipient lists (to and CC), email body, alert queue ID, and URL. It also sets the URL to a specific application URL.
2.  **Subject Retrieval:** It retrieves the email subject from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** It retrieves the name of the form's creator from the `EAS_USER` table using the `@p_FormUserID`.
4.  **Supervisor ID Retrieval:** It retrieves the user ID of the supervisor associated with the form from the `EAS_Form_Approve_Lvl` table and `EAS_USER` table.
5.  **Recipient List Retrieval (To and CC):** It retrieves the recipient lists (to and CC) from the `EAS_Form_Approve_Lvl` table, considering the `@p_NextLevel`.  It uses a `CASE` statement to handle empty recipient lists.
6.  **CC List Retrieval (Conditional):** If `@p_NextLevel` is 4, it retrieves the CC list from the `EAS_Form_Approve_Lvl` table and `EAS_USER` table, including users from the `EAS_PA_Supervisor` table.  Otherwise, it retrieves the CC list from the `EAS_Form_Approve_Lvl` table.
7.  **Email Body Construction:** It constructs the email body, including the subject, a message directing recipients to the URL, and the sender's name. It uses the `fn_Encrypt` function to encrypt the user ID and other values for inclusion in the URL.
8.  **Error Handling:** It checks if the subject, to list, or body are empty. If any are empty, it sets the `@p_ErrorMsg` and raises an error, terminating the procedure.
9.  **Email Queueing:** If no errors are detected, it executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, recipient lists (to and CC), a salutation, the constructed email body, the sender's name, and the alert queue ID.
10. **Cleanup:** After the email queueing, it resets the subject, to list, and CC list variables to empty strings, and resets the email body to empty string.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_USER_ROLE`, `EAS_PA_Supervisor`
* **Writes:** `EAlertQ_EnQueue` (inserts a new alert queue entry)