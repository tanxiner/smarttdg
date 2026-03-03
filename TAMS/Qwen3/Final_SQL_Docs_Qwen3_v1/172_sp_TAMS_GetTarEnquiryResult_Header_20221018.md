# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018

### Purpose
This stored procedure retrieves a header for TAMS Tar Enquiry Result based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |

### Logic Flow
The procedure starts by declaring variables and setting conditions. It then checks the value of `@Line1` and sets a condition string `@cond`. Based on the values of `@TarType`, `@AccessType`, `@TarStatusId`, `@AccessDateFrom`, and `@AccessDateTo`, it appends conditions to `@cond`.

Next, it checks if `@Line1` is 'NEL' or 'DTL'. If it's 'NEL', it executes a query with specific conditions. If it's 'DTL', it executes another query with different conditions.

The procedure then constructs an SQL string `@sql` by concatenating the query and setting the row number column. Finally, it prints the SQL string and executes it using the `EXEC` statement.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables.
* **Writes:** None