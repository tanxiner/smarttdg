# Procedure: sp_TAMS_Insert_RegQueryDept_SysAdminApproval

### Purpose
Insert a new department approval record for a registration module and role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module. |
| @RegRoleID | INT | Identifier of the registration role. |
| @Dept | NVARCHAR(200) | Name of the department to approve. |
| @UpdatedBy | INT | User ID performing the insert. |

### Logic Flow
1. Begin a TRY block and start a transaction.  
2. Insert a row into `TAMS_Reg_QueryDept` with the supplied module ID, role ID, department, the current timestamp for `CreatedDate`, the updater ID for `CreatedBy`, the current timestamp for `UpdatedDate`, and the updater ID for `UpdatedBy`.  
3. Commit the transaction.  
4. If any error occurs, catch it and roll back the transaction.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_Reg_QueryDept` (INSERT)