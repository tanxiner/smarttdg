# Procedure: sp_TAMS_Depot_Form_Save_Access_Details

### Purpose
Creates a new TAR record for a depot access request and returns the generated TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line identifier |
| @TrackType | NVARCHAR(50) | Type of track involved |
| @AccessDate | NVARCHAR(20) | Date of requested access |
| @AccessTimeSlot | NVARCHAR(50) | Time slot for access |
| @AccessType | NVARCHAR(20) | Category of access |
| @TARType | NVARCHAR(10) | Classification of TAR |
| @Company | NVARCHAR(50) | Company name |
| @Designation | NVARCHAR(50) | Employee designation |
| @Name | NVARCHAR(50) | Employee name |
| @OfficeNo | NVARCHAR(50) | Office phone number |
| @MobileNo | NVARCHAR(50) | Mobile phone number |
| @Email | NVARCHAR(50) | Email address |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access |
| @AccessTimeTo | NVARCHAR(50) | End time of access |
| @AccessLocation | NVARCHAR(50) | Physical location of access |
| @IsNeutralGap | INT | Flag indicating neutral gap requirement |
| @IsExclusive | INT | Flag indicating exclusive access |
| @DescOfWork | NVARCHAR(100) | Description of work to be performed |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating power involvement |
| @PowerOn | INT | Flag indicating power on requirement |
| @Is13ASocket | INT | Flag indicating 13A socket requirement |
| @CrossOver | INT | Flag indicating crossover requirement |
| @UserID | NVARCHAR(100) | Login identifier of the user submitting |
| @ProtectionType | NVARCHAR(50) | Type of protection required |
| @TARID | BIGINT OUTPUT | Generated TAR identifier |
| @Message | NVARCHAR(500) OUTPUT | Status or error message |

### Logic Flow
1. Initialise `@TARID` to 0 and set an internal transaction flag `@IntrnlTrans` to 0.  
2. If the procedure is called outside an existing transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Resolve the numeric user identifier `@UserIDID` by selecting `Userid` from `TAMS_User` where `LoginId` matches the supplied `@UserID`.  
4. Insert a new row into `TAMS_TAR` with all supplied parameters, converting `@AccessDate` to a datetime, and populating audit fields (`CreatedOn`, `CreatedBy`, `UpdatedOn`, `UpdatedBy`) with the current timestamp and resolved user ID.  
5. Capture the newly generated identity value into `@TARID`.  
6. If the insert caused an error (`@@ERROR <> 0`), set `@Message` to a generic insert error string and jump to the error handling section.  
7. If no error, commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
8. Return the `@Message` output (which will be NULL on success).  
9. In the error handling section, rollback the transaction if it was started internally and return the `@Message`.

### Data Interactions
* **Reads:** `TAMS_User`  
* **Writes:** `TAMS_TAR`  

---