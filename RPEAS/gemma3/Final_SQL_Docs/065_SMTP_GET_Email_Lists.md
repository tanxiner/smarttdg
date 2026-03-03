# Procedure: SMTP_GET_Email_Lists

### Purpose
This procedure retrieves a list of email addresses for sending alerts via SMTP, based on criteria within the EALERTQ table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ALERTID | INT | Identifies the alert for which email addresses are retrieved. |

### Logic Flow
1.  The procedure begins by selecting data from the EALERTQ table, filtering for records where the status is ‘Q’.
2.  It then retrieves a list of recipient email addresses associated with each alert. This list is constructed by querying the EALERTQTO table, filtering for active records where the email address is not empty.
3.  The email addresses are concatenated into a single string, separated by commas.
4.  The procedure retrieves the subject and greeting messages from the EALERTQ table.
5.  Finally, the procedure returns a result set containing the greeting, subject, alert message, sender, alert identifier, and the concatenated list of recipient email addresses (both recipients and CC recipients).

### Data Interactions
* **Reads:** EALERTQ, EALERTQTO
* **Writes:** None