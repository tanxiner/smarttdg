# Procedure: sp_TAMS_Get_User_List_By_Line_20211101

### Purpose
Retrieves a list of users that match specified search criteria, aggregates their role lines and modules, and returns the compiled data set.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | Login ID of the user executing the procedure; used to limit results to roles the current user has access to. |
| @SearchRail | NVARCHAR(10) | Filter for role line values; supports wildcard matching. |
| @SearchUserType | NVARCHAR(10) | Filter for user external status; expects '0' or '1' or wildcard. |
| @SearchActive | NVARCHAR(10) | Filter for user active status; expects '0' or '1' or wildcard. |
| @SearchModule | NVARCHAR(10) | Filter for role module values; supports wildcard matching. |
| @SearchUserID | NVARCHAR(100) | Filter for user login ID; supports wildcard matching. |
| @SearchUserName | NVARCHAR(200) | Filter for user name; supports wildcard matching. |

### Logic Flow
1. **Temporary Table Creation** – A table named `#UserTable` is created to hold the final result set with columns for row identity, user ID, role lines, user type, login ID, name, modules, and active flag.  
2. **Variable Declaration** – Local variables are declared for user attributes, module flags, and return messages.  
3. **Primary Cursor Setup** – A cursor named `cur` selects users who:
   - Are linked to roles that belong to the same lines as the current user.
   - Match the supplied name, login ID, rail, external status, active status, and module filters.  
   The cursor returns the user’s ID, login ID, mapped external status string, name, and active flag.  
4. **Cursor Iteration** – For each user fetched:
   - **Module Determination** – A nested cursor `u_cur` retrieves distinct modules for the user’s roles.  
     - Flags `@HasTAR` and `@HasOCC` are set when modules 'TAR' or 'OCC' are found.  
     - If a module other than 'TAR' or 'OCC' appears, both flags are set to true.  
     - After processing, `@UModule` is set to a comma‑separated string reflecting the presence of TAR, OCC, or both.  
   - **Rail Determination** – Another nested cursor `u_curRail` retrieves distinct lines for the user’s roles.  
     - If a line value of 'All' is encountered, `@UserRail` is set to 'DTL, NEL, SPLRT' and the loop breaks.  
     - Otherwise, lines are concatenated into a comma‑separated string.  
   - **Insert into Temporary Table** – If the user is not already present in `#UserTable`, a row is inserted with the gathered data.  
5. **Cleanup** – All cursors are closed and deallocated.  
6. **Result Return** – The contents of `#UserTable` are selected and returned to the caller.  
7. **Temporary Table Drop** – `#UserTable` is dropped to free resources.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  

* **Writes:**  
  - Temporary table `#UserTable` (inserted rows only; no permanent table modifications)