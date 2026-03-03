# Procedure: sp_api_send_sms

### Purpose
This stored procedure sends an SMS message to a list of contacts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @contactno | nvarchar(MAX) | The contact numbers to send the SMS to, separated by commas. |
| @subject | nvarchar(500) | The subject of the SMS message. |
| @msg | nvarchar(MAX) | The content of the SMS message. |
| @ret | nvarchar(5) output | The return value indicating whether the operation was successful (0 = success, 1 = failure). |

### Logic Flow
The procedure starts by declaring variables and setting up a cursor to iterate over the contact numbers. It then fetches each contact number from the list, appends it to a string `@DerContactNo`, and executes an external stored procedure `SMSEAlertQ_EnQueue` to send the SMS message to all contacts in the list.

### Data Interactions
* **Reads:** [dbo].[SPLIT] table (explicitly selected)
* **Writes:** None