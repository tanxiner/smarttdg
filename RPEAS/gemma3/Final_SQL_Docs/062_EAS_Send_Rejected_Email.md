# Procedure: EAS_Send_Rejected_Email

### Purpose
This stored procedure sends a rejection email notification to relevant parties involved in an EAS form approval process, including supervisors and users at different approval levels, providing a link to view the rejected form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the EAS form being rejected. |
| @p_FormUserID | varchar(15) | The user ID of the user who initiated the rejection. |
| @p_RejectID | int | The ID of the rejection record. |
| @p_ErrorMsg | output |  An output parameter to store any error messages encountered during the email sending process. |

### Logic Flow
1.  **Initialization:** The procedure initializes several variables, including email subject, recipient list, CC list, email body, alert queue ID, URL, sender detail, and error message. The URL is set to a specific RPEAS login page.
2.  **Subject Retrieval:** The procedure retrieves the email subject from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** The procedure retrieves the email sender's name from the `EAS_USER` table using the `@p_FormUserID`.
4.  **Max Approval Level Determination:** The procedure determines the maximum approval level associated with the form using the `EAS_Form_Approve_Lvl` table and the `@p_RejectID`.
5.  **Recipient List Construction:**
    *   **If Max Approval Level Matches Form Level:** The procedure constructs the recipient list by selecting email addresses from `EAS_Form_Approve_Lvl` for all approval levels up to the maximum level, including supervisors via a join with `EAS_USER` and PA supervisors.
    *   **If Max Approval Level Differs:** The procedure constructs the recipient list by selecting email addresses from `EAS_Form_Approve_Lvl` for all approval levels up to the `@p_RejectID`.
6.  **Email Content Assembly:** The email body is constructed, including a standard rejection message and a hyperlink to the RPEAS login page, incorporating the form GUID, user ID, and an encryption function for the user ID.
7.  **Error Handling:** The procedure checks if the subject, recipient list, or email body are empty. If any are empty, it sets the `@p_ErrorMsg` and raises an error, preventing the email from being sent.
8.  **Email Queueing:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, sender name, recipient list, CC list, BCC list, and the alert queue ID. This effectively queues the email for delivery.
9.  **Variable Reset:** After the email queueing, the procedure resets the initialized variables.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_USER_ROLE`, `EAS_PA_Supervisor`
*   **Writes:** `EAlertQ_EnQueue` (queueing the email)