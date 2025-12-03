# Procedure: sp_TAMS_Email_Urgent_TAR

### Purpose
Sends an urgent TAR status notification email to specified recipients.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | INTEGER       | Identifier of the TAR record. |
| @TARStatus| NVARCHAR(20)  | Current status of the TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo    | NVARCHAR(50)  | TAR reference number. |
| @Remarks  | NVARCHAR(1000)| Optional remarks to include in the email body. |
| @Actor    | NVARCHAR(100) | Role that performed the status change (e.g., Applicant HOD Endorsement). |
| @ToSend   | NVARCHAR(1000)| Comma‑separated list of email addresses to receive the message. |
| @Message  | NVARCHAR(500) OUTPUT | Result message indicating success or error. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Initialize Variables** – Set defaults for sender, system identifiers, greeting, and email lists.  
3. **Subject Construction** – Build the subject line using the TAR number, status, and actor.  
4. **Body Construction**  
   * Create a status paragraph that states whether the TAR was Approved, Rejected, or Cancelled.  
   * Append any remarks supplied.  
   * Retrieve the current TAMS login URLs from `TAMS_Parameters` where the parameter code is `TAMS URL` and the current date is within the effective range.  
   * Add a link to the TAR form using the retrieved URL.  
   * Append a standard sign‑off and a non‑reply footer.  
5. **Queue Email** – Call `EAlertQ_EnQueue` with the assembled subject, body, and recipient lists. Capture the generated alert ID.  
6. **Error Handling** – If the enqueue call fails, set an error message and jump to the error trap.  
7. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it untouched.  
8. **Return** – Output the message string (empty on success, error text on failure).

### Data Interactions
* **Reads:** `TAMS_Parameters` – fetches `ParaValue1` and `ParaValue2` for the current TAMS URL.  
* **Writes:** `EAlertQ_EnQueue` – inserts a new alert record into the email queue.  

---