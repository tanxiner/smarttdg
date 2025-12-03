# Procedure: sp_TAMS_GetOCCRosterByLineAndRole

### Purpose
Retrieve the list of active users assigned to a specific roster role for a given line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The operational line (e.g., DTL, NEL). |
| @TrackType | nvarchar(50) | The type of track associated with the line. |
| @Role | nvarchar(50) | The roster role code to filter users by. |

### Logic Flow
1. Declare an integer variable `@RoleID`.  
2. Query `TAMS_Roster_Role` to find the `RoleId` that matches the supplied `@Role`, `@Line`, and `@TrackType`.  
3. Store the found `RoleId` in `@RoleID`.  
4. Select all users from `TAMS_User` who are active (`IsActive = 1`) and whose validity period (`ValidTo`) is in the future.  
5. Join these users with `TAMS_User_Role` on `Userid`, filtering for rows where `RoleID` equals the previously retrieved `@RoleID`.  
6. Return the columns `userid`, `Line`, and `name`, ordered alphabetically by `name`.  
7. (All commented code is ignored; no additional logic is executed.)

### Data Interactions
* **Reads:** `TAMS_Roster_Role`, `TAMS_User`, `TAMS_User_Role`  
* **Writes:** None

---