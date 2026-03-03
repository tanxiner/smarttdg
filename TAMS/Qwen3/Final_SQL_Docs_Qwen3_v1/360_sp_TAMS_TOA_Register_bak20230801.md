# Procedure: sp_TAMS_TOA_Register_bak20230801

### Purpose
This stored procedure performs a registration process for a TAR (TAR No) and updates various tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR No to be registered. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card Number) of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the TOA (TAR Operation Area) being registered. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Check if a transaction has already started. If not, start a new transaction.
2. Create a temporary table to store the NRIC and its corresponding qualification status.
3. Truncate the temporary table.
4. Retrieve the cut-off time for the TAR No from the TAMS_Parameters table based on the line number.
5. Retrieve the QTS (Qualification Time Stamp) code and protocol code from the TAMS_Parameters table based on the line number.
6. Check if the TAR No exists in the TAMS_TAR table with a status of 0 (Power On = 0). If not, set an error message and return.
7. Check if the location of the TAR No matches any station in the TAMS_Station table. If not, set an error message and return.
8. If the TAR No exists and its location is valid, proceed with the registration process.
9. Retrieve the TAR ID, line number, access date, and access type from the TAMS_TAR table based on the TAR No.
10. Check if the line number matches the TAR line number. If not, set an error message and return.
11. If the line numbers match, proceed with the registration process.
12. Retrieve the TOA ID from the TAMS_TOA table based on the TAR ID. If no TOA ID is found, create a new one.
13. Check if the access date of the TAR No matches the current date and time. If not, set an error message and return.
14. If the access dates match, proceed with the registration process.
15. Retrieve the qualification status from the temporary table based on the NRIC. If no qualification status is found, create a new one.
16. Check if the qualification status is valid. If not, set an error message and return.
17. Insert a new record into the TAMS_TOA table with the registration details.
18. Insert a new record into the TAMS_TOA_Audit table to log the registration process.
19. Insert a new record into the TAMS_TOA_Parties table to add parties to the TOA.
20. If any errors occur during the registration process, roll back the transaction and return an error message.

### Data Interactions
* Reads: TAMS_Station, TAMS_TAR, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties