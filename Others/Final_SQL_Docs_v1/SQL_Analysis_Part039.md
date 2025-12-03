# Procedure: sp_TAMS_Email_Apply_Urgent_TAR
**Type:** Stored Procedure

The purpose of this stored procedure is to apply an urgent TAR (Track Access Management System) email to a user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | The type of email to be sent (e.g. Urgent TAR for Applicant HOD Acceptance) |
| @AppDept | NVARCHAR(200) | The department of the applicant |
| @TARNo | NVARCHAR(50) | The TAR number |
| @Actor | NVARCHAR(100) | The actor performing the action (e.g. Applicant HOD Endorsement) |
| @ToSend | NVARCHAR(1000) | The list of users to send the email to |
| @CCSend | NVARCHAR(1000) | The list of users to CC on the email |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR
* Writes: TAMS_TAR