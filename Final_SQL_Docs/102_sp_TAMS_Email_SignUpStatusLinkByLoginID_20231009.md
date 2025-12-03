# Procedure: sp_TAMS_Email_SignUpStatusLinkByLoginID_20231009

### Purpose
Sends a personalized email containing a link to view a user’s sign‑up status when a valid login ID is supplied.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The user’s login identifier to locate the registration record. |
| @Cipher | NVARCHAR(200) | Encrypted identifier appended to the status‑view URL. |

### Logic Flow
1. Verify that a registration record exists for the supplied @LoginID.  
2. If a record is found, retrieve the associated email address into @ToList.  
3. Construct the status‑view URL by concatenating the base web address with @Cipher.  
4. Populate email metadata: sender, system ID, subject, system name, greeting, and empty CC/BCC lists.  
5. Build the email body in three parts:  
   - **Body1**: a table containing a clickable link to the status page.  
   - **Body2**: a closing signature from the System Administrator.  
   - **Body3**: a disclaimer that the message is computer‑generated.  
6. Concatenate Body1, Body2, and Body3 into @Body.  
7. Call the EAlertQ_EnQueue procedure, passing all email components to enqueue the message for delivery.  
8. End the procedure.

### Data Interactions
* **Reads:** `TAMS_Registration` (to fetch the user’s email).  
* **Writes:** None directly; the procedure invokes `EAlertQ_EnQueue`, which enqueues the email into the system’s alert queue.