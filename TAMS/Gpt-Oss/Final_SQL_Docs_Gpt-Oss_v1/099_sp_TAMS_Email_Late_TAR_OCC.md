# Procedure: sp_TAMS_Email_Late_TAR_OCC

### Purpose
Sends a notification email when a Late TAR is approved, rejected, or cancelled by CC, including remarks and a link to the TAR form.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | INTEGER       | Identifier of the TAR record (unused in current logic). |
| @TARStatus| NVARCHAR(20)  | Current status of the TAR (Approved, Rejected, Cancelled). |
| @TARNo    | NVARCHAR(50)  | TAR reference number used in the email subject and body. |
| @Remarks  | NVARCHAR(1000)| Optional remarks to include in the email body. |
| @ToSend   | NVARCHAR(1000)| Comma‑separated list of email recipients. |
| @Message  | NVARCHAR(500) OUTPUT | Status message returned to the caller (empty on success, error text on failure). |

### Logic Flow
1. Initialise an internal transaction flag (`@IntrnlTrans`) to 0.  
2. If no active transaction exists, set the flag to 1 and begin a new transaction.  
3. Reset the output message to an empty string.  
4. Declare and initialise variables for email components: sender, system ID, subject, greeting, recipient lists, separators, and body sections.  
5. Construct the email subject as “Late TAR {TARNo} has been {TARStatus} by CC”.  
6. Build the first body section (`@Body1`) with a table containing:  
   - A status‑specific line indicating whether the TAR was approved, rejected, or cancelled.  
   - The remarks supplied by the caller.  
7. Build the second body section (`@Body2`) with:  
   - A link to the TAR form login page.  
   - A closing signature from the System Administrator.  
8. Build the third body section (`@Body3`) with a disclaimer that the email is computer‑generated and should not be replied to.  
9. Concatenate the three body sections into a single body string (`@Body`).  
10. Call the helper procedure `EAlertQ_EnQueue` to enqueue the email, passing all constructed parameters.  
11. If the call to `EAlertQ_EnQueue` returns an error, set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to the error handling section.  
12. On normal completion, commit the transaction if it was started internally and return the (empty) message.  
13. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** None.  
* **Writes:** Inserts a record into the alert queue (via `EAlertQ_EnQueue`), which ultimately writes to `TAMS_TAR`.