# Procedure: sp_TAMS_Get_ParentMenuByUserRole

### Purpose
Retrieve the top‑level menu items that a user is authorized to see, optionally filtered by whether the menu is for internet access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | Identifier of the user whose menu is requested. |
| @IsInternet | NVARCHAR(1) | Flag indicating whether to return internet‑enabled menus (1) or all menus (0). |

### Logic Flow
1. Construct a sub‑query (`@usql`) that selects the distinct roles assigned to the supplied user by joining the user, role, and user‑role tables.  
2. Verify that the user has at least one active role.  
   - If the user has roles:  
     a. If `@IsInternet` equals 0, build a dynamic query (`@rsql`) that selects active, level‑1 menu records where the menu is either internet‑enabled or not, and whose display text matches any menu ID linked to the user’s roles in the menu‑role table.  
     b. If `@IsInternet` equals 1, build a similar query but restrict to menus marked as internet‑enabled.  
     c. Execute the dynamic query to return the matching menu rows.  
   - If the user has no roles:  
     Return the three hard‑coded menu items (`Application`, `Apply TRF`, `Logout`) that are always available.  

### Data Interactions
* **Reads:**  
  - TAMS_User_Role  
  - TAMS_User  
  - TAMS_Role  
  - TAMS_Menu  
  - TAMS_Menu_Role  

* **Writes:**  
  None.