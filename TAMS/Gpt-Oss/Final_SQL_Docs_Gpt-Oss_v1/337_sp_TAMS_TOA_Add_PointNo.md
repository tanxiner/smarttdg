# Procedure: sp_TAMS_TOA_Add_PointNo

### Purpose
Adds a new point number record to the TAMS_TOA_PointNo table for a specified TOA.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | nvarchar(200) | The point number to insert. |
| @toaid | int | Identifier of the TOA to associate the point number with. |
| @Message | nvarchar(500) OUTPUT | Receives a status message indicating success or failure. |
| @CreatedBy | nvarchar(50) | Username of the person creating the record. |

### Logic Flow
1. Initialise a flag (`@IntrnlTrans`) to indicate whether the procedure started its own transaction.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set the flag and begin a new transaction.  
3. Clear the output message.  
4. Attempt to insert a new row into `TAMS_TOA_PointNo` with the supplied TOAID, point number, current date, and creator.  
5. If the insert succeeds, keep the message empty.  
6. If an error occurs during the insert, set the message to “ERROR INSERTING TAMS_TOA_PointNo” and jump to the error handling section.  
7. On successful completion, commit the transaction if it was started internally and return the message.  
8. In the error handling section, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_TOA_PointNo` (INSERT)