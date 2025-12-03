# Procedure: sp_TAMS_Get_User_List_By_Line

### Purpose
Return a list of users that the current user can view, filtered by rail, user type, activity status, module, user ID, and user name, and include each user’s associated rail(s) and module(s).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | Login ID of the user executing the procedure; used to determine accessible lines. |
| @SearchRail | NVARCHAR(10) | Optional filter for the rail(s) a user belongs to. |
| @SearchUserType | NVARCHAR(10) | Optional filter for internal/external user type. |
| @SearchActive | NVARCHAR(10) | Optional filter for active status (1, 0, or All). |
| @SearchModule | NVARCHAR(10) | Optional filter for the module a user is assigned to. |
| @SearchUserID | NVARCHAR(100) | Optional filter for the user’s login ID. |
| @SearchUserName | NVARCHAR(200) | Optional filter for the user’s name. |

### Logic Flow
1. **Create a temporary table** `#UserTable` to hold the final result set.  
2. **Determine accessible lines** for `@CurrentUser` by joining `TAMS_User`, `TAMS_User_Role`, and `TAMS_Role`.  
   * If the user has a line of `ALL`, replace the list with all distinct lines that are not `All`.  
3. **Open a cursor** over users that satisfy:  
   * belong to one of the accessible lines,  
   * match the supplied name, ID, rail, type, activity, and module filters.  
4. **For each user returned by the cursor**:  
   a. **Collect modules** (`TAR`, `OCC`, `DCC`) assigned to the user by scanning the same three tables.  
      * Set flags for each module and build a comma‑separated string (`@UModule`) that lists all modules the user has.  
   b. **Collect rails** assigned to the user.  
      * If any rail is `All`, set the rail string to `DTL, NEL, SPLRT`.  
      * Otherwise concatenate distinct rails.  
   c. **Insert the user into `#UserTable`** if the user is not already present.  
5. **Close and deallocate** all cursors.  
6. **Return the contents** of `#UserTable`.  
7. **Drop the temporary table**.

### Data Interactions
* **Reads:**  
  * `TAMS_User` – user details.  
  * `TAMS_User_Role` – mapping of users to roles.  
  * `TAMS_Role` – role definitions, including line and module.  
  * `dbo.SPLIT` – helper function to split comma‑separated line lists.  
* **Writes:**  
  * Temporary table `#UserTable` – holds the result set for the duration of the procedure.