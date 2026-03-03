# Procedure: SP_TAMS_Depot_GetUserAccess

### Purpose
This stored procedure retrieves access information for a specified user at a depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username to check for access. |

### Logic Flow
1. The procedure checks if the provided username exists in the TAMS_User table.
2. If the user exists, it sets the output parameter @res to 1, indicating that the user has access.
3. If the user does not exist, it sets the output parameter @res to 0, indicating that the user does not have access.

### Data Interactions
* **Reads:** TAMS_User table