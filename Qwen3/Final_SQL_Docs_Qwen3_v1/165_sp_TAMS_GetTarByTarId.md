# Procedure: sp_TAMS_GetTarByTarId

### Purpose
This stored procedure retrieves detailed information about a specific TAR (TAR No.) by its ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be retrieved. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table where the Id column matches the provided TarId.
2. It retrieves various columns, including line number, TAR No., type, company, designation, name, office number, mobile number, email, submit date, access date and time, access location, access type, neutral gap status, exclusive status, description of work, remark, 13A socket status, cross-over status, protection type, withdrawal remark, and the corresponding TAR status.

### Data Interactions
* **Reads:** TAMS_TAR table