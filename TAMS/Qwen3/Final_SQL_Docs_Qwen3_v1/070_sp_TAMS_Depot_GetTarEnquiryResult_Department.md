# Procedure: sp_TAMS_Depot_GetTarEnquiryResult_Department

### Purpose
This stored procedure retrieves a list of companies associated with a specific TAR (Tracking and Reporting) status, filtered by various parameters such as track type, access date range, and user role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user making the enquiry. |
| @Line | nvarchar(50) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (e.g., 'NEL', 'PFR', etc.). |
| @TarType | nvarchar(50) | The TAR type to filter by (optional). |
| @AccessType | nvarchar(50) | The access type to filter by (optional). |
| @TarStatusId | integer | The TAR status ID to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access period (optional). |
| @AccessDateTo | nvarchar(50) | The end date of the access period (optional). |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs for all track types.
2. If not, it then checks if the user has a power endorser or power HOD role, which grants them access to TARs with InvolvePower = 1.
3. Next, it checks if the user is an applicant HOD and can view TARs under their own department.
4. Finally, if none of the above conditions are met, the procedure filters the TARs based on the specified track type, access date range, and user ID.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept, TAMS_User_Role
* Writes: None