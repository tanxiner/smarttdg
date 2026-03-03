# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_20231009

### Purpose
This stored procedure retrieves a list of registration inbox items for a specified user ID, including relevant details such as registration status and workflow information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It initializes a temporary table, #RegistrationTable, to store the retrieved data.
2. It opens two cursors: one for roles with 'SysAdmin' and another for roles with 'SysApprover'. The cursors iterate through the relevant rows in the TAMS_User_Role table based on the user ID provided.
3. For each role, it checks if the corresponding registration status is pending. If so, it inserts a new row into the #RegistrationTable for that status.
4. For roles with 'SysApprover', it further filters the registration statuses to only include those that require approval by the approver. It then iterates through these filtered rows and updates the #RegistrationTable accordingly.
5. After processing all relevant rows, it closes both cursors and selects distinct rows from the #RegistrationTable for final output.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus