# Procedure: sp_TAMS_Depot_Form_Save_Access_Details
**Type:** Stored Procedure

Purpose: This stored procedure saves access details for a TAMS Depot Form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line number of the form being saved |
| @TrackType | NVARCHAR(50) | Track type of the form |
| @AccessDate | NVARCHAR(20) | Access date of the form |
| @AccessTimeSlot | NVARCHAR(50) | Access time slot of the form |
| @AccessType | NVARCHAR(20) | Type of access to the form |
| @TARType | NVARCHAR(10) | Type of TAMS TAR |
| @Company | NVARCHAR(50) | Company name associated with the form |
| @Designation | NVARCHAR(50) | Designation associated with the form |
| @Name | NVARCHAR(50) | Name associated with the form |
| @OfficeNo | NVARCHAR(50) | Office number associated with the form |
| @MobileNo | NVARCHAR(50) | Mobile number associated with the form |
| @Email | NVARCHAR(50) | Email address associated with the form |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access to the form |
| @AccessTimeTo | NVARCHAR(50) | End time of access to the form |
| @AccessLocation | NVARCHAR(50) | Location where the form was accessed |
| @IsNeutralGap | INT | Flag indicating if neutral gap is involved |
| @IsExclusive | INT | Flag indicating if exclusive access is required |
| @DescOfWork | NVARCHAR(100) | Description of work being done |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating if power is involved |
| @PowerOn | INT | Flag indicating if power is on |
| @Is13ASocket | INT | Flag indicating if 13A socket is used |
| @CrossOver | INT | Flag indicating if cross over is involved |
| @UserID | NVARCHAR(100) | User ID associated with the form |
| @ProtectionType | NVARCHAR(50) | Protection type of the form |
| @TARID | BIGINT OUTPUT | Unique identifier for the TAMS TAR record |
| @Message | NVARCHAR(500) OUTPUT | Error message if insertion fails |

### Logic Flow
1. Checks if user exists by selecting their User ID from the TAMS_User table.
2. Inserts a new record into the TAMS_TAR table with the provided form details.
3. Retrieves the unique identifier for the newly inserted TAMS TAR record and stores it in the @TARID variable.
4. If an error occurs during insertion, sets the @Message variable to an error message and exits the procedure.
5. If no errors occur, commits the transaction and returns the @Message variable.

### Data Interactions
* Reads: TAMS_User table
* Writes: TAMS_TAR table