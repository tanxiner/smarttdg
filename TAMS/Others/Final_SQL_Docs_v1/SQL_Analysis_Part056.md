# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018
**Type:** Stored Procedure

The procedure retrieves TAR enquiry result headers based on various filters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line number |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Access date from |
| @AccessDateTo | nvarchar(50) | Access date to |
| ... | ... | Additional filter parameters |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables
* **Writes:** None