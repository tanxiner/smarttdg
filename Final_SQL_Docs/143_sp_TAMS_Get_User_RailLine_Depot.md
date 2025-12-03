# Procedure: sp_TAMS_Get_User_RailLine_Depot

### Purpose
Return the rail line(s) a user is authorized to access, with special handling for users granted access to all lines.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @UserId  | NVARCHAR(100) | Login identifier of the user whose rail line access is being queried |

### Logic Flow
1. Verify whether the specified user has a role entry where the `Line` field equals `'All'`.  
2. If such an entry exists, output a single row containing the string `'NEL'` as the rail line.  
3. If no `'All'` role is found, retrieve all distinct `Line` values from the role table that belong to the user and where the `TrackType` equals `'Depot'`.  
4. Return the resulting set of rail lines.

### Data Interactions
* **Reads:** `TAMS_User_Role`, `TAMS_User`  
* **Writes:** None