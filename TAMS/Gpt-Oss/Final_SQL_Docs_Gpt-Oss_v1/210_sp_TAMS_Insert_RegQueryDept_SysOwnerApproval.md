# Procedure: sp_TAMS_Insert_RegQueryDept_SysOwnerApproval

### Purpose
Insert a department query record for a registration module and ensure the corresponding user‑department mapping exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module. |
| @RegRoleID | INT | Role identifier for the query. |
| @Dept | NVARCHAR(200) | Department name to associate with the query. |
| @UpdatedBy | INT | User ID performing the operation. |

### Logic Flow
1. Begin a transaction.  
2. Resolve the user ID (`@UserID`) by selecting the `UserID` from `TAMS_User` where the `LoginID` matches the `LoginID` of the registration record linked to the supplied `@RegModID` via `TAMS_Reg_Module`.  
3. Insert a new row into `TAMS_Reg_QueryDept` with the supplied module ID, role ID, department, current timestamp, and the updater’s ID.  
4. Check if a row already exists in `TAMS_User_QueryDept` for the resolved `@UserID`, the supplied role ID, and department.  
   - If no such row exists, insert a new row into `TAMS_User_QueryDept` with the same values and timestamps.  
5. Commit the transaction.  
6. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_User`, `TAMS_Registration`, `TAMS_Reg_Module`, `TAMS_User_QueryDept`  
* **Writes:** `TAMS_Reg_QueryDept`, `TAMS_User_QueryDept`