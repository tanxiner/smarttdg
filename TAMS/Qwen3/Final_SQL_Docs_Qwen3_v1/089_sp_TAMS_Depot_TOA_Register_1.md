# Procedure: sp_TAMS_Depot_TOA_Register_1

### Purpose
This stored procedure registers a TAR (Train Access Record) for Depot TOA (Train Operations Authority) purposes, updating relevant records and logging the registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line number of the train |
| @TrackType | nvarchar(50) | Track type (DEPOT or Mainline) |
| @Type | NVARCHAR(20) | Type of TAR registration |
| @Loc | NVARCHAR(20) | Location of the station |
| @TARNo | NVARCHAR(30) | Number of the train access record |
| @NRIC | NVARCHAR(20) | National Registration Identity Card number |
| @TOAID | BIGINT OUTPUT | Unique ID for the TAR registration |
| @Message | NVARCHAR(500) OUTPUT | Error message or success message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal flag to indicate that a new transaction has started.
2. It then creates a temporary table #tmpnric to store the results of the QTS (Qualification Testing System) checks for each line number.
3. The procedure truncates the temporary table and sets up variables for the execution string, qualification date, in-charge name, and in-charge status.
4. It retrieves the cut-off time for the current day based on the track type and line number.
5. The procedure then performs QTS checks for each line number using the STRING_AGG function to concatenate the results into a single string.
6. If the line number is 'DTL', it counts the number of TAR records with the same status ID as the line number.
7. It sets up variables for the TAR ID, TAR line, TAR access date, and access type based on the line number.
8. The procedure then checks if the TAR record exists in the database and updates the operation date if necessary.
9. If the TAR record does not exist or has an invalid status, it performs additional checks to determine the reason for the error.
10. Finally, the procedure inserts a new log entry into the TAMS_TOA_Registration_Log table with the registration details.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAMs_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Registration_Log
* Writes: TAMS_TOA