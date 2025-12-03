# Procedure: sp_TAMS_Email_Apply_Late_TAR
**Type:** Stored Procedure

The procedure applies a late TAR (Track Access Management System) email to an applicant or department.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | The type of email to apply (1 for Applicant HOD Endorsement, 2 for TAP HOD Endorsement, etc.) |
| @AppDept | NVARCHAR(200) | The department of the applicant or user |
| @TARNo | NVARCHAR(50) | The TAR number |
| @Actor | NVARCHAR(100) | The actor performing the action (e.g. Applicant HOD Endorsement) |
| @ToSend | NVARCHAR(1000) | The email body to send to the applicant or user |
| @CCSend | NVARCHAR(1000) | The CC list for the email |
| @Message | NVARCHAR(500) | Output parameter containing the final message |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal transaction flag and begins a new transaction.
3. Initializes the output parameter @Message to an empty string.
4. Extracts various email components (sender, system ID, subject, greetings, etc.) from input parameters.
5. Constructs the email body by combining multiple tables of text.
6. Executes the EAlertQ_EnQueue stored procedure to enqueue the email for sending.
7. If any errors occur during execution, rolls back the transaction and returns an error message.
8. If no errors occur, commits the transaction and returns the final message.

### Data Interactions
* Reads: None explicitly listed, but may involve reading from internal tables or variables.
* Writes: 
	+ TAMS_TAR table (inserting a new record)
	+ EAlertQ_EnQueue table (enqueuing an email for sending)