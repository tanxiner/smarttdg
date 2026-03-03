# Procedure: EAS_Send_ReRoute_Email

### Purpose
This stored procedure initiates the sending of an email alert regarding a re-routed form, including relevant details and a direct link for action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being re-routed. |
| @p_FormUserID | varchar(15) | The user ID associated with the form. |
| @p_FormLevel | int | The level of the form approval process. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure initializes all email related variables to empty strings or zero values. This includes the subject, to lists, CC lists, body, and alert queue ID. It also sets the URL to a specific application URL.
2.  **Subject Retrieval:** The procedure retrieves the form title from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** The procedure retrieves the name of the user associated with the form from the `EAS_USER` table using the `@p_FormUserID`.
4.  **To Lists Retrieval:** The procedure retrieves the "To" list by querying the `EAS_Form_Approve_Lvl` and `EAS_USER` tables. It constructs the list by concatenating email addresses, handling the case where the list is empty. It also retrieves the `userid` and `name` from the `EAS_USER` table.
5.  **CC Lists Retrieval:** Similar to the "To" list, the procedure retrieves the "CC" list by querying the `EAS_Form_Approve_Lvl` and `EAS_USER` tables, concatenating email addresses. It also ensures the user ID is not included in the CC list.
6.  **Email Content Construction:** The procedure constructs the email body, including a message indicating the re-routing by the sender and a hyperlink to the form for action. The hyperlink includes the form GUID, encrypted user ID, and an action flag.
7.  **Error Handling:** The procedure checks if the subject, to list, or body are empty. If any of these are empty, it sets the `@p_ErrorMsg` and raises an error, terminating the procedure.
8.  **Email Queue Execution:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, to lists, CC lists, BCC list, separator, alert queue ID, and sender name as parameters.
9.  **Variable Reset:** After the email queue execution, the procedure resets all email related variables to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`
* **Writes:** `EAlertQ_EnQueue` (writes to the email queue)