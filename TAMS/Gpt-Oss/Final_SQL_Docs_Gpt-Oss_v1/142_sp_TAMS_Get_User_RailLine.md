# Procedure: sp_TAMS_Get_User_RailLine

### Purpose
Returns the list of rail lines a specified user is authorized to access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The login identifier of the user whose rail line access is being queried. |

### Logic Flow
1. The procedure checks whether the user has a role entry with the line value set to `'All'`.  
2. If such an entry exists, the procedure returns a fixed set of rail lines: `'DTL'`, `'NEL'`, and `'SPLRT'`.  
3. If no `'All'` role is found, the procedure retrieves the distinct rail lines from the user‑role mapping that belong to the specified user.  

### Data Interactions
* **Reads:** `TAMS_User_Role`, `TAMS_User`  
* **Writes:** None  

---