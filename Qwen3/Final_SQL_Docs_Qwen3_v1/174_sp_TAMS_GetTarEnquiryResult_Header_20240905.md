# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20240905

### Purpose
This stored procedure retrieves a header result for TAMS TAR enquiry, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(50) | Line number |
| @TrackType | nvarchar(50) | Track type |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Access date from |
| @AccessDateTo | nvarchar(50) | Access date to |
| @Department | nvarchar(50) | Department |
| @Userid | nvarchar(50) | User ID |

### Logic Flow
The procedure follows these steps:

1. It checks if the user has a role in the specified track type and if they are an administrator, power endorser, or chief controller.
2. Based on the user's role, it sets three flags: @IsAll, @IsPower, and @IsDep.
3. If the user is not an external user, it sets all flags to 0.
4. It constructs a SQL query string (@cond) based on the input parameters and flags.
5. The procedure then executes the constructed SQL query using the ROW_NUMBER() function to retrieve the TAR results.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User