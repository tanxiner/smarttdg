# Procedure: sp_TAMS_Email_Late_TAR_OCC

### Purpose
This stored procedure sends an email notification to users regarding a late TAR (Track Access Management System) that has been approved, rejected, or cancelled by CC.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR. |
| @TARStatus | NVARCHAR(20) | The status of the late TAR (Approved, Rejected, or Cancelled). |
| @TARNo | NVARCHAR(50) | The number of the late TAR. |
| @Remarks | NVARCHAR(1000) | Any remarks about the late TAR. |
| @ToSend | NVARCHAR(1000) | The list of users to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of users to send to, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the TAR status, it generates three parts of the email body: a table with remarks, a link to access the TAR form, and a signature.
4. The procedure executes an external stored procedure `EAlertQ_EnQueue` to send the email notification using the generated message.
5. If any errors occur during execution, it rolls back the transaction and returns an error message.
6. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes: Inserts/updates data in the `TAMS_TAR` table (not shown in this code snippet).