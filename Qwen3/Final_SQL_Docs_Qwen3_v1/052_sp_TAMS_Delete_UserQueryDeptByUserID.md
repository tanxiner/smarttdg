# Procedure: sp_TAMS_Delete_UserQueryDeptByUserID

### Purpose
This stored procedure deletes all user query departments associated with a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user whose query departments are to be deleted. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then checks if there exists any record in the TAMS_User_QueryDept table where the UserID matches the input parameter @UserID.
3. If such a record exists, it deletes all records from the TAMS_User_QueryDept table where the UserID is equal to @UserID.
4. After deleting the records, the procedure commits the transaction.

### Data Interactions
* **Reads:** TAMS_User_QueryDept
* **Writes:** TAMS_User_QueryDept