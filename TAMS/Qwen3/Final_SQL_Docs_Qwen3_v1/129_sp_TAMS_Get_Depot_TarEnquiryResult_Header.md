# Procedure: sp_TAMS_Get_Depot_TarEnquiryResult_Header

### Purpose
This stored procedure retrieves a header result for depot TAR enquiry, filtering by various parameters such as track type, tar type, access type, and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter results by. |

### Logic Flow
1. The procedure first checks if the user has a specific role (NEL_ApplicantHOD, NEL_PowerEndorser, or NEL_PowerHOD) that grants access to TAR enquiry.
2. Based on the user's role, it sets flags (@IsAll, @IsPower, and @IsDep) to determine which conditions should be applied to filter results.
3. It then constructs a SQL query string (@sql) by concatenating various conditions based on the flags set earlier.
4. The query string is executed using the EXEC function.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus