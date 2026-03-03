# Procedure: sp_TAMS_TOA_Register_20230801

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
| @TOAID | BIGINT OUTPUT | The ID of the TOA (TAR Operation Area) being created or updated. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the outcome of the registration process. |

### Logic Flow
1. The procedure first checks if a transaction has been started. If not, it starts one.
2. It then truncates a temporary table to ensure any previous data is cleared.
3. The procedure retrieves various parameters from the TAMS_Parameters table based on the line number of the TAR and the current date.
4. It checks if the TAR No exists in the TAMS_TAR table and if it has not been activated (PowerOn = 0). If not, it sets an error message and returns.
5. The procedure then checks if the location of the TAR matches any station in the TAMS_Station table associated with the TAR. If not, it sets an error message and returns.
6. If both checks pass, the procedure creates a TOA ID for the TAR No and retrieves the TAR details from the TAMS_TAR table.
7. It then checks if the TAR access date matches the current date or is within one day of the current date. If not, it sets an error message and returns.
8. The procedure then inserts a new record into the TAMS_TOA table with the relevant details.
9. After inserting the record, it updates the TOA status in the TAMS_TOA table based on the TAR access date.
10. It also checks if there are any parties associated with the TAR and updates their status accordingly.
11. Finally, the procedure inserts a new log entry into the TAMS_TOA_Registration_Log table to track the registration process.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_Station, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Registration_Log
* Writes: TAMS_TOA