# Procedure: sp_TAMS_Email_Urgent_TAR_OCC_20231009

### Purpose
This stored procedure sends an urgent email notification to stakeholders regarding a TAR (Track Access Management System) occurrence.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR occurrence. |
| @TARStatus | NVARCHAR(20) | The status of the TAR occurrence (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR occurrence. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR occurrence. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag (@IntrnlTrans) accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients (ToList), CC list, BCC list, separator, alert message, and alert ID.
3. It retrieves the login page URLs from the TAMS Parameters table based on the 'TAMS URL' parameter code.
4. The procedure generates the email body by concatenating three tables: one for the TAR occurrence details, another for the login page links, and a third for the system greetings and disclaimers.
5. It executes the EAlertQ_EnQueue stored procedure to enqueue the alert message with the specified sender, subject, greetings, and recipients.
6. If an error occurs during the execution of the EAlertQ_EnQueue procedure, it sets the @Message output parameter to an error message and exits the transaction.
7. Otherwise, it commits the transaction if a transaction was started.

### Data Interactions
* Reads: TAMS_Parameters table (for retrieving login page URLs)
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure, but implied by the email notification)