# Procedure: sp_TAMS_User_CheckLastEmailRequest

### Purpose
This stored procedure checks if a user has made an email request within a specified rate limit.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user to check. |
| @Mode | NVARCHAR(200) | The mode of operation, either 'User Detail View' or 'Forget Password'. |

### Logic Flow
The procedure first checks if a valid login ID is provided. If it is, it retrieves the registration details for that user and then checks the email requests made by that user within the last 60 seconds (defined by the Rate Limiting parameter). If an email request was made recently, the procedure returns -1; otherwise, it returns 1.

### Data Interactions
* **Reads:** TAMS_Registration, EAlertQTo, eAlertQ, TAMS_Parameters