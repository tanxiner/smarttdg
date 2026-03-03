# Procedure: sp_TAMS_Get_RegistrationInformationByRegModuleID

### Purpose
This stored procedure retrieves registration information for a specific module ID, including relevant details from TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Reg_Role, and TAMS_Reg_QueryDept tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModuleID | INT | The ID of the module for which to retrieve registration information. |

### Logic Flow
1. Check if a record exists in TAMS_Reg_Module with the specified RegModuleID.
2. If a record exists, select relevant details from TAMS_Registration, TAMS_WFStatus, and TAMS_Reg_Module tables based on the RegId, Line, Module, and RegStatus columns.
3. Extract specific values from TAMS_Reg_Module for use in subsequent steps.
4. Update the RegStatus value by subtracting 1.
5. Retrieve the ID of the previous module with matching RegId, Line, Module, and RegStatus values.
6. Check if a record exists in TAMS_Reg_Role with the previously retrieved RegModID.
7. If a record exists, select relevant details from TAMS_Reg_Role and TAMS_Role tables based on the RegRoleID column.
8. Check if a record exists in TAMS_Reg_QueryDept with the previously retrieved RegModID.
9. Return results.

### Data Interactions
* **Reads:** 
	+ TAMS_Registration table
	+ TAMS_Reg_Module table
	+ TAMS_WFStatus table
	+ TAMS_Reg_Role table
	+ TAMS_Reg_QueryDept table
* **Writes:** None