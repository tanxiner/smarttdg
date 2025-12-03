# Procedure: sp_TAMS_Email_Apply_Urgent_TAR

### Purpose
Sends an urgent TAR notification email to the appropriate recipients, tailoring the subject and body to the requested action.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @EType   | INTEGER       | Indicates the email type; 1 for HOD acceptance, otherwise specifies the action type. |
| @AppDept | NVARCHAR(200) | Department that has applied for the urgent TAR. |
| @TARNo   | NVARCHAR(50)  | Identifier of the TAR. |
| @Actor   | NVARCHAR(100) | Role that must act on the TAR (e.g., Applicant HOD Endorsement, TAP Authority Approval). |
| @ToSend  | NVARCHAR(1000)| Comma‑separated list of primary recipients. |
| @CCSend  | NVARCHAR(1000)| Comma‑separated list of CC recipients. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns it.  
2. **Initialize Variables** – Set defaults for sender, system identifiers, greeting, and email lists.  
3. **Subject Construction**  
   * If `@EType = 1`, subject = “Urgent TAR *@TARNo* for Applicant HOD Acceptance.”  
   * Otherwise, subject starts with “Urgent TAR *@TARNo* for ” and appends a phrase based on `@Actor` (e.g., “Applicant HOD Acceptance.”, “TAP Verification.”, etc.).  
4. **Body Construction**  
   * **Body1** – Builds an HTML table row that states the department and the required action, varying the wording according to `@EType` and `@Actor`.  
   * **Body2** – Adds a link to the TAR form using the URL retrieved from `TAMS_Parameters` (parameter code “TAMS URL”) and a closing sign‑off.  
   * **Body3** – Appends a disclaimer that the email is computer‑generated.  
   * Concatenates Body1, Body2, and Body3 into the final `@Body`.  
5. **Retrieve Login URL** – Queries `TAMS_Parameters` for the current “TAMS URL” values, ensuring the dates are valid.  
6. **Queue Email** – Calls `EAlertQ_EnQueue` with all constructed fields to enqueue the email for delivery.  
7. **Error Handling** – If the enqueue call fails, set `@Message` to “ERROR INSERTING INTO TAMS_TAR” and jump to error handling.  
8. **Commit/Rollback** – If the procedure started the transaction, commit on success or rollback on error.  
9. **Return** – Return the status message.

### Data Interactions
* **Reads:** `TAMS_Parameters` (to obtain the current TAR login URL).  
* **Writes:** None directly; the procedure delegates email queuing to `EAlertQ_EnQueue`, which writes to the alert queue.