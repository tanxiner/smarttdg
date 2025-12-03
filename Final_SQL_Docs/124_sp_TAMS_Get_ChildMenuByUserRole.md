# Procedure: sp_TAMS_Get_ChildMenuByUserRole

### Purpose
Retrieve the list of level‑2 child menus that a user is authorized to see, optionally filtered by an internet flag.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @UserID   | NVARCHAR(100) | Login identifier of the user whose roles are evaluated. |
| @MenuID   | NVARCHAR(100) | Identifier of the parent menu whose children are requested. |
| @IsInternet | NVARCHAR(1) | Flag (1 or 0) indicating whether to include only internet‑enabled menus. |

### Logic Flow
1. Initialise an empty string to hold role codes.  
2. Create a temporary table to store distinct role IDs for the supplied user.  
3. Populate the temporary table by joining the user, role, and user‑role tables on matching IDs and filtering by the supplied login ID.  
4. Concatenate the role codes from the temporary table into a comma‑separated list, trimming the trailing comma.  
5. If the role list is not empty:  
   1. Build a dynamic SELECT statement that pulls menu records from the menu table where:  
      * The menu is active.  
      * The menu level equals 2.  
      * The parent menu matches @MenuID.  
      * The menu ID and module ID are present in the menu‑role table for any of the user’s roles.  
      * If @IsInternet equals 1, the menu must also be internet‑enabled.  
   2. Execute the dynamic statement.  
   3. Drop the temporary table.  
6. If the role list is empty:  
   1. Return a static set of menus with IDs 'Application', 'Apply TRF', and 'Logout', applying the same level, parent, active, and internet filters as above.

### Data Interactions
* **Reads:**  
  - TAMS_User_Role  
  - TAMS_User  
  - TAMS_Role  
  - TAMS_Menu  
  - TAMS_Menu_Role  
  - Menu (alias for TAMS_Menu in the fallback query)  

* **Writes:** None. The procedure only performs SELECT operations and temporary table creation.