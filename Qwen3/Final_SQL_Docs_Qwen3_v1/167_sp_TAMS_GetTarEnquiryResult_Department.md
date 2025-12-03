# Procedure: sp_TAMS_GetTarEnquiryResult_Department

### Purpose
This stored procedure retrieves a list of TAR (Traffic Accident Report) companies that match the specified criteria, including track type, line, and access date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter by. |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs for all track types.
2. If not, it then checks if the user has a power endorser or power HOD role, which grants access to TARs involving power.
3. Next, it checks if the user has an applicant HOD or applicant role, which allows them to view TARs under their own department.
4. The procedure then constructs a SQL query using the `ROW_NUMBER()` function to order the results by company name.
5. The query filters the TARs based on the specified track type, line, and access date range.
6. Finally, the procedure executes the constructed SQL query and prints it for debugging purposes.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User