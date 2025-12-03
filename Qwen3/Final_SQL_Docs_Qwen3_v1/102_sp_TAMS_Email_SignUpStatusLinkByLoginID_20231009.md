# Procedure: sp_TAMS_Email_SignUpStatusLinkByLoginID_20231009

### Purpose
This stored procedure generates an email link for a user to view their sign-up status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user. |

### Logic Flow
1. The procedure checks if a registration record exists for the given login ID.
2. If a record is found, it retrieves the email addresses associated with that login ID.
3. It constructs an email body with a link to view the sign-up status and other relevant information.
4. The procedure then sends this email using the EAlertQ_EnQueue stored procedure.

### Data Interactions
* **Reads:** TAMS_Registration table (to retrieve registration record for the given login ID)
* **Writes:** None