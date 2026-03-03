# Procedure: sp_TAMS_TOA_Register_20230801_M

### Purpose
This stored procedure registers a new TAR (Traction and Maintenance System) record, including the line, station, TAR number, and other relevant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the station. |
| @TARNo | NVARCHAR(30) | The number of the TAR. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA (Traction and Maintenance System) record. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. The procedure checks if a transaction has already started. If not, it starts one.
2. It truncates a temporary table to ensure any previous data is cleared.
3. The procedure retrieves various parameters from the TAMS_Parameters table based on the input line and TAR number.
4. It checks if the station exists for the given TAR number. If not, it sets an error message and returns.
5. If the station exists, it checks if the TAR number is valid. If not, it sets an error message and returns.
6. The procedure then checks if the line matches the TAR line. If not, it sets an error message and returns.
7. It retrieves the TOA ID from the TAMS_TOA table based on the TAR ID. If no TOA ID is found, it creates a new one.
8. The procedure then checks the qualification status of the person associated with the NRIC number. If the qualification is invalid, it sets an error message and returns.
9. If the qualification is valid, it inserts a new record into the TAMS_TOA table with the relevant details.
10. It also updates the TOA parties table with the newly created TOA ID and other relevant details.
11. Finally, it logs the registration process in the TAMS_TOA_Registration_Log table.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TAR_Station, TAMS_Station, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Registration_Log
* Writes: #tmpnric (temporary table), TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties