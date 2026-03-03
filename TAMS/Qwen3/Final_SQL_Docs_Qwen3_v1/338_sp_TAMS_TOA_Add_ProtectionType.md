# Procedure: sp_TAMS_TOA_Add_ProtectionType

### Purpose
This stored procedure adds a new protection type to the TAMS_TOA table and updates related data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | dbo.Point | The point number to be associated with the new protection type. |
| @protectiontype | char(5) | The new protection type to be added. |
| @toaid | int | The ID of the TAMS_TOA record to which the new protection type is being added. |
| @Message | NVARCHAR(500) | An output parameter that contains a message indicating whether the operation was successful or not. |
| @CreatedBy | nvarchar(50) | The user who created the new protection type. |

### Logic Flow
1. The procedure starts by checking if there are any open transactions. If not, it sets an internal transaction flag to 1.
2. It then updates the TAMS_TOA record with the specified ID and new protection type.
3. Next, it deletes all existing point numbers associated with the same TAMS_TOA record.
4. After that, it inserts a new point number into the TAMS_TOA_PointNo table, linking it to the updated TAMS_TOA record.
5. The procedure then checks if any errors occurred during this process. If so, it sets an error message and skips the rest of the procedure.
6. Finally, if no errors occurred, the procedure commits the internal transaction (if one was started) and returns a success message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_PointNo tables
* **Writes:** TAMS_TOA, TAMS_TOA_PointNo tables