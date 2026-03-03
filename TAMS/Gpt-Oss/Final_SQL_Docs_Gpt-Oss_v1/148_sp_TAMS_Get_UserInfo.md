# Procedure: sp_TAMS_Get_UserInfo

### Purpose
Retrieves user details, updates the last login timestamp for active accounts, and returns the account status, a message, and the user’s roles for a specified login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | NVARCHAR(100) | Login identifier used to locate the user record |

### Logic Flow
1. Initialise two local variables, `@ret` and `@retmsg`, to empty strings.  
2. Check if a user with the supplied login ID exists, is active, and has a `ValidTo` date in the future.  
   - If true, update that user’s `lastlogin` field to the current date and time.  
3. If the first condition fails, check if the user exists but the `ValidTo` date is in the past.  
   - If true, set `@ret` to `'Expired'` and provide an expiration message in `@retmsg`.  
4. If the second condition fails, check if the user exists but is marked inactive (`IsActive = 0`).  
   - If true, set `@ret` to `'DeActivate'` and supply a deactivation message in `@retmsg`.  
5. If none of the above conditions are met, set `@ret` to `'NoAccess'`.  
6. Return the user record for the supplied login ID where the account is active and not expired.  
7. Return the account status (`@ret`) and the associated message (`@retmsg`).  
8. Return the list of role names assigned to the user by joining the user, user‑role, and role tables on the user ID and role ID, filtered by the supplied login ID.

### Data Interactions
* **Reads:** `TAMS_User`, `TAMS_User_Role`, `TAMS_Role`  
* **Writes:** `TAMS_User` (updates `lastlogin` for active users)