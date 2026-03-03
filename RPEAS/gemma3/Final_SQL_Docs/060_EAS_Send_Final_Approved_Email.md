# Procedure: EAS_Send_Final_Approved_Email

### Purpose
This procedure initiates the sending of a final approval email notification to relevant stakeholders after a form has been approved.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form that has been approved. |
| @p_FormUserID | varchar(15) | The user ID of the user who initiated the form. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure begins by setting all email-related variables to empty strings and zero. It also sets the URL to be used in the email.
2.  **Retrieve Subject:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Get Sender Detail:** The sender detail (currently set to 'REAS') is retrieved from a configuration.
4.  **Get Approver Information:** The name and user ID of the final approver are retrieved from the `EAS_Form_Approve_Lvl` and `EAS_USER` tables based on the `@p_FormGuid`.
5.  **Retrieve To Lists:** The email recipient list is populated by combining email addresses from the `EAS_Form_Approve_Lvl` table (for those already passed through approval levels) and the `EAS_USER` table (for PA users).
6.  **Email Content Construction:** The email body is constructed, including the subject line and a message indicating the form has been approved by the final approver.  The URL is included in the email body, directing recipients to a specific page for viewing the form.
7.  **Error Handling:** The procedure checks if any of the critical email components (subject, recipient list, or email body) are empty. If any are empty, an error message is raised, and the procedure terminates.
8.  **Enqueue Alert Queue:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, and recipient list. This effectively queues the email for delivery.
9.  **Cleanup:** After the email queue is enqueued, the email-related variables are reset to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None