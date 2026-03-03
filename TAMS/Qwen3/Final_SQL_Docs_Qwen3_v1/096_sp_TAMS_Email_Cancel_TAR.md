# Procedure: sp_TAMS_Email_Cancel_TAR

### Purpose
This stored procedure sends an email notification to a list of recipients when a TAR (Track Access Management System) record is cancelled.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR record being cancelled. |
| @TARStatus | NVARCHAR(20) | The status of the TAR record (e.g., "CANCELLED"). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR record. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it starts one.
2. It initializes an internal transaction flag and sets the output parameter @Message to an empty string.
3. The procedure declares several variables to store email content, including sender information, subject, body, and links.
4. It populates these variables with default values or user-provided input (if available).
5. The procedure executes a stored procedure [dbo].EAlertQ_EnQueue to send the email notification to the specified recipients.
6. If any errors occur during this process, it rolls back the internal transaction and returns an error message.
7. Otherwise, it commits the internal transaction and returns the generated email message.

### Data Interactions
* Reads: None explicitly listed; however, the procedure interacts with the [dbo].EAlertQ_EnQueue stored procedure, which likely reads data from a database table to retrieve recipient information.
* Writes: The procedure writes data to the following tables:
	+ TAMS_TAR (to update the TAR record)
	+ [dbo].EAlertQ_EnQueue (to insert or update email notification records)