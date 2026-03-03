# Procedure: sp_TAMS_Email_Late_TAR

### Purpose
This stored procedure sends an email notification to stakeholders regarding a late TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR being notified. |
| @TARStatus | NVARCHAR(20) | The current status of the late TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the late TAR. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the late TAR. |
| @Actor | NVARCHAR(100) | The actor who endorsed or approved the late TAR (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend | NVARCHAR(1000) | The list of stakeholders to whom the email should be sent. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it begins a new transaction.
2. It initializes an internal transaction flag and sets the output parameter @Message to an empty string.
3. The procedure declares several variables to store sender information, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
4. Based on the value of @Actor, it updates the subject line accordingly.
5. It constructs the email body by concatenating three tables: one for remarks, another for a link to access the TAR Form, and a third with a disclaimer.
6. The procedure executes an external stored procedure [dbo].EAlertQ_EnQueue to enqueue the alert message and send it to the specified stakeholders.
7. If any errors occur during this process, it sets @Message to an error message and exits the transaction.
8. Otherwise, it commits the transaction if an internal transaction was started.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes:
	+ TAMS_TAR (for storing the alert message)
	+ TAMS_TARID (for storing the TAR ID)