# Procedure: sp_TAMS_Get_RegistrationInformationByRegModuleID

### Purpose
Retrieve registration details, previous module information, associated roles, and query departments for a given registration module ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModuleID | INT | Identifier of the registration module to query |

### Logic Flow
1. Verify that a record exists in **TAMS_Reg_Module** with the supplied ID.  
2. If found, perform a join between **TAMS_Registration**, **TAMS_Reg_Module**, and **TAMS_WFStatus** to return all registration fields, module metadata, and the current workflow status where the workflow type is *UserRegStatus* and the line matches the module line.  
3. Capture the module’s RegID, Line, TrackType, Module, and RegStatus into local variables.  
4. Decrement the captured RegStatus by one to identify the preceding status.  
5. Locate the previous module record that shares the same RegID, Line, and Module but has the decremented RegStatus, storing its ID in @PrevRegModuleID.  
6. If a role record exists for @PrevRegModuleID in **TAMS_Reg_Role**, return all role fields joined with **TAMS_Role** to provide role names and descriptions.  
7. If a query‑department record exists for @PrevRegModuleID in **TAMS_Reg_QueryDept**, return those records.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration, TAMS_WFStatus, TAMS_Reg_Role, TAMS_Role, TAMS_Reg_QueryDept  
* **Writes:** None