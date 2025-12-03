# Procedure: sp_TAMS_TOA_Register_20230107_M

### Purpose
This stored procedure registers a new TAR (Traction Alignment Record) into the TAMS system, including booking in and updating relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR (e.g. 'NEL' or 'NOR') |
| @Type | NVARCHAR(20) | The type of the TAR (e.g. 'Possession' or '') |
| @Loc | NVARCHAR(20) | The location of the TAR (used to select the station name) |
| @TARNo | NVARCHAR(30) | The number of the TAR |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number of the person booking in |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA (Traction Alignment Record) |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Create a temporary table to store the results of the qualification check for the person booking in.
3. Retrieve the cut-off time and QTS qualification code from the TAMS parameters table based on the line of the TAR.
4. Check if the TAR number is valid (i.e. it exists in the TAMS_TAR table with a status ID of 9 or 8).
5. If the TAR number is invalid, set an error message and exit the procedure.
6. Retrieve the station name from the TAMS_Station table based on the location of the TAR.
7. Check if the TAR number is valid (i.e. it exists in the TAMS_TAR table with a status ID of 9 or 8) and the station name matches; if not, set an error message and exit the procedure.
8. If the TAR number and station name are valid, proceed to book in the TAR.
9. Retrieve the TAR ID, line, access date, and access type from the TAMS_TAR table based on the TAR number.
10. Check if the operation date is within the allowed range; if not, set an error message and exit the procedure.
11. Perform a qualification check for the person booking in using the QTS qualification code.
12. If the qualification check fails, set an error message and exit the procedure.
13. Book in the TAR into the TAMS system, including updating relevant records such as the TOA table and parties table.
14. Return the ID of the newly created TOA and any error messages.

### Data Interactions
* Reads: TAMS_TAR, TAMS_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA