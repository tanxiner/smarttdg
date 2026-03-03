# Procedure: sp_TAMS_Email_Apply_Urgent_TAR_20231009

### Purpose
Sends an urgent TAR notification email to the designated recipients, tailoring the subject and body content to the type of request and the actor responsible for the next approval step.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @EType   | INTEGER       | Indicates the email context: 1 for HOD acceptance, otherwise a generic urgent TAR notification. |
| @AppDept | NVARCHAR(200) | Department of the applicant; used in the email body. |
| @TARNo   | NVARCHAR(50)  | TAR reference number; included in the subject line. |
| @Actor   | NVARCHAR(100) | Role that will receive the email (e.g., Applicant HOD Endorsement, TAP HOD Endorsement, Power Endorsement, TAP Authority Verification, TAP Authority Approval, OCC Approval). |
| @ToSend  | NVARCHAR(1000)| Comma‑separated list of primary recipients. |
| @CCSend  | NVARCHAR(1000)| Comma‑separated list of CC recipients (unused in the current logic). |
| @Message | NVARCHAR(500) OUTPUT | Returns a status message; empty on success, error text on failure. |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction, start a new one and flag that the procedure owns the transaction.

2. **Initialize Variables**  
   - Set default sender, system identifiers, greeting, and empty message.  
   - Prepare placeholders for email components: subject, body sections, and recipient lists.

3. **Subject Construction**  
   - If `@EType = 1`, subject = “Urgent TAR *@TARNo* for Applicant HOD Acceptance.”  
   - Otherwise, subject starts with “Urgent TAR *@TARNo* for ” and appends a role‑specific suffix based on `@Actor` (e.g., “Applicant HOD Acceptance.”, “TAP HOD Acceptance.”, “Power Endorsement.”, etc.).

4. **Body Section 1 (Message)**  
   - Begin an HTML table.  
   - Insert a row that states the applicant department and the required action, varying the wording by `@EType` and `@Actor`.  
   - Close the table.

5. **Retrieve Login URLs**  
   - Default URLs are hard‑coded, but the procedure queries `TAMS_Parameters` for the current `TAMS URL` values (`ParaValue1` and `ParaValue2`) that are effective for the current date.

6. **Body Section 2 (Links & Sign‑off)**  
   - Add a line with a hyperlink to the intranet login page (`@LoginPage1`).  
   - Append a closing signature block (“Regards, System Administrator”).

7. **Body Section 3 (Footer)**  
   - Add a non‑reply notice and a computer‑generated email disclaimer.

8. **Assemble Full Body**  
   - Concatenate Body1, Body2, and Body3 into a single HTML string.

9. **Enqueue Email**  
   - Call `EAlertQ_EnQueue` with the prepared parameters to insert the email into the alert queue.

10. **Error Handling**  
    - If the enqueue call fails, set `@Message` to “ERROR INSERTING INTO TAMS_TAR” and jump to the error trap.

11. **Commit/Rollback**  
    - On success, commit the transaction if it was started internally.  
    - On error, rollback the transaction if it was started internally.

12. **Return**  
    - Return the `@Message` value (empty on success).

### Data Interactions
* **Reads:** `TAMS_Parameters` – retrieves current URL parameters for the login links.  
* **Writes:** `EAlertQ_EnQueue` – inserts a new alert record that will trigger the email delivery.  

---