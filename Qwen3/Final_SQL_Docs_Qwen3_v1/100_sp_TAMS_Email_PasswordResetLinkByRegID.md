# Procedure: sp_TAMS_Email_PasswordResetLinkByRegID

### Purpose
This stored procedure generates an email with a password reset link for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(200) | The ID of the user to generate the email for. |

### Logic Flow
1. The procedure checks if a user with the specified ID exists in the TAMS_User table.
2. If the user exists, it sets various variables such as the sender's name, system ID, subject, greetings, and body content for the email.
3. It constructs the password reset link using the provided cipher value.
4. The procedure then executes an external stored procedure, EAlertQ_EnQueue, to send the email with the constructed body content.

### Data Interactions
* **Reads:** TAMS_User table (to retrieve user data)
* **Writes:** None