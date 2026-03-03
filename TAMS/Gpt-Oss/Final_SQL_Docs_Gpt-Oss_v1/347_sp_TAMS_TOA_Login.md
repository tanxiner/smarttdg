# Procedure: sp_TAMS_TOA_Login

### Purpose
Retrieves system parameters for a login session while ensuring transactional integrity.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARNo | NVARCHAR(50) | Identifier for the TAR (unused in current logic) |
| @TPOPCNRIC | NVARCHAR(50) | National ID for the user (unused in current logic) |
| @Message | NVARCHAR(500) OUTPUT | Returns status or error message |

### Logic Flow
1. Declare a flag @IntrnlTrans to track if the procedure starts its own transaction.  
2. Initialize @IntrnlTrans to 0.  
3. If no transaction is active (`@@TRANCOUNT = 0`), set @IntrnlTrans to 1 and begin a new transaction.  
4. Execute a `SELECT *` from TAMS_Parameters to load configuration values.  
5. If the SELECT raises an error, set @Message to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. If no error occurs, commit the transaction if it was started internally and return @Message.  
7. In the error handling section, rollback the transaction if it was started internally and return @Message.

### Data Interactions
* **Reads:** TAMS_Parameters  
* **Writes:** None  

---