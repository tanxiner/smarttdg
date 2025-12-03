# Procedure: sp_TAMS_TOA_Register_20221117_M

### Purpose
This stored procedure registers a new TOA (TAR Management System - Terminal Access) record, including the TAR number, location, and qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR (e.g., 'NEL' or 'TAMS_TAR') |
| @Type | NVARCHAR(20) | The type of qualification (e.g., 'Possession' or '') |
| @Loc | NVARCHAR(20) | The location of the TAR station |
| @TARNo | NVARCHAR(30) | The TAR number |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record |
| @Message | NVARCHAR(500) OUTPUT | An error message if any |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Initialize variables for internal transactions and temporary tables.
3. Retrieve the cut-off time for the current line from the TAMS_Parameters table.
4. Retrieve the QTS qualification code and protocol from the TAMS_Parameters table based on the current line and possession status.
5. Check if the TAR number exists in the TAMS_TAR table; if not, set an error message.
6. Check if a valid location for the selected TAR exists; if not, set an error message.
7. If both checks pass, proceed to register the TOA record:
	* Retrieve the TAR ID and access date from the TAMS_TAR table.
	* Check if the qualification details match with the existing records in the TAMS_TOA table; if not, set an error message.
	* If the qualification details are valid, insert a new TOA record into the TAMS_TOA table.
	* Insert parties into the TAMS_TOA_Parties table for the newly created TOA record.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TOA, TAMS_TOA_Parties
* Writes: TAMS_TOA