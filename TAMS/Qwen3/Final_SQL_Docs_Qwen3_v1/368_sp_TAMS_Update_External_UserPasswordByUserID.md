# Procedure: sp_TAMS_Update_External_UserPasswordByUserID

### Purpose
This stored procedure updates the external user password for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user whose password is to be updated. |
| @Password | NVARCHAR(200) | The new password for the specified user ID. |

### Logic Flow
1. The procedure begins by attempting to start a transaction.
2. It then checks if a record exists in the TAMS_User table with the specified UserID.
3. If such a record is found, the procedure updates the Password column of that record using an encryption function (dbo.EncryptString) and sets the PasswordChangedDate to the current date and time.
4. After updating the password, the procedure commits the transaction if no errors occurred.
5. If any error occurs during this process, the procedure rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table