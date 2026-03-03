# Procedure: getUserInformationByID

### Purpose
This stored procedure retrieves user information, including roles, for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The unique identifier of the user to retrieve information for. |

### Logic Flow
1. Check if a user with the provided UserID exists in the TAMS_User table.
2. If the user exists, perform a join operation on the TAMS_User_Role and TAMS_Role tables to retrieve the user's roles.
3. Filter the results to only include the user with the specified UserID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role