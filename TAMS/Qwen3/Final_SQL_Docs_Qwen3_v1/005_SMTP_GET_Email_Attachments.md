# Procedure: SMTP_GET_Email_Attachments

The purpose of this stored procedure is to retrieve the file path of email attachments associated with a specific alert.

### Parameters
| Name | Type | Purpose |
| @AlertID | int | Identifies the unique identifier for the alert whose attachments are to be retrieved. |

### Logic Flow
1. The procedure starts by selecting data from the EAlertQAtt table.
2. It filters the results based on two conditions: the Active flag must be set to 1, and the AlertID parameter passed in must match the one stored in the database for the current alert.
3. Once filtered, the procedure returns only the FPath column, which presumably contains the file path of the email attachment.

### Data Interactions
* **Reads:** EAlertQAtt table