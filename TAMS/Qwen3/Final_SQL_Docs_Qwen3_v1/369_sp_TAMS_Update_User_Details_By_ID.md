# Procedure: sp_TAMS_Update_User_Details_By_ID

### Purpose
This stored procedure updates user details in the TAMS_User table based on a provided user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user to be updated. |

### Logic Flow
1. The procedure begins by attempting to start a transaction.
2. It then checks if a record exists in the TAMS_User table with the specified user ID.
3. If a record is found, the procedure updates the corresponding fields (Name, Email, Department, OfficeNo, MobileNo, ValidTo, IsActive, UpdatedBy, and UpdatedOn) with the provided values.
4. After updating the record, the procedure commits the transaction if successful.
5. If any error occurs during the execution of the stored procedure, it rolls back the transaction to maintain database consistency.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table