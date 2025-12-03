# Procedure: sp_TAMS_GetOCCRosterByLineAndRole

### Purpose
This stored procedure retrieves a list of users assigned to specific roles within the OCC (Operations Control Center) module, filtered by line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter results by. |
| @TrackType | nvarchar(50) | The track type to filter results by. |
| @Role | nvarchar(50) | The role to filter results by. |

### Logic Flow
1. The procedure first determines the RoleID associated with the specified @Role.
2. It then selects users (u.userid, ur.Line, [name]) from TAMS_User and TAMS_User_Role, joined on UserID and RoleID, where the user is active and valid until the current date.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Roster_Role, TAMS_Role