# Procedure: sp_TAMS_TOA_Delete_PointNo

### Purpose
This stored procedure deletes a point from the TAMS_TOA_PointNo table based on the provided TOAID and point ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointid | BIGINT | The ID of the point to be deleted. |
| @TOAID | BIGINT | The ID of the TOA associated with the point to be deleted. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. Initialize a variable `@IntrnlTrans` to 0, which tracks whether a transaction is in progress.
2. Check if a transaction is already active. If not, set `@IntrnalTrans` to 1 and begin a new transaction.
3. Attempt to delete the point from the TAMS_TOA_PointNo table where TOAID matches @TOAID and Id matches @pointid.
4. If an error occurs during deletion, print 'ERROR INSERTING' to the error log, set `@Message` to an error message, and exit the procedure with a trap error.
5. If no errors occur, commit the transaction if one was started.
6. Return the value of `@Message`, which contains any error messages generated.

### Data Interactions
* **Reads:** TAMS_TOA_PointNo table
* **Writes:** TAMS_TOA_PointNo table