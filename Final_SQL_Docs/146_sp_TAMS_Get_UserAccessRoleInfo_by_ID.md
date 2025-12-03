# Procedure: sp_TAMS_Get_UserAccessRoleInfo_by_ID

### Purpose
Retrieves all role assignments for a specified user.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @UserID  | NVARCHAR(100) | Identifier of the user whose role information is requested. |

### Logic Flow
1. Check if a record exists in **TAMS_User** where **UserID** matches the supplied @UserID.  
2. If such a record is found, perform a join between **TAMS_User_Role** (alias ur) and **TAMS_Role** (alias r) on **ur.roleID = r.ID**.  
3. Filter the joined result to rows where **ur.UserID** equals the supplied @UserID.  
4. Return all columns from the joined tables for those rows.  
5. If no matching user is found, the procedure returns no rows.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role  
* **Writes:** None

---