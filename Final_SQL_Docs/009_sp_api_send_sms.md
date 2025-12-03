# Procedure: sp_api_send_sms

### Purpose
Send an SMS message to a list of phone numbers by enqueuing an alert record.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @contactno | nvarchar(MAX) | Comma‑separated list of destination phone numbers. |
| @subject   | nvarchar(500) | Subject line for the SMS alert. |
| @msg       | nvarchar(MAX) | Text of the SMS message. |
| @ret       | nvarchar(5)   | Output flag indicating success (set to '0'). |

### Logic Flow
1. **Initialize variables** – declare identifiers for alert ID, cursor row, value, and a derived contact list.  
2. **Normalize contact list** – append the fixed suffix `,83681010` to the supplied @contactno string.  
3. **Split the contact string** – open a cursor over the table‑valued function `SPLIT` that tokenizes the string by commas.  
4. **Build a clean list** – iterate through each token, concatenating it into @DerContactNo with trailing commas.  
5. **Close cursor** – release cursor resources.  
6. **Enqueue SMS alert** – call `SMSEAlertQ_EnQueue` with:
   - Sender: `TAMSadmin`
   - Subject: @subject  
   - Alert message: @msg  
   - UserId: `TAMSadmin`  
   - SendTo: @DerContactNo  
   - Separator: `,`  
   The procedure returns an @AlertID.  
7. **Set return status** – assign `'0'` to @ret and return it.

### Data Interactions
* **Reads:** `[dbo].[SPLIT]` (table‑valued function)  
* **Writes:** `SMSEAlertQ_EnQueue` (enqueues an SMS alert record)