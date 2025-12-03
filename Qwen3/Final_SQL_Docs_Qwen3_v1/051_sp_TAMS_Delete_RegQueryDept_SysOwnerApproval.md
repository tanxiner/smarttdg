# Procedure: sp_TAMS_Delete_RegQueryDept_SysOwnerApproval

The procedure deletes a record from TAMS_Reg_QueryDept based on the provided RegModID and RegRoleID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the module to be deleted. |
| @RegRoleID | INT | The ID of the role to be deleted. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then retrieves the RegId, Line, Module, and RegStatus from TAMS_Reg_Module for the provided RegModID.
3. The RegStatus is decremented by 1.
4. The procedure checks if there exists a record in TAMS_Reg_QueryDept with the same RegModID and RegRoleID as the current record.
5. If such a record exists, it is deleted from TAMS_Reg_QueryDept.
6. Finally, the transaction is committed.

### Data Interactions
* **Reads:** TAMS_Reg_Module
* **Writes:** TAMS_Reg_QueryDept