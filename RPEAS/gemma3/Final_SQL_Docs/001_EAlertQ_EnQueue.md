# Procedure: EAlertQ_EnQueue

### Purpose
This stored procedure creates a new alert queue entry, populating the EAlertQ table and then sequentially adding recipient email addresses from the SendTo, CC, and BCC fields to the EAlertQTo, EAlertQCC, and EAlertQBCC tables, respectively, based on the presence of a separator character.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(1000) | The sender's email address. |
| @Subject | nvarchar(500) | The subject line of the alert. |
| @Sys | nvarchar(100) | System identifier, likely for tracking. |
| @Greetings | ntext | A greeting message to be included in the alert. |
| @AlertMsg | ntext | The main body of the alert message. |
| @UserId | nvarchar(50) | The user ID associated with the alert creation. |
| @SendTo | ntext | The primary list of recipient email addresses. |
| @CC | ntext | The list of CC'd email addresses. |
| @BCC | ntext | The list of BCC'd email addresses. |
| @Separator | nvarchar(1) | A character used to delimit recipient addresses within the SendTo field. |
| @AlertID | decimal(18, 0) | Output parameter: The ID of the newly created alert queue entry. |
| @From | nvarchar(250) | The originating system or application. |

### Logic Flow
The stored procedure begins by creating a new alert queue entry in the `EAlertQ` table, populating fields like `From`, `Sender`, `Subject`, `Sys`, `Greetings`, `AlertMsg`, `CreatedOn`, `CreatedBy`, and `LastUpdatedOn` with provided values and the current user ID. The `AlertID` (a unique identifier for the alert) is generated and assigned to the output parameter.

The procedure then processes recipient addresses from the `SendTo`, `CC`, and `BCC` fields. It utilizes a loop and string manipulation to extract individual email addresses, delimited by the `@Separator` character.

1.  **Initialization:** A temporary table `#tsendto`, `#tcc`, and `#tbcc` are created to hold the respective recipient lists.
2.  **Looping:** The procedure enters a loop that continues as long as the `@Separator` character is found within the `SendTo`, `CC`, or `BCC` fields.
3.  **Email Extraction:** Inside the loop, the procedure extracts individual email addresses from the delimited string using `substring` and `PATINDEX`.
4.  **Recipient Table Population:** For each extracted email address, the procedure inserts a new record into the `EAlertQTo`, `EAlertQCC`, or `EAlertQBCC` table, depending on the source field. The `AlertID` is used as the primary key for all recipient tables. The `CreatedOn`, `CreatedBy`, and `LastUpdatedOn` fields are populated with the current date and user ID.
5.  **String Manipulation:** The `UPDATETEXT` function is used to move the pointer within the delimited string, allowing the procedure to process the next email address.
6.  **Cleanup:** After processing all email addresses, the temporary tables `#tsendto`, `#tcc`, and `#tbcc` are dropped.
7.  **Commit:** Finally, the transaction is committed, making the changes permanent.

### Data Interactions
* **Reads:** `EAlertQ`, `EAlertQTo`, `EAlertQCC`, `EAlertQBCC`
* **Writes:** `EAlertQ`, `EAlertQTo`, `EAlertQCC`, `EAlertQBCC`