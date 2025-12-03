# Procedure: sp_TAMS_Insert_RegQueryDept_SysOwnerApproval

### Purpose
This stored procedure inserts a new record into the TAMS_Reg_QueryDept table, which is used to track departmental queries for registered modules. It also checks if a user query department record already exists and inserts one if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registered module being inserted into the TAMS_Reg_QueryDept table. |
| @RegRoleID | INT | The role ID associated with the departmental query. |
| @Dept | NVARCHAR(200) | The name of the department for which a query is being tracked. |
| @UpdatedBy | INT | The user ID who last updated the record. |

### Logic Flow
1. The procedure starts by beginning a transaction to ensure data consistency.
2. It retrieves the user ID associated with the login ID used in the TAMS_Registration table, linked to the registered module being inserted.
3. A new record is inserted into the TAMS_Reg_QueryDept table with the provided departmental query details and timestamps for creation and update.
4. The procedure checks if a user query department record already exists for the same user ID, role ID, and department.
5. If no existing record is found, a new record is inserted into the TAMS_User_QueryDept table.
6. Finally, the transaction is committed to save the changes.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_QueryDept, TAMS_User_QueryDept
* **Writes:** TAMS_Reg_QueryDept, TAMS_User_QueryDept