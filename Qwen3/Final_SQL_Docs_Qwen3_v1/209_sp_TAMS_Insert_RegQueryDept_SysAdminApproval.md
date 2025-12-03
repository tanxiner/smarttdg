# Procedure: sp_TAMS_Insert_RegQueryDept_SysAdminApproval

### Purpose
This stored procedure performs a system-level approval for inserting new records into the TAMS_Reg_QueryDept table, ensuring that only authorized users can make changes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module associated with the query department. |
| @RegRoleID | INT | The ID of the role associated with the query department. |
| @Dept | NVARCHAR(200) | The name of the query department. |
| @UpdatedBy | INT | The ID of the user who initiated the update. |

### Logic Flow
1. The procedure begins by attempting to start a new transaction.
2. It then attempts to insert a new record into the TAMS_Reg_QueryDept table, passing in the provided parameters and current date/time values for creation and last update timestamps.
3. If the insertion is successful, the procedure commits the transaction, effectively making the changes permanent.
4. If any errors occur during the insertion process, the procedure rolls back the transaction, ensuring that no changes are made to the database.

### Data Interactions
* **Reads:** None explicitly listed in this procedure.
* **Writes:** TAMS_Reg_QueryDept table