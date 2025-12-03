# Procedure: sp_TAMS_Depot_Form_Update_Access_Details

### Purpose
This stored procedure updates access details for a depot form, including company, designation, name, and other relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | Company name to be updated |
| @Designation | NVARCHAR(50) | Designation to be updated |
| @Name | NVARCHAR(50) | Name to be updated |
| @OfficeNo | NVARCHAR(50) | Office number to be updated |
| @MobileNo | NVARCHAR(50) | Mobile number to be updated |
| @Email | NVARCHAR(50) | Email address to be updated |
| @AccessTimeFrom | NVARCHAR(50) | Access time from to be updated |
| @AccessTimeTo | NVARCHAR(50) | Access time to be updated |
| @IsExclusive | INT | Flag indicating exclusive access (0 or 1) |
| @DescOfWork | NVARCHAR(100) | Description of work to be updated |
| @ARRemark | NVARCHAR(1000) | Additional remarks to be updated |
| @InvolvePower | INT | Flag indicating involvement with power (0 or 1) |
| @PowerOn | INT | Flag indicating power on status (0 or 1) |
| @Is13ASocket | INT | Flag indicating 13A socket usage (0 or 1) |
| @CrossOver | INT | Flag indicating cross-over usage (0 or 1) |
| @UserID | NVARCHAR(20) | User ID to be updated |
| @ProtectionType | NVARCHAR(50) | Protection type to be updated |
| @TARID | BIGINT | ID of the TAR record to be updated |
| @Message | NVARCHAR(500) | Error message output |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a transaction if no transactions are already active.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. The procedure then updates the specified fields in the TAMS_TAR table with the provided values, including the updated user ID.
4. If any errors occur during the update process, an error message is set and the transaction is rolled back.
5. Otherwise, the transaction is committed, and the procedure returns the error message.

### Data Interactions
* **Reads:** TAMS_User table (for retrieving user ID)
* **Writes:** TAMS_TAR table (for updating records)