# Procedure: sp_TAMS_Insert_UserRoleByUserIDRailModule

### Purpose
This stored procedure inserts a new user role into the TAMS_User_Role table if it does not already exist for a given user ID and role ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to insert the role for. |
| @Rail | NVARCHAR(10) | The rail associated with the role. |
| @TrackType | NVARCHAR(50) | The track type associated with the role. |
| @Module | NVARCHAR(10) | The module associated with the role. |
| @RoleID | INT | The ID of the role to insert. |
| @UpdatedBy | INT | The ID of the user who is updating the role. |

### Logic Flow
1. The procedure checks if a record already exists in the TAMS_User_Role table for the given user ID and role ID.
2. If no record exists, it inserts a new record into the TAMS_User_Role table with the provided values.

### Data Interactions
* **Reads:** TAMS_User_Role table
* **Writes:** TAMS_User_Role table