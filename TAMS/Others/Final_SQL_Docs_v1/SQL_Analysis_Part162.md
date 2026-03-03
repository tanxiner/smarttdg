# Procedure: sp_TAMS_TOA_Register_20221117_M
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of registering a new TOA (Temporary Occupation Agreement) for a specific TAR (Temporary Access Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number associated with the TAR. |
| @Type | NVARCHAR(20) | The type of TOA being registered. |
| @Loc | NVARCHAR(20) | The location associated with the TAR. |
| @TARNo | NVARCHAR(30) | The TAR number to be registered. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) of the person registering the TOA. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR, TAMS_TAR_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties