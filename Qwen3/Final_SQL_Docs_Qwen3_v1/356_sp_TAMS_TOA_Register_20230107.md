# Procedure: sp_TAMS_TOA_Register_20230107

### Purpose
This stored procedure registers a new TAR (Traction Alignment Record) and updates the corresponding TOA (Track and Maintenance System - Operations Area) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. Can be either 'NEL' or 'TAMS_TAR'. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. Must match a station in TAMS_Station table. |
| @TARNo | NVARCHAR(30) | The number of the TAR. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Check if a transaction has already started. If not, start a new transaction.
2. Create a temporary table #tmpnric to store the results of the QTS qualification check.
3. Truncate the temporary table and initialize variables for the execution string and date.
4. Retrieve the cut-off time and QTS qualification code from TAMS_Parameters table based on the line number and effective dates.
5. Check if the TAR exists in TAMS_TAR table with a status of 0 (not powered on). If not, set an error message.
6. Check if the location matches a station in TAMS_Station table. If not, set an error message.
7. If both checks pass, proceed to register the TAR and update the TOA record.
8. Retrieve the TAR ID, line number, access date, and access type from TAMS_TAR table.
9. Check if the line number matches the TAR line number. If not, set an error message.
10. Register the TAR by inserting a new record into TAMS_TOA table with the retrieved values.
11. Update the TOA ID in the temporary table #tmpnric.
12. Insert a new record into TAMS_TOA_Audit table to log the registration process.
13. If the TAR has an InChargeNRIC, check if it matches the NRIC number of the person registering. If not, set an error message.
14. Update the TOA record by setting the OperationDate and TOAStatus based on the access date and status.
15. Insert a new record into TAMS_TOA_Parties table to log the registration process.
16. Commit or roll back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_Station, TAMS_TAR, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA