# Procedure: sp_TAMS_Get_External_UserInfo_by_LoginIDPWD

### Purpose
Retrieve the full user record for an active external user when the supplied login ID and password match.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @LoginID  | NVARCHAR(100) | The user’s login identifier. |
| @LoginPWD | NVARCHAR(200) | The user’s password in plain text. |

### Logic Flow
1. Check if a record exists in **TAMS_User** where `LoginID` equals the supplied @LoginID, `IsExternal` is 1, and `IsActive` is 1.  
2. If such a record exists, select all columns from **TAMS_User** for that `LoginID` where the decrypted `Password` matches the supplied @LoginPWD.  
3. If no matching external active user is found, the procedure returns no rows.  
4. (Commented out code that would return a user record regardless of external status is ignored.)

### Data Interactions
* **Reads:** TAMS_User  
* **Writes:** None  

---