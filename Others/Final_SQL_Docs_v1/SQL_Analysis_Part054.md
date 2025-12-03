# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve a list of TAR (TARWFStatus) results for a given set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID used to filter the results. |
| @Line | nvarchar(10) | The line number used to filter the results. |
| @TarType | nvarchar(50) | The TAR type used to filter the results. |
| @AccessType | nvarchar(50) | The access type used to filter the results. |
| @TarStatusId | integer | The TAR status ID used to filter the results. |
| @AccessDateFrom | nvarchar(50) | The start date of the access period used to filter the results. |
| @AccessDateTo | nvarchar(50) | The end date of the access period used to filter the results. |
| ... | ... | Additional parameters used to filter the results by specific roles and departments. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables
* **Writes:** None