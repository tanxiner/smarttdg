# Procedure: sp_TAMS_Email_SignUpStatusLinkByLoginID

### Purpose
Sends a personalized email containing a link to view a user’s sign‑up status based on the supplied login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | Identifier used to locate the user’s registration record and email address. |
| @Cipher | NVARCHAR(200) | Token appended to the sign‑up status URL to uniquely identify the user. |

### Logic Flow
1. Verify that a registration record exists for the supplied @LoginID.  
2. If a record is found, retrieve the user’s email address into @ToList.  
3. Construct a URL that points to the sign‑up status page, embedding @Cipher as the query parameter.  
4. Initialize email metadata: sender, system ID, subject, system name, greeting, and empty CC/BCC lists.  
5. Build the email body in three parts:  
   - A table containing a clickable link to the sign‑up status page.  
   - A closing table with a “Regards” signature.  
   - A footer table with a disclaimer that the email is computer‑generated.  
6. Concatenate the body parts into @Body.  
7. Call the EAlertQ_EnQueue procedure, passing all email components to enqueue the message for delivery.  
8. End the procedure; no further action is taken if no registration record exists.

### Data Interactions
* **Reads:** TAMS_Registration  
* **Writes:** Enqueues an email via the EAlertQ_EnQueue procedure (no direct table modifications).