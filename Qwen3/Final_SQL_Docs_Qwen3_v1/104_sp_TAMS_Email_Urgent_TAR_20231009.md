# Procedure: sp_TAMS_Email_Urgent_TAR_20231009

### Purpose
This stored procedure sends an urgent email notification to stakeholders regarding a TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| INTEGER | The ID of the TAR being updated. |
| @TARStatus	| NVARCHAR(20) | The current status of the TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo	| NVARCHAR(50) | The number associated with the TAR. |
| @Remarks	| NVARCHAR(1000) | Additional remarks about the TAR update. |
| @Actor	| NVARCHAR(100) | The actor who performed the action (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend	| NVARCHAR(1000) | The list of stakeholders to send the email to. |
| @Message	| NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of stakeholders, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the actor performing the action, it updates the subject line to include the actor's name.
4. The procedure generates the email body by concatenating three tables: a remark table, a login link table, and an alert message table.
5. It executes the EAlertQ_EnQueue stored procedure to enqueue the email notification.
6. If any errors occur during execution, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_Parameters (to retrieve the URL parameter value)
* Writes: None