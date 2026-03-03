# Procedure: sp_TAMS_Update_UserRegRole_SysOwnerApproval

### Purpose
Updates the assignment status of a role for a specific registration module and, when assigned, ensures the corresponding user role record exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module to be updated |
| @RegRoleID | INT | Identifier of the role being assigned or unassigned |
| @IsAssigned | BIT | Flag indicating whether the role is being assigned (1) or unassigned (0) |
| @RejectRemarks | NVARCHAR(MAX) | Text explaining the reason for rejection when unassigning |
| @UpdatedBy | INT | Identifier of the user performing the update |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Retrieve the **UserID** of the user who owns the registration that the supplied **@RegModID** belongs to.  
3. Load the **Line** and **TrackType** values for the module identified by **@RegModID**.  
4. Fetch the module’s **RegID**, **Line**, **Module**, and **RegStatus**.  
5. Decrease the **RegStatus** by one to target the previous status level.  
6. Find the module ID that matches the same **RegID**, **Line**, **Module**, and the decremented **RegStatus**; this becomes the new **@RegModID** for the update.  
7. Verify that a role record exists for this module and role ID.  
   - If it exists, update the **IsAssigned**, **UpdatedOn**, **RejectReason**, and **UpdatedBy** fields.  
   - If **@IsAssigned** is true, check whether a user‑role record already exists for the user, line, and role.  
     - If not, insert a new record into **TAMS_User_Role** with the current date and a status flag of 1.  
8. Commit the transaction.  
9. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_Role, TAMS_User_Role  
* **Writes:** TAMS_Reg_Role (UPDATE), TAMS_User_Role (INSERT)