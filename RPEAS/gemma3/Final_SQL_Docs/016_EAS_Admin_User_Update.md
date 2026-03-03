# Procedure: EAS_Admin_User_Update

### Purpose
This procedure updates user information within the EAS system, specifically targeting records associated with the "RPEAS" system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(10) | The unique identifier for the user record to be updated. |
| @Name | VARCHAR(200) | The new name for the user. |
| @BArea | VARCHAR(250) | The new business area for the user. |
| @Dept | VARCHAR(250) | The new department for the user. |
| @Section | VARCHAR(250) | The new section for the user. |
| @Email | VARCHAR(500) | The new email address for the user. |
| @Designation | VARCHAR(100) | The new job title for the user. |
| @Active | VARCHAR(5) | The active status for the user. |
| @CreatedBy | VARCHAR(50) | The identifier of the user making the update. |
| @P_ErrorMsg | Varchar(250) | Output parameter to hold any error messages. |

### Logic Flow
1.  The procedure begins within a `TRY` block to manage potential errors.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  An `UPDATE` statement modifies the `EAS_User` table. It sets the `Name`, `Email`, `Designation`, `BusinessArea`, `Department`, `Section`, `Active`, `UpdatedOn`, and `UpdatedBy` columns for the user record identified by the `@User` parameter. The `sysid` column is set to 'RPEAS'.
4.  The `WHERE` clause of the `UPDATE` statement ensures that the update only applies to the user record with the specified `@User` and `sysid` of 'RPEAS'.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The error message is retrieved using `ERROR_MESSAGE()` and stored in the output parameter `@P_ErrorMsg`.
7.  The transaction is rolled back to undo any changes made during the update process.
8.  The `@P_ErrorMsg` parameter is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
*   **Reads:** `EAS_User`
*   **Writes:** `EAS_User`