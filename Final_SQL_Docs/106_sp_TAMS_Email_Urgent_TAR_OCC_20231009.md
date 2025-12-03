# Procedure: sp_TAMS_Email_Urgent_TAR_OCC_20231009

### Purpose
Sends an urgent TAR status notification email to specified recipients, formatting the message based on the TAR status and including relevant links.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | INTEGER       | Identifier of the TAR record (unused in current logic). |
| @TARStatus| NVARCHAR(20)  | Current status of the TAR (Approved, Rejected, Cancelled). |
| @TARNo    | NVARCHAR(50)  | TAR reference number used in the email subject and body. |
| @Remarks  | NVARCHAR(1000)| Optional remarks to include in the email body. |
| @ToSend   | NVARCHAR(1000)| Comma‑separated list of email addresses to receive the notification. |
| @Message  | NVARCHAR(500) OUTPUT | Status message returned to the caller (empty on success). |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction, start a new one and flag that the procedure owns it.

2. **Initialize Variables**  
   - Set sender, system identifiers, greeting, and email lists.  
   - Build the email subject: `"Urgent TAR <TARNo> has been <TARStatus> by CC"`.

3. **Compose Email Body**  
   - **Body1**:  
     - Start an HTML table.  
     - Add a row describing the TAR status:  
       - If `Approved` → “has been APPROVED by CC and requires your necessary actions.”  
       - If `Rejected` → “has been REJECTED by CC.”  
       - If `Cancelled` → “has been Cancelled by CC.”  
     - Add a row with the remarks.  
   - **Body2**:  
     - Retrieve intranet and internet login URLs from `TAMS_Parameters` where `ParaCode = 'TAMS URL'` and the current date is within the effective range.  
     - Add links to the TAR form using those URLs.  
     - Append a closing signature.  
   - **Body3**:  
     - Append a disclaimer: “Do Not reply. This is a computer generated Email.”  
   - Concatenate Body1, Body2, and Body3 into the final `@Body`.

4. **Enqueue Alert**  
   - Call `EAlertQ_EnQueue` with the constructed subject, body, and recipient lists to insert the email into the alert queue.

5. **Error Handling**  
   - If an error occurs during enqueue, set `@Message` to `"ERROR INSERTING INTO TAMS_TAR"` and jump to the error trap.  
   - On error, rollback the transaction if it was started internally.  
   - On success, commit the transaction if it was started internally.

6. **Return**  
   - Return the `@Message` (empty on success).

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters` (to obtain intranet and internet URLs for the TAR form).

* **Writes:**  
  - Calls `EAlertQ_EnQueue`, which inserts a new alert record into the alert queue (no direct table writes in this procedure).