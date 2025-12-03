# Procedure: sp_TAMS_Get_User_RailLine_Depot

### Purpose
This stored procedure retrieves the rail line and depot information for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user ID to retrieve information for. |

### Logic Flow
1. The procedure first checks if the provided user ID exists in the TAMS_User_Role table with a Line value of 'All' and matches the user's LoginID.
2. If the user has a role that includes all lines, it returns a hardcoded value 'NEL' as the rail line.
3. If the user does not have a role that includes all lines, it retrieves the distinct Line values from the TAMS_User_Role table where the UserID matches the provided ID and TrackType is 'Depot'.
4. The procedure then returns these Line values as the rail line.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User
* **Writes:** None