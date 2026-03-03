# Procedure: sp_TAMS_TOA_Add_ProtectionType

### Purpose
Adds a protection type to a TOA record and refreshes its associated point numbers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | dbo.Point readonly | Table of point numbers to associate with the TOA. |
| @protectiontype | char(5) | New protection type value to set on the TOA. |
| @toaid | int | Identifier of the TOA record to update. |
| @Message | nvarchar(500) OUTPUT | Returns status or error message. |
| @CreatedBy | nvarchar(50) | User who is performing the update, stored with new point rows. |

### Logic Flow
1. Initialise an internal transaction flag to 0.  
2. If no outer transaction is active, set the flag to 1 and begin a new transaction.  
3. Clear the @Message variable.  
4. Update the TAMS_TOA row whose Id equals @toaid, setting its ProtectionType to @protectiontype.  
5. Delete all rows from TAMS_TOA_PointNo that reference @toaid.  
6. Insert a new row into TAMS_TOA_PointNo for each point number supplied in @pointno, recording the current date and @CreatedBy.  
7. Reset @Message to an empty string.  
8. If any error occurred during the update, delete, or insert steps, set @Message to a generic error string and jump to the error handling section.  
9. If the internal transaction flag is set, commit the transaction.  
10. Return @Message.  
11. In the error handling section, if the internal transaction flag is set, roll back the transaction and return @Message.

### Data Interactions
* **Reads:** TAMS_TOA (to locate the row for update).  
* **Writes:** TAMS_TOA (updates ProtectionType), TAMS_TOA_PointNo (deletes old point rows and inserts new ones).