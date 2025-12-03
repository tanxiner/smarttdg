# Procedure: sp_TAMS_TOA_Register_20230801
**Type:** Stored Procedure

The procedure performs a registration process for a TAR (TAR No) and updates various tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR No to be registered. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card Number) of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA (TAR Operation Authorization). |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAM, TAMS_Station, TAMS_TOA, TAMS Paramaters
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties