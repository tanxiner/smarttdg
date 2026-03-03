# Procedure: sp_TAMS_Get_ChildMenuByUserRoleID

### Purpose
Retrieve child menu items for a specified parent menu and user role, optionally filtering by internet access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | Identifier used to locate the user’s roles. |
| @MenuID | NVARCHAR(100) | Parent menu identifier to filter child menus. |
| @IsInternet | NVARCHAR(1) | Flag indicating whether to include only internet‑enabled menus. |

### Logic Flow
1. Initialize an empty string @urole to hold a comma‑separated list of role codes.  
2. Create a temporary table #RoleTbl with an identity column ROWID and a RoleCode column.  
3. Populate #RoleTbl with distinct RoleID values from the join of TAMS_User_Role, TAMS_User, and TAMS_Role where the user’s LoginID matches @UserID.  
4. Concatenate each RoleCode from #RoleTbl into @urole, surrounded by single quotes and separated by commas; trim the trailing comma.  
5. If @urole contains values:  
   a. Build a dynamic SELECT statement that pulls MenuID, MenuLevel, DispText, ToolTip, ProgURL, and ParentMenuID from TAMS_Menu where Active = 1, MenuLevel = 2, ParentMenuID equals @MenuID, and the menu is linked to any of the roles in @urole via TAMS_Menu_Role.  
   b. If @IsInternet equals 1, add a filter for IsInternet = 1.  
   c. Include a subquery that restricts ModuleID to those associated with the roles in @urole.  
   d. Execute the dynamic query.  
   e. Drop #RoleTbl.  
6. If @urole is empty or null:  
   a. Select the same columns from Menu where Active = 1, MenuLevel = 2, ParentMenuID equals @MenuID, and either @IsInternet is 0 or the menu’s IsInternet matches @IsInternet.  
   b. Restrict the result to MenuID values 'Application', 'Apply TRF', or 'Logout'.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role, Menu  
* **Writes:** None