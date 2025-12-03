# Procedure: sp_TAMS_Get_User_List_By_Line_20211101

### Purpose
This stored procedure retrieves a list of users based on various search criteria, including user type, active status, and module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |
| @SearchRail | NVARCHAR(10) | The rail line to search for. |
| @SearchUserType | NVARCHAR(10) | The user type to filter by. |
| @SearchActive | NVARCHAR(10) | The active status to filter by. |
| @SearchModule | NVARCHAR(10) | The module to filter by. |
| @SearchUserID | NVARCHAR(100) | The user ID to search for. |
| @SearchUserName | NVARCHAR(200) | The username to search for. |

### Logic Flow
1. The procedure starts by creating a temporary table #UserTable to store the retrieved user data.
2. It then declares several variables to hold the user's ID, type, name, and module.
3. A cursor is opened to iterate through the users who match the current user's login ID and the search criteria.
4. For each matching user, the procedure checks if they have access to both TAR and OCC modules. If so, it sets @UModule to 'TAR, OCC'. Otherwise, it sets @UModule to either 'TAR' or 'OCC'.
5. The procedure then retrieves the rail lines for the current user and sets @UserRail to a comma-separated list of these rail lines.
6. If the user is not already in the #UserTable, their data is inserted into the table with the updated @UModule value.
7. The procedure repeats steps 4-6 until all matching users have been processed.
8. Finally, it closes the cursor and deletes the temporary table.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role, TAMS_User u, TAMS_User_Role ur, TAMS_Role r
* **Writes:** #UserTable