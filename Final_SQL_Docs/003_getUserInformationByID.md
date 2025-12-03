# Procedure: getUserInformationByID

### Purpose
Retrieve all user and role details for a specified user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | Identifier of the user to query |

### Logic Flow
1. Check if a record exists in **TAMS_User** where **UserID** matches the supplied @UserID.  
2. If a matching user is found, perform a join across **TAMS_User**, **TAMS_User_Role**, and **TAMS_Role** to gather the user’s role information.  
3. Return the combined result set of user and role columns.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role  
* **Writes:** None