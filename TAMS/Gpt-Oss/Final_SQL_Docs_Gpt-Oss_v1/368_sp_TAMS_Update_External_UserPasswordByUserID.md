# Procedure: sp_TAMS_Update_External_UserPasswordByUserID

### Purpose
Updates a user’s password and records the change date for a specified user.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @UserID   | INT           | Identifier of the user whose password is to be updated. |
| @Password | NVARCHAR(200) | New plaintext password to be encrypted and stored. |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Check if a record exists in **TAMS_User** with the supplied **@UserID**.  
3. If the user exists, encrypt **@Password** using the `dbo.EncryptString` function, update the **Password** field, and set **PasswordChangedDate** to the current timestamp.  
4. Commit the transaction.  
5. If any error occurs during the process, roll back the transaction to leave the database unchanged.

### Data Interactions
* **Reads:** TAMS_User  
* **Writes:** TAMS_User  

---