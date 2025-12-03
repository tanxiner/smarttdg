# Procedure: sp_TAMS_Delete_UserRoleByUserID

### Purpose
Delete every role assigned to a specified user except the role with ID 1.

### Parameters
| Name     | Type | Purpose |
| :------- | :--- | :------ |
| @UserID  | INT  | Identifier of the user whose roles are to be removed |

### Logic Flow
1. Start a TRY block and begin a transaction.  
2. Check if any rows exist in **TAMS_User_Role** for the supplied **@UserID**.  
3. If such rows exist, delete all rows for that user where **RoleID** is not equal to 1.  
4. Commit the transaction.  
5. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_User_Role  
* **Writes:** TAMS_User_Role  

---