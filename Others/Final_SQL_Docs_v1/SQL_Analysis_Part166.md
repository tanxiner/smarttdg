# Procedure: sp_TAMS_TOA_Register_20230801_M
**Type:** Stored Procedure

The purpose of this stored procedure is to register a new TAR (Traction and Maintenance) record, including the line, station, TAR number, and other relevant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| AS NVARCHAR(20) = NULL | The line of the TAR |
| @Type		| AS NVARCHAR(20) = NULL | The type of the TAR |
| @Loc		| AS NVARCHAR(20) = NULL | The location of the station |
| @TARNo		| AS NVARCHAR(30) = NULL | The number of the TAR |
| @NRIC		| AS NVARCHAR(20) = NULL | The National Registration Identity Card number |
| @TOAID		| AS BIGINT = 0 OUTPUT | The ID of the newly created TOA record (output parameter) |
| @Message	| AS NVARCHAR(500) = NULL OUTPUT | A message indicating the result of the operation (output parameter) |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR, TAMS_TAR_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties