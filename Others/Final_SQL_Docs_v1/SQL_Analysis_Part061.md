# Procedure: sp_TAMS_GetTarEnquiryResult_User
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve a list of TAR (TARWFStatus) records for a specific user, filtered by various criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR records. |

### Logic Flow
1. Checks if the user exists in the TAMS_User table with a matching role.
2. If the user exists, checks if they have a specific role (e.g., NEL_DCC, NEL_ChiefController) that allows them to view all TAR records.
3. If the user has the required role, sets a flag (@IsAll = 1).
4. Checks if the user has another specific role (e.g., NEL_PowerEndorser, NEL_PFR) that allows them to view only Power-related TAR records.
5. If the user has the required role, sets a flag (@IsPower = 1).
6. Checks if the user has yet another specific role (e.g., NEL_ApplicantHOD, NEL_Applicant) that allows them to view TAR records under their own department.
7. If the user has the required role, sets a flag (@IsDep = 1).
8. Based on the flags set in steps 3-7, constructs a SQL query to retrieve the TAR records using the ROW_NUMBER() function.

### Data Interactions
* Reads: TAMS_User, TAMS_User_Role, TAMS_Role, TAMS_TAR, TAMS_WFStatus
* Writes: None