# Procedure: EAS_Send_Approval_Email

### Purpose
This stored procedure sends an email notification to relevant parties to initiate an approval process for a form, providing a direct link to the form for review and action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being approved. |
| @p_FormUserID | varchar(15) | The ID of the user who initiated the form. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1. **Initialization:** The procedure initializes all email-related variables to empty strings or zero values. It also sets the URL to a default RPEAS login page.
2. **Subject Retrieval:** It retrieves the subject line for the email from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3. **Current User Record:** It selects the ID of the current user record from the `EAS_Form_Approve_Lvl` table, which is the first record in the approval chain.
4. **Determine Maximum Level:** It identifies the highest level in the approval chain from the `EAS_Form_Approve_Lvl` table using the `@p_FormGuid`.
5. **Get Email Sender Detail:** It retrieves the sender's name from the `EAS_USER` table using the `@p_FormUserID`.
6. **Get Supervisor ID:** It retrieves the supervisor ID from the `EAS_Form_Approve_Lvl` and `EAS_USER` tables, based on the approval hierarchy.
7. **Get To Lists:** It selects the email addresses for the approvers, starting with the current user record and potentially including the supervisor. It uses the `EAS_Form_Approve_Lvl` and `EAS_USER` tables to determine the email addresses.
8. **Get CC Lists:** It determines the CC email addresses. If the next action is at level 4, it also includes the PA (Personal Assistant) in the CC list. It uses the `EAS_Form_Approve_Lvl` and `EAS_USER` tables to identify the relevant users.
9. **Email Content Construction:** It constructs the email body, including a standard greeting, a request for approval, and a hyperlink to the form. The hyperlink includes the form GUID, the user ID, and an encryption of the user's name.
10. **Error Handling:** It checks if the subject, to list, or body are empty. If any of these are empty, it sets the `@p_ErrorMsg` and raises an error, preventing the email from being sent.
11. **Email Queueing:** If no errors are detected, it executes the `EAlertQ_EnQueue` stored procedure, which enqueues the email for delivery. This procedure sends the email using the constructed subject, to list, CC list, body, and sender details.
12. **Cleanup:** After the email queueing, it resets the email-related variables to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None