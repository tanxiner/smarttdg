# Procedure: sp_TAMS_Email_Apply_Late_TAR

### Purpose
Sends an automated email notifying the relevant party that a Late TAR has been applied for, with subject and body tailored to the type of action required.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | Indicates the email type; 1 for HOD acceptance, otherwise a generic type that is refined by @Actor. |
| @AppDept | NVARCHAR(200) | Department of the applicant, used in the email body. |
| @TARNo | NVARCHAR(50) | TAR number, included in the subject line. |
| @Actor | NVARCHAR(100) | Role that triggered the email (e.g., “Applicant HOD Endorsement”, “TAP Authority Approval”). |
| @ToSend | NVARCHAR(1000) | Primary recipient email addresses. |
| @CCSend | NVARCHAR(1000) | CC recipient email addresses. |
| @Message | NVARCHAR(500) OUTPUT | Returns status message; empty on success, error text on failure. |

### Logic Flow
1. Initialise a transaction flag (`@IntrnlTrans`) to 0.  
2. If no outer transaction exists, set the flag to 1 and begin a new transaction.  
3. Reset `@Message` to an empty string.  
4. Declare and initialise email‑related variables: sender, system ID, system name, greeting, recipient lists, separators, and placeholders for the email body.  
5. Build the email subject:  
   * If `@EType = 1`, subject = “Late TAR *@TARNo* for Applicant HOD Acceptance.”  
   * Otherwise, start with “Late TAR *@TARNo* for ” and append a phrase based on `@Actor` (e.g., “Applicant HOD Acceptance.”, “TAP Verification.”, etc.).  
6. Construct the email body in three parts:  
   * **Body1** – a table containing a sentence that references `@AppDept` and the action required, chosen according to `@EType` and `@Actor`.  
   * **Body2** – a link to the TAR login page and a closing signature.  
   * **Body3** – a disclaimer that the email is computer‑generated.  
   Concatenate the parts into `@Body`.  
7. Call `EAlertQ_EnQueue` to enqueue the email, passing all constructed values and capturing an alert ID.  
8. If the enqueue call fails (`@@ERROR <> 0`), set `@Message` to “ERROR INSERTING INTO TAMS_TAR” and jump to error handling.  
9. On normal completion, commit the transaction if it was started internally and return `@Message`.  
10. On error, rollback the transaction if it was started internally and return `@Message`.

### Data Interactions
* **Reads:** None  
* **Writes:** None (the procedure enqueues an alert via `EAlertQ_EnQueue`, which internally writes to the alert queue).