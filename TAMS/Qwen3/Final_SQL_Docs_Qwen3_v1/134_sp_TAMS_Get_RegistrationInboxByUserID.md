# Procedure: sp_TAMS_Get_RegistrationInboxByUserID

### Purpose
This stored procedure retrieves a list of registration inbox items for a specified user ID, including relevant workflow status and details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It initializes a temporary table, #RegistrationTable, to store the retrieved data.
2. It opens two cursors: one for roles with 'SysAdmin' and another for roles with 'SysApprover'.
3. For each role, it iterates through the registration items that match the current role's track type and line.
4. If the item is pending approval by a SysAdmin or SysApprover, it inserts the relevant data into #RegistrationTable.
5. It then fetches the next row from the cursor for the same role and repeats the process until all rows are processed.
6. After processing both cursors, it closes them and deallocates their resources.
7. Finally, it selects distinct registration items from #RegistrationTable and drops the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role