# Procedure: sp_TAMS_Check_UserExist

### Purpose
Determine whether a user record exists in **TAMS_User** based on supplied SAP number and/or login ID, returning `1` when a match is found.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @SapNo    | NVARCHAR(100) | SAP identifier to search for. |
| @LoginID  | NVARCHAR(200) | Login identifier to search for. |

### Logic Flow
1. **Both parameters provided**  
   - If `@LoginID` is not empty and `@SapNo` is not empty, query **TAMS_User** for a row where `LoginID = @LoginID` **and** `SAPNo = @SapNo`.  
   - If such a row exists, return `1`.

2. **Only SAP number provided**  
   - If `@SapNo` is empty, query **TAMS_User** for a row where `LoginID = @LoginID`.  
   - If found, return `1`.

3. **No output**  
   - If none of the above conditions are met, the procedure completes without returning a value.

*Commented sections* that would have handled the reverse checks (SAP only, Login only) are present but inactive.

### Data Interactions
* **Reads:** `TAMS_User`  
* **Writes:** None
---