# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220120

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID. |

### Logic Flow
1. The procedure starts by declaring variables and setting conditions based on the input parameters.
2. It then checks if the `@Line` parameter is not empty, and if so, it prints the first three characters of the line number (`@Line1`) to identify the type of inquiry (NEL or DTL).
3. Based on the value of `@Line1`, the procedure selects the corresponding status ID from TAMS_WFStatus.
4. It then constructs a SQL query using the `@sql` variable, which includes conditions based on the input parameters and the selected status ID.
5. The procedure executes the constructed SQL query to retrieve the required data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept
* **Writes:** None