# Procedure: sp_TAMS_Get_ChildMenuByUserRole_20231009

### Purpose
Retrieve the list of level‑2 child menu items that a specified user is authorized to see, based on the user’s roles.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @UserID   | NVARCHAR(100) | Login identifier of the user whose menu is being requested. |
| @MenuID   | NVARCHAR(100) | Identifier of the parent menu whose children are being queried. |

### Logic Flow
1. Initialise an empty string `@urole` that will hold the user’s role codes.  
2. Create a temporary table `#RoleTbl` with an identity column and a `RoleCode` column.  
3. Populate `#RoleTbl` with the distinct role codes that belong to the user identified by `@UserID`.  
4. Concatenate the role codes from `#RoleTbl` into a single comma‑separated list, each code wrapped in single quotes, and store it in `@urole`.  
5. If `@urole` contains at least one role:  
   1. Build a dynamic SQL statement that selects menu attributes from `TAMS_Menu` where the menu is active, at level 2, and its parent matches `@MenuID`.  
   2. The statement further restricts results to menu IDs and module IDs that appear in `TAMS_Menu_Role` for any of the roles in `@urole`.  
   3. Execute the dynamic statement to return the authorized child menus.  
   4. Drop the temporary table `#RoleTbl`.  
6. If the user has no roles (`@urole` is null or empty):  
   1. Return the default set of child menus (`Application`, `Apply TRF`, `Logout`) that are active, at level 2, and whose parent matches `@MenuID`.  
7. End of procedure.

### Data Interactions
* **Reads:**  
  - `TAMS_User_Role`  
  - `TAMS_User`  
  - `TAMS_Role`  
  - `TAMS_Menu`  
  - `TAMS_Menu_Role`  
  - `Menu` (fallback query)  

* **Writes:**  
  - Temporary table `#RoleTbl` (created and dropped within the procedure)