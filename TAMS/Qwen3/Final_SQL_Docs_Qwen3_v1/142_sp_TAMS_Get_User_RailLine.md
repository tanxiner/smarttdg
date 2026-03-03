# Procedure: sp_TAMS_Get_User_RailLine

### Purpose
This stored procedure retrieves the rail line associated with a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user ID to retrieve the rail line for. |

### Logic Flow
1. The procedure checks if the provided user ID exists in the TAMS_User_Role table and matches a specific condition.
2. If the condition is met, it returns a list of three predefined rail lines ('DTL', 'NEL', and 'SPLRT').
3. If the condition is not met, it retrieves the distinct rail line(s) associated with the user ID from the TAMS_User_Role table.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User