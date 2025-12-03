# Procedure: sp_TAMS_GetTarEnquiryResult_Header_ToBeDeployed

### Purpose
This stored procedure retrieves a header for a TAR enquiry result to be deployed, based on various parameters such as user ID, line number, tar type, access date range, and applicant status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line number |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Start access date |
| @AccessDateTo | nvarchar(50) | End access date |
| ... | ... | Various applicant statuses |

### Logic Flow
The procedure first checks the line number and sets a condition based on it. If the line number is 'NEL', it retrieves the status ID from TAMS_WFStatus table for the specified WFType and WFStatus. It then constructs an SQL query to select rows with ROW_NUMBER() over (ORDER BY t.tarno desc) as sno, and various other columns.

If the line number is not 'NEL' but is 'DTL', it performs a similar process as above. However, if the line number is neither 'NEL' nor 'DTL', it simply prints 'dtl'.

The procedure then constructs an SQL query with UNION ALL to combine results from both 'NEL' and 'DTL' lines.

Finally, it executes the constructed SQL query using EXEC (@sql).

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables.
* Writes: None.