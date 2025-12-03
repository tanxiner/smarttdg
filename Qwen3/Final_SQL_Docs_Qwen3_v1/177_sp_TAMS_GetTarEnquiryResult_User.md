# Procedure: sp_TAMS_GetTarEnquiryResult_User

### Purpose
This stored procedure retrieves TAR (TAR Status) enquiry results for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR enquiry results. |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs under their department or as a power endorser, power HOD, or power endorser.
2. If the user meets these conditions, it filters the TARs based on the specified track type and additional parameters such as tar type, access date range, and more.
3. The procedure then selects distinct TAR records from the TAMS_TAR table, along with the createdBy field, which represents the ID of the user who created the TAR record.
4. Finally, it executes the selected query to retrieve the TAR enquiry results.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, and TAMS_User tables.