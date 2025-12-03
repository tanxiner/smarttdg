# Procedure: sp_TAMS_Get_UserAccessStatusInfo_by_LoginID
**Type:** Stored Procedure

The procedure retrieves user access status information based on a login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve access status for |

### Logic Flow
1. Checks if the user exists with the given login ID.
2. If the user exists, retrieves their UserID from the TAMS_User table.
3. Opens a cursor to iterate through the distinct lines, track types, and modules of active roles in the TAMS_Role table where the line is not 'All' and the role is active.
4. For each row in the cursor, checks if the user has access to the current line, track type, and module by joining the TAMS_User_Role table.
5. If the user has access, inserts a new record into the #AccessStatus table with the line, track type, module, and status 'Approved'.
6. If the user does not have access, checks if there is an active registration for the current line, track type, and module that matches the user's login ID.
7. If an active registration exists, inserts a new record into the #AccessStatus table with the line, track type, module, and status 'Pending Approval'.
8. Closes the cursor and deallocates it.

### Data Interactions
* Reads: TAMS_User, TAMS_Role, TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus
* Writes: #AccessStatus