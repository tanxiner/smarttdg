# Procedure: sp_TAMS_Email_Urgent_TAR_OCC

### Purpose
This stored procedure sends an urgent email to a list of recipients regarding a TAR (Track Access Management System) occurrence.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR occurrence. |
| @TARStatus | NVARCHAR(20) | The status of the TAR occurrence (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number of the TAR occurrence. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR occurrence. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. It retrieves the login page URLs from the TAMS parameters table based on the 'TAMS URL' parameter code.
4. The procedure generates the email body by concatenating three tables: one for the TAR occurrence status, another for the login page links, and a third for the system greetings and disclaimers.
5. It executes an EAlertQ_EnQueue stored procedure to enqueue the alert message with the specified sender, subject, and recipients.
6. If any errors occur during the execution of the EAlertQ_EnQueue procedure, it sets the output parameter @Message to an error message and exits the transaction.
7. Otherwise, it commits the transaction if one was started and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve login page URLs)
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure, but implied by the use of TARID)