# Procedure: sp_TAMS_User_CheckLastUserRegistration

### Purpose
This stored procedure checks if a user has registered within the allowed time frame as defined by the 'Rate Limiting-UserReg' parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user to check. |

### Logic Flow
1. If a valid login ID is provided, the procedure checks if there is an existing registration record for that user.
2. If a registration record exists, it retrieves the maximum date of creation from that record.
3. It then compares this date with the current date and time using the 'DATEDIFF' function to calculate the difference in seconds.
4. If the difference is less than the rate limiting value defined by the 'Rate Limiting-UserReg' parameter, the procedure returns -1 indicating that the user has registered too recently.
5. Otherwise, it returns 1.

### Data Interactions
* **Reads:** TAMS_Registration table
* **Writes:** None