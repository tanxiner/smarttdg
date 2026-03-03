# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018_M
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve a list of TAR (TARWFStatus) records based on various filters and conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID used for filtering. |
| @Line | nvarchar(10) | The line number used for filtering. |
| @TarType | nvarchar(50) | The TAR type used for filtering. |
| @AccessType | nvarchar(50) | The access type used for filtering. |
| @TarStatusId | integer | The TAR status ID used for filtering. |
| @AccessDateFrom | nvarchar(50) | The start date of the access period used for filtering. |
| @AccessDateTo | nvarchar(50) | The end date of the access period used for filtering. |
| ... | ... | Additional filter parameters |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables
* **Writes:** None