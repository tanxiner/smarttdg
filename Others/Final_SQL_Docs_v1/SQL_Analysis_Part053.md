# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220120
**Type:** Stored Procedure

This procedure retrieves the TAR enquiry result header data based on various filters and conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter by. |
| @Line | nvarchar(10) | The line number to filter by. |
| @TarType | nvarchar(50) | The TAR type to filter by. |
| @AccessType | nvarchar(50) | The access type to filter by. |
| @TarStatusId | integer | The TAR status ID to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date for access filtering. |
| @AccessDateTo | nvarchar(50) | The end date for access filtering. |
| ... | ... | Various flags to filter by (e.g., isNEL_Applicant, isDTL_Applicant). |

### Logic Flow
1. Checks if the user ID exists.
2. Inserts into the Audit table.
3. Returns the TAR enquiry result header data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept
* **Writes:** None