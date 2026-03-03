# Procedure: sp_TAMS_Insert_UserRegRole_SysAdminApproval

### Purpose
Insert a new user registration role record into the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module. |
| @RegRoleID | INT | Identifier of the role to assign. |
| @IsAssigned | BIT | Flag indicating whether the role is currently assigned. |
| @UpdatedBy | INT | Identifier of the user performing the operation. |

### Logic Flow
1. Begin a TRY block and start a database transaction.  
2. Declare three local variables: @WorkflowID, @NewWFStatusID, and @EndorserID.  
3. (Commented out) Code that would normally determine the next workflow stage and endorser for the given registration module.  
4. Insert a new row into TAMS_Reg_Role using the supplied parameters, an empty string for the remarks field, the current date/time for CreatedDate and UpdatedDate, and @UpdatedBy for both CreatedBy and UpdatedBy.  
5. Commit the transaction.  
6. If any error occurs, roll back the transaction in the CATCH block.

### Data Interactions
* **Reads:** None (the SELECT statements are commented out).  
* **Writes:** TAMS_Reg_Role.