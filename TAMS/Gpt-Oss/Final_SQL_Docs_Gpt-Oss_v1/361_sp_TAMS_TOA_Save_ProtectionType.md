# Procedure: sp_TAMS_TOA_Save_ProtectionType

### Purpose
Updates the protection type of a TOA record and removes associated point numbers when the new type is not “B”.

### Parameters
| Name           | Type          | Purpose |
| :---           | :---          | :--- |
| @toaid         | int           | Identifier of the TOA record to modify. |
| @protectiontype | nvarchar(50) | New protection type value to assign. |
| @Message       | nvarchar(500) | Output message indicating success or error. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Clear the output message.  
4. If the supplied protection type is not “B”, delete all rows from `TAMS_TOA_PointNo` that reference the given TOA ID.  
5. Update the `ProtectionType` column of the `TAMS_TOA` row whose `Id` matches the supplied TOA ID.  
6. Reset the output message to an empty string.  
7. If any error occurred during the update or delete, set the message to “ERROR SELECTING PROTECTION TYPE” and jump to the error handling section.  
8. On normal completion, commit the transaction if it was started by this procedure and return the message.  
9. In the error handling section, roll back the transaction if it was started by this procedure and return the message.

### Data Interactions
* **Reads:** `TAMS_TOA`, `TAMS_TOA_PointNo`  
* **Writes:** `TAMS_TOA` (UPDATE), `TAMS_TOA_PointNo` (DELETE)