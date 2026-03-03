# Procedure: EAS_Send_Withdrawn_Email

### Purpose
This procedure initiates the process of sending an email notification to relevant parties when a form has been withdrawn, providing a link to view the form details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form that was withdrawn. |
| @p_FormUserID | varchar(15) | The user ID of the form initiator. |
| @p_ErrorMsg | output |  An output parameter to hold any error messages generated during the process. |

### Logic Flow
1.  **Initialization:** The procedure begins by setting default values for all output variables, including the subject, to lists, and the body of the email. It also initializes the alert queue ID and URL.
2.  **URL Setup:** The URL for the RPEAS login page is set to `http://mssqldevpsvr/RPEAS/RPEAS_Login.aspx`.
3.  **Subject Retrieval:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
4.  **Sender Detail Retrieval:** The sender detail is set to 'REAS'.
5.  **Subject Retrieval:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
6.  **To List Population:** The procedure constructs the recipient email list. It first attempts to retrieve emails from the `EAS_Form_Approve_Lvl` table, considering all levels that have passed through the form. If the `p_RejectGroupLevel` is equal to the maximum level, it also includes emails from the PA supervisor list.
7.  **Email Content Construction:** The email body is constructed, stating that the form has been withdrawn. It includes a hyperlink to the RPEAS login page, using the form's GUID and the user ID of the form initiator, along with an action parameter.
8.  **Error Handling:** If the subject, to list, or body are empty after all steps, an error message is set, and the procedure exits.
9.  **Email Queue Execution:** If no errors are encountered, the `EAlertQ_EnQueue` stored procedure is executed, passing the sender detail, subject, body, recipient email list, and sender name. This triggers the actual sending of the email alert.
10. **Variable Reset:** After the email queue execution, the subject, to list, and the body are reset to empty.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None