# Procedure: sp_TAMS_Email_Apply_Urgent_TAR_20231009

### Purpose
This stored procedure applies an urgent TAR (Track Access Management System) email to various stakeholders, including the applicant HOD acceptance, TAP HOD endorsement, power endorsement, TAP authority verification, and OCC approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType	| INTEGER | The type of email being sent (1 for urgent TAR) |
| @AppDept	| NVARCHAR(200) | The department of the applicant |
| @TARNo	| NVARCHAR(50) | The TAR number |
| @Actor	| NVARCHAR(100) | The actor performing the action (e.g. Applicant HOD Endorsement) |
| @ToSend	| NVARCHAR(1000) | The list of recipients to send the email to |
| @CCSend	| NVARCHAR(1000) | The list of CC recipients to send the email to |
| @Message	| NVARCHAR(500) | The output message |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets a flag and begins a new transaction.
2. It then initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the email type (@EType), it sets the subject accordingly.
4. It constructs the body of the email by concatenating three tables: one with the applicant's department information, another with login instructions, and a third with a disclaimer.
5. The procedure then executes an EAlertQ_EnQueue stored procedure to send the email to the specified recipients.
6. If any errors occur during this process, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the output message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve the URL parameter value)
* Writes: TAMS_TAR table (to insert or update a new email)