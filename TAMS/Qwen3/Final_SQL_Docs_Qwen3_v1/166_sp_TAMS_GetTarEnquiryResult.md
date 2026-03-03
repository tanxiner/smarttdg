# Procedure: sp_TAMS_GetTarEnquiryResult

### Purpose
This stored procedure retrieves and displays the TAR enquiry results based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID used to filter the results. |

### Logic Flow
The procedure starts by checking if any of the input parameters are not null or empty. It then constructs a SQL query string based on the values of these parameters.

If the line number is provided, it checks for specific conditions and constructs different parts of the SQL query string accordingly. For example, if the line number is 'NEL', it checks for certain flags to determine which part of the query to use.

The procedure then combines all the parts of the SQL query string using a union operator and executes the resulting query.

### Data Interactions
* **Reads:** TAMS_TAR_Test table, TAMS_WFStatus table, TAMS_User_QueryDept table.
* **Writes:** None