# Procedure: sp_TAMS_Email_Urgent_TAR

### Purpose
This stored procedure sends an urgent email to stakeholders regarding a TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being updated. |
| @TARStatus | NVARCHAR(20) | The current status of the TAR. |
| @TARNo | NVARCHAR(50) | The number associated with the TAR. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR update. |
| @Actor | NVARCHAR(100) | The actor who performed the action on the TAR. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and body parts.
3. Based on the actor who performed the action, it updates the subject line with the corresponding title (e.g., "Applicant HOD" or "TAP Verifier").
4. It constructs the email body by combining three table elements: a remark section, a login link section, and a closing message section.
5. The procedure executes an external stored procedure `EAlertQ_EnQueue` to enqueue the alert message with the specified sender, system ID, subject, greetings, alert message, recipients, CC list, BCC list, separator, and alert ID output parameter.
6. If any errors occur during execution, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table to retrieve the URL parameter value.
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure but implied by the context).