# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry, which includes various filter criteria such as Line, TarType, AccessType, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line number |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| ... | ... | Additional filter criteria |

### Logic Flow
The procedure starts by checking the values of various parameters and setting a condition string (@cond). It then constructs a SQL query using this condition string to select rows from TAMS_TAR and TAMS_WFStatus tables. The query is based on the value of @Line, which determines whether it's 'NEL' or 'DTL'. For each line, it checks various conditions (e.g., TarType, AccessType) and applies them to the condition string (@cond). If the conditions are met, it includes the corresponding table in the SQL query. The procedure then prints the constructed SQL query and executes it.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables
* Writes: None