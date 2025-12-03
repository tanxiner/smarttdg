# Procedure: sp_TAMS_Email_Apply_Late_TAR

### Purpose
This stored procedure applies a late TAR (Track Access Management System) email to an applicant or department, depending on the specified actor.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | Specifies whether the email is for an Applicant HOD Acceptance or another type of endorsement. |
| @AppDept | NVARCHAR(200) | The department that applied for the late TAR. |
| @TARNo | NVARCHAR(50) | The unique identifier for the late TAR. |
| @Actor | NVARCHAR(100) | The actor who is being notified (e.g., Applicant HOD Endorsement, TAP HOD Endorsement, etc.). |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @CCSend | NVARCHAR(1000) | The list of CC recipients for the email. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It initializes several variables to store the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the specified @EType and @Actor values, it generates a unique subject for the email.
4. The procedure constructs three tables (body1, body2, body3) to format the email content, including a table with department information, a link to access the TAR Form, and a signature.
5. It executes an external stored procedure [dbo].EAlertQ_EnQueue to send the email, passing in the generated message, sender, system ID, subject, greetings, alert message, recipients, CC list, BCC list, separator, and alert ID as parameters.
6. If any errors occur during execution, it sets a message variable with an error message and exits the procedure.
7. Otherwise, it commits or rolls back the transaction based on the internal flag and returns the generated email message.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes:
	+ TAMS_TAR (inserting or updating)
	+ EAlertQ_EnQueue (inserting)