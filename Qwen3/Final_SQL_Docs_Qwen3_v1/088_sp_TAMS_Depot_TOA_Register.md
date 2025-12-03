# Procedure: sp_TAMS_Depot_TOA_Register

### Purpose
This stored procedure registers a new TOA (Train Operations Authority) for a specific TAR (Train Access Request). It validates various parameters, including the line, track type, and TAR status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the train. |
| @TrackType | NVARCHAR(50) | The type of track (e.g., Depot or Mainline). |
| @Type | NVARCHAR(20) | The type of TOA registration. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The unique identifier for the TAR. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number. |
| @TOAID | BIGINT OUTPUT | The unique identifier for the TOA registration. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the outcome of the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It creates a temporary table to store the results of the qualification checks for each QTS (Qualification Testing System) code.
3. The procedure then retrieves the cut-off time for the current day based on the line and track type.
4. It selects the QTS codes that apply to the current line and track type, as well as the corresponding protection types.
5. If the TAR is not found or does not match the expected status, the procedure sets an error message and returns without inserting into the TOA table.
6. The procedure then checks if the TAR has a valid QTS code and if the qualification status is valid. If not, it sets an error message and returns without inserting into the TOA table.
7. If the TAR has a valid QTS code and qualification status, the procedure inserts a new record into the TOA table with the required information.
8. The procedure then updates the TAR status to reflect the new TOA registration.
9. Finally, it logs the registration in the TAMS_TOA_Registration_Log table.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAMs_Station, TAMS_Parameters, TAMS_TOa, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA