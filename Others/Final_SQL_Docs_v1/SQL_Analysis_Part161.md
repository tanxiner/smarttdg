# Procedure: sp_TAMS_TOA_Register_20221117
**Type:** Stored Procedure

Purpose: This stored procedure performs a series of checks and operations to register a new TOA (Technical Operations Assistant) for a specific TAR (Technical Assistance Request).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(20) | The line number associated with the TAR. |
| @Type		| NVARCHAR(20) | The type of TOA being registered. |
| @Loc		| NVARCHAR(20) | The location where the TAR is located. |
| @TARNo		| NVARCHAR(30) | The unique identifier for the TAR. |
| @NRIC		| NVARCHAR(20) | The National Registration Identity Card number of the person registering. |
| @TOAID		| BIGINT | The ID of the newly created TOA (output parameter). |
| @Message	| NVARCHAR(500) | A message indicating the outcome of the registration process (output parameter). |

### Logic Flow
1. Checks if user exists by verifying that no transactions are currently active.
2. Truncates a temporary table to ensure it is empty before inserting new data.
3. Retrieves relevant parameters from the TAMS_Parameters table, including the cut-off time and QTS qualification code.
4. Verifies that the TAR does not exist or has an invalid status.
5. If the TAR exists, checks if the line number matches and retrieves the TAR's access date and type.
6. Checks if the user's NRIC matches with the InChargeNRIC in the TAMS_TOA table for the same TAR.
7. If the NRIC matches, updates the TAR's operation date or adds parties to the TOA table based on the TAR's status.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR, TAMS_TAR_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties