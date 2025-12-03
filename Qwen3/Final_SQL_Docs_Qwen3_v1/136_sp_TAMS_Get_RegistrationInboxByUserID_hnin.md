# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_hnin

### Purpose
This stored procedure retrieves a list of registration inbox items for a specific user ID, including relevant workflow statuses and details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the user has a role that includes 'SysAdmin' or 'SysApprover'. If so, it retrieves and inserts relevant data into a temporary table.
2. For roles with 'SysAdmin', it filters for pending company registration and system admin approval workflows, inserting data into the temporary table.
3. For roles with 'SysApprover', it uses a cursor to iterate through the registration items, checking if each item has been updated by the user or not. If not, it inserts the relevant data into the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role