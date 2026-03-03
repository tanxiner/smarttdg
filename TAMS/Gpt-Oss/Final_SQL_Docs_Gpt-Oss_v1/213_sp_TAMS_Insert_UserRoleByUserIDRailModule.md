# Procedure: sp_TAMS_Insert_UserRoleByUserIDRailModule

### Purpose
Insert a user‑role assignment for a rail module when the assignment does not already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | Identifier of the user |
| @Rail | NVARCHAR(10) | Rail identifier to store |
| @TrackType | NVARCHAR(50) | Track type to store |
| @Module | NVARCHAR(10) | Module identifier (unused in logic) |
| @RoleID | INT | Identifier of the role to assign |
| @UpdatedBy | INT | Identifier of the user performing the update |

### Logic Flow
1. Begin a TRY block and start a transaction.  
2. Check if a record exists in **TAMS_User_Role** where **UserID** equals @UserID and **RoleID** equals @RoleID.  
3. If no such record exists, insert a new row into **TAMS_User_Role** with the supplied @UserID, @RoleID, @Rail, @TrackType, current date for creation and update timestamps, and @UpdatedBy for both CreatedBy and UpdatedBy fields.  
4. Commit the transaction.  
5. If any error occurs, roll back the transaction in the CATCH block.

### Data Interactions
* **Reads:** TAMS_User_Role  
* **Writes:** TAMS_User_Role  

---