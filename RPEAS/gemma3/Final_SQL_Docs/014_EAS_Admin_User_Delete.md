# Procedure: EAS_Admin_User_Delete

### Purpose
This procedure deletes a user record from the EAS_User table based on the provided UserID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(15) | The UserID of the user to be deleted. |
| @P_ErrorMsg | VARCHAR(250) | Stores an error message if the deletion fails. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the deletion process.
2.  A transaction is initiated within the `TRY` block to ensure atomicity – either all changes are committed, or none are.
3.  A `DELETE` statement is executed from the `EAS_User` table, removing the row where the `UserID` column matches the value provided in the `@User` parameter.
4.  If the `DELETE` statement executes successfully, the transaction is committed, saving the changes to the database.
5.  If any error occurs during the `DELETE` statement, the `CATCH` block is executed.
6.  Within the `CATCH` block, the error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` parameter.
7.  The transaction is rolled back using `ROLLBACK TRANSACTION`, undoing any changes made during the procedure.
8.  Finally, the `@P_ErrorMsg` parameter is set to an empty string if it was previously null.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_User (deleted)