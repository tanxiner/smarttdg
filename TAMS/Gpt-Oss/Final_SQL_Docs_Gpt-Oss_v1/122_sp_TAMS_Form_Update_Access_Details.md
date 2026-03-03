# Procedure: sp_TAMS_Form_Update_Access_Details

### Purpose
Updates a single TAR record with new access and contact details, recording who made the change.

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
| @DescOfWork | NVARCHAR(100) | Description of work to be performed |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating power involvement |
| @PowerOn | INT | Flag indicating power on status |
| @Is13ASocket | INT | Flag indicating 13A socket requirement |
| @CrossOver | INT | Flag indicating crossover requirement |
| @UserID | NVARCHAR(100) | Login identifier of the user performing the update |
| @TARID | BIGINT | Primary key of the TAR record to update |
| @Message | NVARCHAR(500) OUTPUT | Status or error message returned to caller |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If the procedure is called without an existing transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and start a new transaction.  
3. Resolve the numeric user identifier `@UserIDID` by selecting `Userid` from `TAMS_User` where `LoginId` matches the supplied `@UserID`.  
4. Update the `TAMS_TAR` row whose `ID` equals `@TARID`, setting each column to the corresponding input value and recording the current date/time in `UpdatedOn` and the resolved user id in `UpdatedBy`.  
5. If the update raises an error (`@@ERROR <> 0`), set `@Message` to a generic error string and jump to the error handling section.  
6. On normal completion, commit the transaction if it was started internally (`@IntrnlTrans = 1`) and return the (empty) `@Message`.  
7. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `TAMS_User` (to resolve `Userid`), `TAMS_TAR` (implicit read for the update condition).  
* **Writes:** `TAMS_TAR` (single row update).