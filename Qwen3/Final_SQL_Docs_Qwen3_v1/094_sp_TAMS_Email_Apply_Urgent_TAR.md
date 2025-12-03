# Procedure: sp_TAMS_Email_Apply_Urgent_TAR

### Purpose
This stored procedure applies an urgent TAR (Track Access Management System) email to various stakeholders, including Applicant HOD Acceptance, TAP HOD Endorsement, Power Endorsement, and others. It generates a personalized email with the required details and sends it to the specified recipients.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | The type of email being sent (e.g., Urgent TAR for Applicant HOD Acceptance) |
| @AppDept | NVARCHAR(200) | The department of the applicant |
| @TARNo | NVARCHAR(50) | The TAR number |
| @Actor | NVARCHAR(100) | The actor performing the action (e.g., Applicant HOD Endorsement) |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to |
| @CCSend | NVARCHAR(1000) | The list of CC recipients to send the email to |
| @Message | NVARCHAR(500) | The output parameter that stores the generated email message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal transaction flag and begins a new transaction.
2. It initializes several variables, including the sender's name, system ID, subject line, greetings, and body content.
3. Based on the @EType parameter, it generates the subject line and body content for the email. The subject line includes the TAR number and the actor performing the action.
4. It populates the body content with tables containing relevant information, such as the applicant's department and a link to access the TAR Form via Intranet or Internet.
5. It executes an external stored procedure (EAlertQ_EnQueue) to send the email to the specified recipients.
6. If any errors occur during the execution of EAlertQ_EnQueue, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve the URL parameter value)
* Writes: TAMS_TAR table (to insert or update a new TAR record)