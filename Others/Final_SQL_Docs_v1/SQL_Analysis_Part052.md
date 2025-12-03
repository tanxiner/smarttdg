# Procedure: sp_TAMS_GetTarEnquiryResult_Department
**Type:** Stored Procedure

This procedure retrieves TAR (Traffic and Road) data for a specific department.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter the results by. |

### Logic Flow
1. Checks if the user exists in the TAMS_User table with the specified role.
2. If the user exists, checks if they have a specific role (e.g., NEL_OCCScheduler or DTL_Applicant).
3. Based on the role, sets flags to determine which department and power levels should be included in the results.
4. Constructs a SQL query using the @Line, @TarType, @AccessType, @TarStatusId, @AccessDateFrom, and @AccessDateTo parameters to filter the TAR data.
5. Executes the SQL query and returns the results.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** None