# Procedure: sp_TAMS_Email_Urgent_TAR_OCC

### Purpose
Send an urgent TAR status notification email to specified recipients.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR record (unused in current logic). |
| @TARStatus | NVARCHAR(20) | Status of the TAR (Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | TAR reference number. |
| @Remarks | NVARCHAR(1000) | Optional remarks to include in the email body. |
| @ToSend | NVARCHAR(1000) | Comma‑separated list of email addresses to receive the message. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned after execution. |

### Logic Flow
1. Initialise an internal transaction flag and start a transaction if none is active.  
2. Reset the output message to an empty string.  
3. Declare and initialise email header variables: sender, system ID, system name, greeting, recipient list, CC/BCC lists, separator, and subject line that incorporates the TAR number and status.  
4. Build the first part of the email body (`@Body1`) as an HTML table.  
   - Insert a line describing the TAR status (Approved, Rejected, or Cancelled).  
   - Append the remarks line.  
5. Retrieve the intranet and internet login URLs from `TAMS_Parameters` where `ParaCode = 'TAMS URL'` and the current date falls between `EffectiveDate` and `ExpiryDate`.  
6. Build the second part of the body (`@Body2`) containing a link to the TAR form using the internet URL and a closing signature.  
7. Build the third part of the body (`@Body3`) with a non‑reply disclaimer.  
8. Concatenate `@Body1`, `@Body2`, and `@Body3` into the final body (`@Body`).  
9. Call `EAlertQ_EnQueue` to enqueue the email, passing all header and body components.  
10. If an error occurs during the enqueue call, set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to error handling.  
11. On successful completion, commit the transaction if it was started internally and return the message.  
12. In case of error, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** `TAMS_Parameters` (selects `ParaValue1`, `ParaValue2` for the current URL parameters).  
* **Writes:** `EAlertQ_EnQueue` (inserts a new alert record into the email queue, typically stored in `TAMS_TAR` or a related alert table).