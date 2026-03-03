# Procedure: sp_TAMS_Get_User_List_By_Line

### Purpose
This stored procedure retrieves a list of users based on various search criteria, including user type, active status, and module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |
| @SearchRail | NVARCHAR(10) | The rail line to search for. Can be 'ALL' or a specific value. |
| @SearchUserType | NVARCHAR(10) | The user type to filter by (e.g., Internal, External). |
| @SearchActive | NVARCHAR(10) | The active status to filter by (e.g., 1 for active, 0 for inactive). Can be '%1%', '%0%', or 'ALL'. |
| @SearchModule | NVARCHAR(10) | The module to search for. |
| @SearchUserID | NVARCHAR(100) | The user ID to search for. |
| @SearchUserName | NVARCHAR(200) | The username to search for. |

### Logic Flow
1. The procedure starts by creating a temporary table #UserTable to store the results.
2. It then declares several variables to hold intermediate results and initializes them with default values.
3. The procedure retrieves a list of user lines from the TAMS_User_Role table, grouped by role line, for the current user's login ID.
4. If the search rail is 'ALL', it retrieves all non-'All' user lines; otherwise, it uses the provided search rail value.
5. It then opens a cursor to iterate over the users in the retrieved list and performs the following steps:
	* Retrieves the module(s) associated with each user's role ID.
	* Checks if the user has access to TAR, OCC, or DCC modules; if so, sets the @UModule variable accordingly.
	* If the user does not have access to any of these modules, it sets @UModule to a default value (e.g., 'TAR, OCC, DCC').
	* Retrieves the rail line(s) associated with each user's role ID and updates the @UserRail variable accordingly.
	* Inserts the user into the #UserTable if they do not already exist.
6. The procedure closes all cursors and deletes the temporary table.

### Data Interactions
* Reads: TAMS_User, TAMS_User_Role, TAMS_Role
* Writes: None