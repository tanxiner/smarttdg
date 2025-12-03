# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529_M
**Type:** Stored Procedure

The procedure retrieves TAR enquiry result headers based on various filters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables
* **Writes:** None