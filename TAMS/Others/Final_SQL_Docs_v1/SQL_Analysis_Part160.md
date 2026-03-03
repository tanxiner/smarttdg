# Procedure: sp_TAMS_TOA_Register
**Type:** Stored Procedure

The purpose of this stored procedure is to register a new TOA (Track and Trace Operation) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the track |
| @TrackType | NVARCHAR(50) | The type of track |
| @Type | NVARCHAR(20) | The type of TOA |
| @Loc | NVARCHAR(20) | The location of the TOA |
| @TARNo | NVARCHAR(30) | The TAR number |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the operation |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAMSSubscription
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties