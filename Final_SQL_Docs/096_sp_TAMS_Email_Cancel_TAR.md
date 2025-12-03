# Procedure: sp_TAMS_Email_Cancel_TAR

### Purpose
Send a cancellation notification email for a specified TAR.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR to cancel |
| @TARStatus | NVARCHAR(20) | Current status of the TAR (optional) |
| @TARNo | NVARCHAR(50) | TAR reference number (optional) |
| @ToSend | NVARCHAR(1000) | Comma‑separated list of email recipients |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error |

### Logic Flow
1. Initialise an internal transaction flag to 0.  
2. If the procedure is called outside an existing transaction, set the flag to 1 and begin a new transaction.  
3. Reset the output message to an empty string.  
4. Declare and initialise variables for email components: sender, system ID, subject, greeting, recipient lists, separators, and body sections.  
5. Construct the email subject using the TAR number and a “CANCELLED” suffix.  
6. Build the email body in three parts:  
   * **Body1** – notification that the TAR has been cancelled and a contact phone number.  
   * **Body2** – a link to the login page and a closing signature.  
   * **Body3** – a disclaimer that the email is computer‑generated.  
7. Concatenate the body parts into a single body string.  
8. Call `EAlertQ_EnQueue` to enqueue the email with all prepared parameters.  
9. If the enqueue call returns an error, set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to the error trap.  
10. On normal completion, commit the transaction if it was started internally and return the message.  
11. In the error trap, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** none  
* **Writes:** inserts an email record via `EAlertQ_EnQueue` (likely into the alert queue used by the TAMS system)