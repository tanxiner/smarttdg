# Procedure: EAS_Send_Approval_Email_Reminder

### Purpose
This stored procedure sends a reminder email to approvers in an EAS form, prompting them to review and approve the form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages. |

### Logic Flow
The stored procedure `EAS_Send_Approval_Email_Reminder` initiates a process to send a reminder email to individuals involved in the approval workflow of an EAS form.

1.  **Initialization:** The procedure begins by setting default values for variables such as the email subject, recipient lists, and email body. It also initializes the alert queue ID and URL.

2.  **Form Iteration:** The procedure then uses a cursor to iterate through all active EAS forms that have not been closed, rejected, or withdrawn. The cursor selects forms based on their status.

3.  **Pending Day Calculation:** For each form, the procedure calculates the number of days the form has been pending approval using the `EAS_Form_Pending_NODays` function.

4.  **Reminder Email Trigger:** If the pending days exceed 2, the procedure proceeds to generate the reminder email.

5.  **Email Content Generation:** The procedure constructs the email content, including the subject line ("The above subject matter refer. For your approval please."), a link to the form, and the sender's name. The link directs the recipient to the form for review and action.

6.  **Recipient List Population:** The procedure populates the recipient lists (To and CC) by retrieving the relevant information from the `EAS_Form_Approve_Lvl` table. It identifies the approvers based on their level in the approval hierarchy.  It also identifies the PA Supervisor.

7.  **URL Construction:** The procedure constructs the URL for the email, incorporating the form's GUID, the user ID of the approver, and an action code.

8.  **Email Queueing:** Finally, the procedure uses the `EAlertQ_EnQueue` procedure to queue the email for sending. This function sends the email with the generated content and recipient lists.

9.  **Error Handling:** If any error occurs during the process (e.g., missing data), the procedure sets the `@p_ErrorMsg` output parameter and raises an error.

---