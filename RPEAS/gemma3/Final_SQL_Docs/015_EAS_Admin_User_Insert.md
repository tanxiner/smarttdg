# Procedure: EAS_Admin_User_Insert

### Purpose
This procedure inserts a new user record into the EAS_User table, populating fields with provided data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(10) | The unique identifier for the user. |
| @Name | VARCHAR(200) | The user’s full name. |
| @BArea | VARCHAR(250) | The business area to which the user belongs. |
| @Dept | VARCHAR(250) | The department the user belongs to. |
| @Section | VARCHAR(250) | The section within the department the user belongs to. |
| @Email | VARCHAR(500) | The user’s email address. |
| @Designation | VARCHAR(100) | The user’s job title or designation. |
| @Active | VARCHAR(5) | A flag indicating whether the user account is active. |
| @CreatedBy | VARCHAR(50) | The user who created the record. |
| @P_ErrorMsg | Varchar(250) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins within a `TRY` block to handle potential errors during the insertion process.
2.  A transaction is initiated using `BEGIN TRANSACTION`.
3.  An `INSERT` statement is executed to add a new row to the `EAS_User` table.
4.  The `UserID` column is populated with the lowercase version of the input `@User` parameter.
5.  The `sysid` column is populated with the constant "RPEAS".
6.  The `Name`, `Email`, `Designation`, `BusinessArea`, `Department`, `Section`, `Active`, `CreatedOn`, and `CreatedBy` columns are populated with the corresponding values from the input parameters.
7.  The `Getdate()` function is used to populate the `CreatedOn` column with the current date and time.
8.  If the `INSERT` statement executes successfully, the transaction is committed using `COMMIT TRANSACTION`.
9.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
10. The `ERROR_MESSAGE()` function is called to retrieve the error message.
11. The error message is stored in the output parameter `@P_ErrorMsg`.
12. The transaction is rolled back using `ROLLBACK TRANSACTION` to undo any changes made during the process.
13. The `@P_ErrorMsg` parameter is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_User