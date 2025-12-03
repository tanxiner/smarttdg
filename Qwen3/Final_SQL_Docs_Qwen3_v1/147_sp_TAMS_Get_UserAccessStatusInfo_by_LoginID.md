# Procedure: sp_TAMS_Get_UserAccessStatusInfo_by_LoginID

### Purpose
This stored procedure retrieves user access status information for a given login ID, including approved and pending approvals.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve access status information for. |

### Logic Flow
1. Check if the provided login ID exists in the TAMS_User table.
2. If it does, select the corresponding user ID from the TAMS_User table.
3. Open a cursor to iterate through distinct lines, track types, and modules from the TAMS_Role table where the line is not 'All' and the role is active (1).
4. For each iteration:
   - Check if the current user has access to the current line, track type, and module by joining the TAMS_User_Role table.
   - If they do, insert a new record into the #AccessStatus temporary table with an approved status.
   - If they don't, check if there is a registration associated with the login ID, line, track type, and module that has not been approved or rejected.
     - If such a registration exists, insert a new record into the #AccessStatus temporary table with a pending approval status.
5. Repeat steps 3-4 until all lines, track types, and modules have been processed.
6. Close and deallocate the cursor.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Role, TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus