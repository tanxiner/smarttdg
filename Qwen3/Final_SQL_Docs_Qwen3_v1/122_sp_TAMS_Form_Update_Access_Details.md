# Procedure: sp_TAMS_Form_Update_Access_Details

### Purpose
This stored procedure updates access details for a TAMS TAR record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | Company name |
| @Designation | NVARCHAR(50) | Designation of the user |
| @Name | NVARCHAR(50) | User's name |
| @OfficeNo | NVARCHAR(50) | Office number of the user |
| @MobileNo | NVARCHAR(50) | Mobile number of the user |
| @Email | NVARCHAR(50) | Email address of the user |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access |
| @AccessTimeTo | NVARCHAR(50) | End time of access |
| @IsExclusive | INT | Flag indicating exclusive access |
| @DescOfWork | NVARCHAR(100) | Description of work |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating involvement with power |
| @PowerOn | INT | Flag indicating power on status |
| @Is13ASocket | INT | Flag indicating 13A socket usage |
| @CrossOver | INT | Flag indicating cross-over status |
| @UserID | NVARCHAR(100) | Login ID of the user |
| @TARID | BIGINT | ID of the TAMS TAR record to update |

### Logic Flow
1. The procedure starts by initializing a transaction flag and checking if a transaction is already in progress.
2. It then retrieves the Userid from the TAMS_User table based on the provided UserID.
3. The procedure updates the specified fields of the TAMS_TAR table with the new values, including the updated timestamp and user ID.
4. If any errors occur during the update process, an error message is set and the transaction is rolled back.
5. Otherwise, the transaction is committed and the procedure returns the error message.

### Data Interactions
* **Reads:** TAMS_User table (to retrieve Userid)
* **Writes:** TAMS_TAR table (to update access details)