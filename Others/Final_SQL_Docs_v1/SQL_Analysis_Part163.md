# Procedure: sp_TAMS_TOA_Register_20230107
**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of registering a new TOA (Temporary Occupation Agreement) for a specific TAR (Temporary Access Request).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| AS NVARCHAR(20) | The line number associated with the TAR. |
| @Type		| AS NVARCHAR(20) | The type of TOA being registered. |
| @Loc		| AS NVARCHAR(20) | The location associated with the TAR. |
| @TARNo		| AS NVARCHAR(30) | The TAR number to be registered. |
| @NRIC		| AS NVARCHAR(20) | The NRIC (National Registration Identity Card) of the person registering the TOA. |
| @TOAID		| AS BIGINT OUTPUT | The ID of the newly created TOA. |
| @Message	| AS NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAMs_TAR
* **Writes:** TAMS_TOA_Audit, TAMS_TOA_Parties