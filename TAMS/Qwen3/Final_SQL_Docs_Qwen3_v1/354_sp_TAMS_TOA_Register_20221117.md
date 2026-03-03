# Procedure: sp_TAMS_TOA_Register_20221117

### Purpose
This stored procedure registers a new TOA (TAR Management System - Terminal Access) record, including the TAR number, location, and qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of operation (e.g., NEL or TAMS_TAR). |
| @Type | NVARCHAR(20) | The type of TOA. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR number. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card (NRIC) number. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record. |
| @Message | NVARCHAR(500) OUTPUT | An error message if any errors occur during registration. |

### Logic Flow
1. Check if a transaction has already started. If not, start one.
2. Initialize variables for internal transactions and temporary tables.
3. Retrieve the cut-off time for the current line of operation from the TAMS_Parameters table.
4. Retrieve the QTS qualification code and protocol from the TAMS_Parameters table based on the line of operation and possession status.
5. Check if the TAR number exists in the TAMS_TAR table with a power-on status of 0. If not, set an error message.
6. Check if the location exists for the selected TAR number. If not, set an error message.
7. If both checks pass, proceed to register the TOA record:
	* Retrieve the TAR ID and access date from the TAMS_TAR table.
	* Check if the line of operation matches the TAR line. If not, set an error message.
	* Calculate the operation date based on the cut-off time and access date.
	* Insert a new TOA record into the TAMS_TOA table with the calculated operation date and other details.
	* Insert parties into the TAMS_TOA_Parties table for the newly created TOA record.
8. If any errors occur during registration, set an error message and return it.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TAR_Station, TAMS_TOA, TAMS_TOA_Parties
* Writes: TAMS_TOA