# Procedure: sp_TAMS_GetTarEnquiryResult_Header

### Purpose
This stored procedure retrieves a header result for TAMS TAR enquiry, based on the provided parameters.

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
The procedure first checks the user's role and permissions based on the provided parameters. It then constructs a SQL query using the `ROW_NUMBER()` function to retrieve the required data.

1. The procedure starts by checking if the user has any roles that match the specified track type. If they do, it sets the `@IsAll` variable to 1.
2. Next, it checks if the user has any roles that involve power or are power endorser. If they do, it sets the `@IsPower` variable to 1.
3. Then, it checks if the user has any roles that involve department or are applicant HOD. If they do, it sets the `@IsDep` variable to 1.
4. The procedure then constructs a SQL query using the `ROW_NUMBER()` function to retrieve the required data. It uses the `@cond` variable to filter the results based on the provided parameters.
5. Finally, it executes the constructed SQL query and prints the result.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User
* Writes: None