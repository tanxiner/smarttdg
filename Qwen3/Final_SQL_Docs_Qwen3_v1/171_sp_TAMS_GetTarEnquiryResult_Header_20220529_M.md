# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529_M

### Purpose
This stored procedure retrieves a list of TAR (TAR Status) enquiry results for a given set of parameters, including user ID, line number, tar type, access date range, and applicant status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line Number |
| @TarType | nvarchar(50) | TAR Type |
| @AccessType | nvarchar(50) | Access Type |
| @TarStatusId | integer | TAR Status ID |
| @AccessDateFrom | nvarchar(50) | Access Date From |
| @AccessDateTo | nvarchar(50) | Access Date To |
| ... | ... | Applicant Status |

### Logic Flow
The procedure starts by declaring variables and setting conditions based on the input parameters. It then constructs a SQL query using these conditions to retrieve the required data from the TAMS_TAR and TAMS_WFStatus tables.

1. The procedure first checks if the line number is 'NEL' or 'DTL'. If it's 'NEL', it sets up a condition for the TAR type, access type, and TAR status ID.
2. If the line number is not 'NEL', but is 'DTL', it sets up conditions based on the applicant status.
3. The procedure then constructs the SQL query using these conditions and executes it to retrieve the required data.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables
* Writes: None