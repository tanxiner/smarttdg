# Procedure: EAS_Admin_Role_Delete

### Purpose
This procedure removes associated data related to a specified administrative role from multiple tables within the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The name of the administrative role to be deleted. |
| @P_ErrorMsg | Varchar(250) |  A variable to store any error messages that occur during the procedure execution. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the data deletion process.
2.  A transaction is initiated within the `TRY` block to ensure atomicity – either all operations succeed, or none do.
3.  The procedure attempts to delete records from the `EAS_Menu_Role` table where the `Role` column matches the provided `@Role` value.
4.  Next, it attempts to delete records from the `EAS_User_Role` table, again matching the `@Role` value.
5.  Finally, it attempts to delete records from the `EAS_Role` table, using the same `@Role` value.
6.  If any error occurs during these deletion operations, the `CATCH` block is executed.
7.  Within the `CATCH` block, the error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` variable.
8.  A `ROLLBACK TRANSACTION` command is executed to undo any changes made during the transaction, ensuring data consistency.
9.  The `@P_ErrorMsg` variable is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
* **Reads:** None
* **Writes:** `EAS_Menu_Role`, `EAS_User_Role`, `EAS_Role`