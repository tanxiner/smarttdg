# Procedure: sp_TAMS_Get_User_TrackType_Line

### Purpose
This stored procedure retrieves a list of unique track types associated with a specific user and line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(100) | The line number to filter track types by. |
| @UserId | NVARCHAR(100) | The ID of the user to retrieve track types for. |

### Logic Flow
1. The procedure starts by selecting distinct track types from the TAMS_User_Role and TAMS_User tables.
2. It filters the results to only include rows where the UserID in TAMS_User matches the provided @UserId, and the LoginID in TAMS_User matches the provided @Line.
3. The resulting track types are returned as a list.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User