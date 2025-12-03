# Procedure: sp_TAMS_TOA_Register_bak20230801
**Type:** Stored Procedure

Purpose: This stored procedure performs a registration process for a TAR (Test and Measurement) record, including checking user existence, inserting into Audit table, and returning ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line number of the TAR |
| @Type | NVARCHAR(20) | Type of the TAR |
| @Loc | NVARCHAR(20) | Location of the TAR |
| @TARNo | NVARCHAR(30) | Number of the TAR |
| @NRIC | NVARCHAR(20) | National Registration Identity Card number of the user |
| @TOAID | BIGINT OUTPUT | ID of the TOA (Test and Measurement) record |
| @Message | NVARCHAR(500) OUTPUT | Error message |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA_PointNo, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties