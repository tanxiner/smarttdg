# Procedure: sp_TAMS_Email_Urgent_TAR_20231009

### Purpose
Send an urgent TAR status notification email to the specified recipients.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | INTEGER       | Identifier of the TAR record. |
| @TARStatus| NVARCHAR(20)  | Current status of the TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo    | NVARCHAR(50)  | TAR reference number used in the email subject and body. |
| @Remarks  | NVARCHAR(1000)| Optional remarks to include in the email body. |
| @Actor    | NVARCHAR(100) | Role that performed the status change, used to tailor the subject line. |
| @ToSend   | NVARCHAR(1000)| Comma‑separated list of email addresses to receive the message. |
| @Message  | NVARCHAR(500) OUTPUT | Status message returned by the procedure (empty on success). |

### Logic Flow
1. Initialise an internal transaction flag and start a transaction if none is active.  
2. Reset the output message to an empty string.  
3. Declare and initialise variables for email components: sender, system ID, subject, greeting, recipient lists, separators, and body sections.  
4. Build the email subject:  
   - Prefix with “Urgent TAR \<TARNo\> has been \<TARStatus\> by”.  
   - Append the actor’s role (Applicant HOD, TAP HOD, Power, TAP Verifier, TAP Approver, OCC) if it matches one of the predefined values.  
5. Construct the email body in three parts:  
   - **Body1**: A table stating the TAR status and including any remarks.  
   - **Body2**: Links to the TAR form on intranet and internet, plus a closing signature.  
   - **Body3**: A disclaimer that the email is computer‑generated.  
6. Retrieve the intranet and internet URLs from the `TAMS_Parameters` table where `ParaCode = 'TAMS URL'` and the current date falls between `EffectiveDate` and `ExpiryDate`.  
7. Concatenate the body parts into a single HTML body string.  
8. Call `EAlertQ_EnQueue` to enqueue the email for delivery, passing all constructed fields and capturing the generated `@AlertID`.  
9. If the enqueue call fails (`@@ERROR <> 0`), set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to error handling.  
10. On normal completion, commit the transaction if it was started internally and return the (empty) message.  
11. On error, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `TAMS_Parameters` (to obtain URL values).  
* **Writes:** `EAlertQ_EnQueue` (inserts a new alert record into the queue).