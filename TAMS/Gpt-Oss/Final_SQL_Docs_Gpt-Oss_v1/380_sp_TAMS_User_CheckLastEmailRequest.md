# Procedure: sp_TAMS_User_CheckLastEmailRequest

### Purpose
Determine whether a user can request a new email (e.g., sign‑up status or password reset) based on the time elapsed since the last sent email of the same type.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @LoginID  | NVARCHAR(200) | User identifier to look up in TAMS_Registration; may be NULL or empty. |
| @Mode     | NVARCHAR(200) | Operation type; expected values are 'User Detail View' or 'Forget Password'. |

### Logic Flow
1. **Initialize variables** for the most recent email date (`@maxDate`), the email address (`@EmailID`), and the rate‑limit threshold (`@RateLimit`).
2. **Check @LoginID presence** – if it is not an empty string, proceed.
3. **Verify user existence** – confirm that a record with `LoginId = @LoginID` exists in TAMS_Registration.
4. **Determine last email date**  
   * If `@Mode = 'User Detail View'`, find the maximum `CreatedOn` from eAlertQ where the subject contains *Link to View Sign Up Status* and the recipient matches the user’s most recent email address.  
   * If `@Mode = 'Forget Password'`, perform the same lookup but for subjects containing *Link to reset password*.
5. **Retrieve rate‑limit setting** – read `Paravalue1` from TAMS_Parameters where `ParaCode = 'Rate Limiting'`.
6. **Compare timestamps** – calculate the difference in seconds between the current time and `@maxDate`.  
   * If this difference is **less** than `@RateLimit`, return `-1` (request denied).  
   * Otherwise, return `1` (request allowed).
7. **Exit** – if any earlier condition fails (empty @LoginID or user not found), the procedure ends without returning a value.

### Data Interactions
* **Reads:**  
  - TAMS_Registration  
  - EAlertQTo  
  - eAlertQ  
  - TAMS_Parameters  
* **Writes:** None

---