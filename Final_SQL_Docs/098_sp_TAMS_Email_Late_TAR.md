# Procedure: sp_TAMS_Email_Late_TAR

### Purpose
Sends a status‑update e‑mail for a Late TAR, notifying the specified recipients of the approval, rejection, or cancellation outcome.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | INTEGER       | Identifier of the TAR record (unused in the current logic). |
| @TARStatus| NVARCHAR(20)  | Current status of the TAR (Approved, Rejected, Cancelled). |
| @TARNo    | NVARCHAR(50)  | TAR reference number used in the e‑mail subject and body. |
| @Remarks  | NVARCHAR(1000)| Optional remarks to include in the e‑mail body. |
| @Actor    | NVARCHAR(100) | Role that performed the action, used to append to the subject line. |
| @ToSend   | NVARCHAR(1000)| Comma‑separated list of e‑mail recipients. |
| @Message  | NVARCHAR(500) OUTPUT | Result message indicating success or error. |

### Logic Flow
1. Initialise a transaction flag (`@IntrnlTrans`) to 0.  
2. If no active transaction exists, set the flag to 1 and begin a new transaction.  
3. Reset the output message to an empty string.  
4. Declare and initialise variables for e‑mail composition: sender, system ID, system name, greeting, recipient list, CC/BCC lists, separator, subject, body parts, and login page URL.  
5. Build the email subject: start with “Late TAR \<TARNo\> has been \<TARStatus\> by” and append the actor’s role (Applicant HOD, TAP HOD, Power, TAP Verifier, TAP Approver, OCC) if it matches one of the predefined values.  
6. Construct the body in three sections:  
   - **Body1**: Status notification and remarks.  
   - **Body2**: Link to the TAR form and closing signature.  
   - **Body3**: Standard footer warning not to reply.  
   Concatenate these sections into the final body (`@Body`).  
7. Call `EAlertQ_EnQueue` to enqueue the e‑mail with all composed parameters.  
8. If the call returns an error, set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to the error handling section.  
9. On normal completion, commit the transaction if it was started internally and return the message.  
10. In the error handling section, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** None (no SELECT from persistent tables).  
* **Writes:** Enqueues an alert via `EAlertQ_EnQueue`, which records the e‑mail in the alert queue (typically the `TAMS_TAR` or related alert table).