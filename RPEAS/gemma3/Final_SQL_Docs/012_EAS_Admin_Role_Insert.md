# Procedure: EAS_Admin_Role_Insert

### Purpose
This procedure inserts a new record into the EAS_Role table, representing an administrative role within the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The name of the administrative role to be created. |
| @RoleDesc | VARCHAR(250) | A description of the administrative role. |
| @Active | VARCHAR(5) | Indicates whether the administrative role is currently active. |
| @CreatedBy | VARCHAR(50) | The user account that initiated the role creation. |
| @P_ErrorMsg | Varchar(250) |  An output parameter to hold any error messages encountered during the procedure execution. |

### Logic Flow
1.  The procedure begins within a `TRY` block to handle potential errors during the role creation process.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  An `INSERT` statement is executed to add a new row to the `EAS_Role` table. The values being inserted are: the provided role name, the string literal "RPEAS", the provided role description, the value of the @Active parameter, the current date and time, and the @CreatedBy parameter, also with the current date and time.
4.  If the `INSERT` statement completes successfully, the transaction is committed, making the changes permanent.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The error message is retrieved using `ERROR_MESSAGE()` and stored in the output parameter @P_ErrorMsg.
7.  The transaction is rolled back, undoing any changes made during the procedure.
8.  The @P_ErrorMsg parameter is set to an empty string if it was previously null.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_Role