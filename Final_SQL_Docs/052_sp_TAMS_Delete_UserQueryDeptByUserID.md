# Procedure: sp_TAMS_Delete_UserQueryDeptByUserID

### Purpose
Deletes all query‑department associations for a specified user.

### Parameters
| Name    | Type | Purpose |
| :------ | :--- | :------ |
| @UserID | INT  | Identifier of the user whose query‑department links are to be removed |

### Logic Flow
1. Begin a TRY block to handle potential errors.  
2. Start a database transaction.  
3. Check if any rows exist in **TAMS_User_QueryDept** where **UserID** equals the supplied @UserID.  
4. If such rows exist, delete them from **TAMS_User_QueryDept**.  
5. Commit the transaction to persist the deletion.  
6. If any error occurs during the transaction, catch it and roll back the transaction to leave the database unchanged.

### Data Interactions
* **Reads:** TAMS_User_QueryDept  
* **Writes:** TAMS_User_QueryDept  

---