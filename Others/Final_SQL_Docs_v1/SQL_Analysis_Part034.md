# Procedure: sp_TAMS_Depot_TOA_Register_1
**Type:** Stored Procedure

The procedure performs a registration process for a Train Operator Assistant (TOA) at a depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the train. |
| @TrackType | nvarchar(50) | The type of track. |
| @Type | NVARCHAR(20) | The type of TOA registration. |
| @Loc | NVARCHAR(20) | The location of the depot. |
| @TARNo | NVARCHAR(30) | The TAR number. |
| @NRIC | NVARCHAR(20) | The NRIC number. |
| @TOAID | BIGINT OUTPUT | The ID of the TOA registration. |
| @Message | NVARCHAR(500) OUTPUT | An error message if any. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_AccessReq, TAMS_TAM, TAMS_TOA, TAMS_Parameters
* **Writes:** TAMS_TOA_Registration_Log