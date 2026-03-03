# Procedure: sp_TAMS_Delete_RegQueryDept_SysOwnerApproval

### Purpose
Removes a system‑owner approval record for a specific registration module and role, rolling back to the previous approval status level.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the current registration module record. |
| @RegRoleID | INT | Identifier of the role whose approval is to be removed. |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Retrieve the current module’s `RegID`, `Line`, `Module`, and `RegStatus` from `TAMS_Reg_Module` using the supplied `@RegModID`.  
3. Decrease the retrieved `RegStatus` by one to target the previous approval level.  
4. Locate the module record that matches the same `RegID`, `Line`, and `Module` but has the decremented `RegStatus`; update `@RegModID` with this record’s ID.  
5. Check if a record exists in `TAMS_Reg_QueryDept` for the new `@RegModID` and the supplied `@RegRoleID`.  
6. If such a record exists, delete it.  
7. Commit the transaction.  
8. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_Reg_Module`, `TAMS_Reg_QueryDept`  
* **Writes:** `TAMS_Reg_QueryDept` (DELETE)