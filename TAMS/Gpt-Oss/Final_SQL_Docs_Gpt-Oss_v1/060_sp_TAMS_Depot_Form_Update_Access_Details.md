# Procedure: sp_TAMS_Depot_Form_Update_Access_Details

### Purpose
Updates a single TAMS_TAR record with new access and contact details for a depot form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | New company name |
| @Designation | NVARCHAR(50) | New designation |
| @Name | NVARCHAR(50) | New name |
| @OfficeNo | NVARCHAR(50) | New office number |
| @MobileNo | NVARCHAR(50) | New mobile number |
| @Email | NVARCHAR(50) | New email address |
| @AccessTimeFrom | NVARCHAR(50) | New start time for access |
| @AccessTimeTo | NVARCHAR(50) | New end time for access |
| @IsExclusive | INT | Flag indicating exclusive access |
| @DescOfWork | NVARCHAR(100) | Description of work |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating power involvement |
| @PowerOn | INT | Flag indicating power on status |
| @Is13ASocket | INT | Flag indicating 13A socket usage |
| @CrossOver | INT | Flag indicating crossover usage |
| @UserID | NVARCHAR(20) | Login identifier of the user performing the update |
| @ProtectionType | NVARCHAR(50) | Type of protection applied |
| @TARID | BIGINT | Primary key of the TAMS_TAR record to update |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error |

### Logic Flow
1. Initialise a transaction flag `@IntrnlTrans` to 0.  
2. If the procedure is called outside an existing transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Resolve the internal numeric user identifier `@UserIDID` by selecting `Userid` from `TAMS_User` where `LoginId` matches the supplied `@UserID`.  
4. Execute an `UPDATE` on `TAMS_TAR` setting all supplied columns to the corresponding parameters, and updating `UpdatedOn` to the current date/time and `UpdatedBy` to the resolved `@UserIDID`. The update targets the row where `ID = @TARID`.  
5. If the update raises an error (`@@ERROR <> 0`), set `@Message` to a generic error string and jump to the error handling section.  
6. If no error occurs, commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
7. Return the (potentially empty) `@Message`.  
8. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `TAMS_User` (to map `LoginId` to `Userid`)  
* **Writes:** `TAMS_TAR` (record identified by `ID = @TARID`)