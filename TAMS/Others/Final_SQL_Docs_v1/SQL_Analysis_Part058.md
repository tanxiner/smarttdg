# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20240905
**Type:** Stored Procedure

The procedure retrieves and returns a list of TAR (Traffic Accident Report) results based on various filters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR results. |

### Logic Flow
1. Checks if the user exists in the system.
2. If the user is an administrator, checks if they have access to all TAR results.
3. If the user has power endorser or power HOD role, checks if they have access to power endorser or power HOD TAR results.
4. If the user has applicant HOD or applicant role, checks if they have access to their own created TAR results.
5. If the user is an external user, sets the IsDep flag to 0 and clears the IsPower and IsAll flags.
6. Constructs a SQL query based on the user's role and filters.
7. Executes the SQL query and returns the results.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User, TAMS_Role
* **Writes:** None