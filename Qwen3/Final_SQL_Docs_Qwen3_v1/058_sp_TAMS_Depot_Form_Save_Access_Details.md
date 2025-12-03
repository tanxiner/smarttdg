# Procedure: sp_TAMS_Depot_Form_Save_Access_Details

### Purpose
This stored procedure saves access details for a depot form, including user information and TAR (Traction and Maintenance System) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number |
| @TrackType | NVARCHAR(50) | Track type of the depot form |
| @AccessDate | NVARCHAR(20) | Date of access to the depot form |
| @AccessTimeSlot | NVARCHAR(50) | Time slot for accessing the depot form |
| @AccessType | NVARCHAR(20) | Type of access (e.g., user, admin) |
| @TARType | NVARCHAR(10) | Type of TAR data being saved |
| @Company | NVARCHAR(50) | Company name associated with the TAR data |
| @Designation | NVARCHAR(50) | Designation or role of the user accessing the depot form |
| @Name | NVARCHAR(50) | Name of the user accessing the depot form |
| @OfficeNo | NVARCHAR(50) | Office number of the user accessing the depot form |
| @MobileNo | NVARCHAR(50) | Mobile number of the user accessing the depot form |
| @Email | NVARCHAR(50) | Email address of the user accessing the depot form |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access to the depot form |
| @AccessTimeTo | NVARCHAR(50) | End time of access to the depot form |
| @AccessLocation | NVARCHAR(50) | Location where the depot form was accessed |
| @IsNeutralGap | INT | Flag indicating whether a neutral gap is involved |
| @IsExclusive | INT | Flag indicating whether exclusive access is required |
| @DescOfWork | NVARCHAR(100) | Description of work being done on the depot form |
| @ARRemark | NVARCHAR(1000) | Additional remarks or comments about the TAR data |
| @InvolvePower | INT | Flag indicating whether power involvement is required |
| @PowerOn | INT | Flag indicating whether power-on is required |
| @Is13ASocket | INT | Flag indicating whether 13A socket is involved |
| @CrossOver | INT | Flag indicating whether cross-over is involved |
| @UserID | NVARCHAR(100) | User ID of the user accessing the depot form |
| @ProtectionType | NVARCHAR(50) | Type of protection required for the TAR data |
| @TARID | BIGINT OUTPUT | Unique identifier for the saved TAR data |
| @Message | NVARCHAR(500) OUTPUT | Error message if any |

### Logic Flow
1. The procedure starts by setting the initial internal transaction counter to 0.
2. It checks if there is an active transaction and sets the internal transaction counter accordingly.
3. If the user ID is provided, it retrieves the corresponding user ID from the TAMS_User table.
4. The procedure then inserts a new record into the TAMS_TAR table with the provided data.
5. After inserting the record, it retrieves the newly generated TAR ID using the SCOPE_IDENTITY() function.
6. If any errors occur during the insertion process, it sets an error message and exits the procedure.
7. Finally, if no errors occurred, it commits the transaction and returns the error message.

### Data Interactions
* Reads: TAMS_User table (for retrieving user ID)
* Writes: TAMS_TAR table (for inserting new record)