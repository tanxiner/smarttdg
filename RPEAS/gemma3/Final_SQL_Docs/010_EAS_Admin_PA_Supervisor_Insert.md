# Procedure: EAS_Admin_PA_Supervisor_Insert

### Purpose
This procedure allows an administrator to manage PA Supervisor lists by either updating an existing record or deleting a record based on specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PAID | VARCHAR(50) | The unique identifier for the PA. |
| @SupervisorLanID | VARCHAR(50) | The unique identifier for the Supervisor. |
| @Active | SMALLINT | A flag indicating whether the PA Supervisor record is active. |
| @LoginID | VARCHAR(50) | The identifier of the user making the change. |
| @Sel | VARCHAR(5) |  A selection indicator, likely determining the action to take. |
| @P_ErrorMsge | VARCHAR(225) | An output parameter to hold any error messages. |

### Logic Flow
1.  The procedure initializes the `@P_ErrorMsge` output parameter to an empty string.
2.  It enters a TRY block to handle potential errors and begins a transaction.
3.  If the `@Sel` parameter is equal to 'Y', the procedure checks if a record already exists in the `EAS_PA_Supervisor` table with the specified `@PAID` and `@SupervisorLanID`.
    *   If the record exists, the procedure updates the `EAS_PA_Supervisor` record, setting the `@Active` flag to the value of the `@Active` parameter, the `Updatedby` field to the `@LoginID`, and the `updatedON` field to the current date and time.
    *   If the record does not exist, the procedure inserts a new record into the `EAS_PA_Supervisor` table, using the `SYSID` value 'RPEAS', the `@PAID`, the `@SupervisorLanID`, the `@Active` value, the current date and time for `CreatedOn`, the `@LoginID` for `CreatedBy`, the current date and time for `UpdatedOn`, and the `@LoginID` for `UpdatedBy`.
4.  If the `@Sel` parameter is not 'Y', the procedure deletes records from the `EAS_PA_Supervisor` table where the `UserID` matches the `@PAID` and the `SupervisorID` matches the `@SupervisorLanID`.
5.  The transaction is committed.
6.  If an error occurs within the TRY block, the CATCH block is executed. The error message is retrieved and stored in the `@P_ErrorMsge` output parameter. The transaction is rolled back.
7.  The `@P_ErrorMsge` output parameter is set to the value of `@P_ErrorMsge`, handling the case where no error occurred.

### Data Interactions
*   **Reads:** `EAS_PA_Supervisor`
*   **Writes:** `EAS_PA_Supervisor`