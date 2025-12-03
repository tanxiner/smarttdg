# Procedure: sp_TAMS_Insert_UserQueryDeptByUserID

### Purpose
This stored procedure inserts a new record into the TAMS_User_QueryDept table if the specified user query department does not already exist for that user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to insert the query department for. |
| @Dept | NVARCHAR(100) | The department code to insert as a new record. |
| @UpdatedBy | INT | The ID of the user who is updating the query department. |

### Logic Flow
1. The procedure checks if a record already exists in the TAMS_User_QueryDept table for the specified user and department.
2. If no record exists, it retrieves the department line from the TAMS_Parameters table based on the provided department code.
3. It then retrieves the role ID from the TAMS_Role table that matches the department line and has a specific pattern (ApplicantHOD).
4. With the role ID in hand, it inserts a new record into the TAMS_User_QueryDept table with the specified user ID, role ID, department code, and update information.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_Role, TAMS_User_QueryDept
* **Writes:** TAMS_User_QueryDept