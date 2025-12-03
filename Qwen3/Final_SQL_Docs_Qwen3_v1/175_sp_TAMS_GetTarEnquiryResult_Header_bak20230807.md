# Procedure: sp_TAMS_GetTarEnquiryResult_Header_bak20230807

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID. |

### Logic Flow
The procedure starts by checking the values of various parameters, such as `@Line1` and `@Line2`, to determine which type of Tar Enquiry to retrieve (NEL or DTL). It then constructs a SQL query using these parameters and executes it.

Here's a step-by-step explanation:

1. The procedure checks if `@Line1` is not empty, and if so, prints the value of `@Line1`.
2. If `@Line1` is 'NEL', it retrieves the status ID from TAMS_WFStatus where Line = @Line1 and WFType = 'TARWFStatus' and WFStatus = 'Cancel'.
3. It then constructs a SQL query using the parameters, including conditions based on the values of various flags (e.g., `@isNEL_Applicant`, `@isDTL_Applicant`).
4. The procedure checks if `@Line2` is not empty, and if so, appends another condition to the SQL query.
5. Finally, it executes the constructed SQL query.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept
* **Writes:** None