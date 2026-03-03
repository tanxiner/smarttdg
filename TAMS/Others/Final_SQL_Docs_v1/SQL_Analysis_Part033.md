# Procedure: sp_TAMS_Depot_TOA_Register
**Type:** Stored Procedure

The procedure registers a new TOA (Train Operations Authority) for a specific TAR (Train Access Request).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the train. |
| @TrackType | nvarchar(50) | The type of track (e.g., Depot, Mainline). |
| @Type | NVARCHAR(20) | The type of TOA registration. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The number of the TAR. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_AccessReq, TAMS_TAMs, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties