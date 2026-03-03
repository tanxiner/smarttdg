# Procedure: sp_TAMS_TOA_Update_Details

### Purpose
This stored procedure updates details of a TAMS TOA record, including mobile number and tetra radio number, based on the provided ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @MobileNo | NVARCHAR(50) | Mobile number to update |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number to update |
| @UserID | NVARCHAR(20) | User ID for updating record |
| @TOAID | BIGINT | ID of the TAMS TOA record to update |
| @Message | NVARCHAR(500) | Error message output |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a transaction if no existing one is found.
2. It then updates the specified fields in the TAMS_TOA table based on the provided ID, including mobile number and tetra radio number.
3. If any error occurs during this update process, it sets an error message output parameter and jumps to the TRAP_ERROR label.
4. After successful update or if an error occurred, the procedure checks the internal transaction flag. If a transaction was started, it commits the changes; otherwise, it returns the error message.
5. If an error occurred during the update process, the procedure rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA]
* **Writes:** [dbo].[TAMS_TOA]