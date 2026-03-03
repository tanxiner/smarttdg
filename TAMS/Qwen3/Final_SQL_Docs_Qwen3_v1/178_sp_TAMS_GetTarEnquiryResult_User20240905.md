# Procedure: sp_TAMS_GetTarEnquiryResult_User20240905

### Purpose
This stored procedure retrieves TAR (TARWFStatus) data for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user to retrieve TAR data for. |
| @Line | nvarchar(50) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (e.g., 'NEL_DCC', 'DTL_TAPApprover'). |
| @TarType | nvarchar(50) | The tar type to filter by (optional). |
| @AccessType | nvarchar(50) | The access type to filter by (optional). |
| @TarStatusId | integer | The TAR status ID to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access date range (optional). |
| @AccessDateTo | nvarchar(50) | The end date of the access date range (optional). |

### Logic Flow
1. The procedure first checks if the user has a specific role or combination of roles that allow them to view TAR data.
2. Based on the user's role, it sets flags (`@IsAll`, `@IsPower`, and `@IsDep`) to determine which filter conditions to apply.
3. It then constructs a SQL query string using these flags and additional filter parameters (e.g., line number, tar type, access date range).
4. The procedure executes the constructed SQL query and prints it for debugging purposes.
5. Finally, it executes the query to retrieve the TAR data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User