# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018_M

### Purpose
This stored procedure retrieves a list of TAR (TARWFStatus) enquiry results for a given set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter the results by. |

### Logic Flow
The procedure starts by declaring variables and setting conditions based on the input parameters. It then constructs a SQL query using these conditions and executes it.

1. If `@Line1` is not empty, the procedure checks if it's 'NEL' or 'DTL'. Depending on this value, it selects rows from either `TAMS_TAR` table with specific conditions.
2. For each line (either `@Line1` or `@Line2`), the procedure constructs a SQL query using the input parameters and executes it.
3. The results are stored in a temporary result set named 't'.
4. Finally, the procedure prints the constructed SQL query and executes it.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_WFStatus`
* **Writes:** None