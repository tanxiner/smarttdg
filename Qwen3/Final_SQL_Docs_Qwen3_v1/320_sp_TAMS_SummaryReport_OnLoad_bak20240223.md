# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20240223

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type ('DTL' or 'NEL') to filter TAMS data. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter TAMS data. |
| @StrAccDate | NVARCHAR(20) | Specifies the access date for which the report is generated. |

### Logic Flow
The procedure follows these steps:

1. It determines the cutoff time based on the provided line and track types.
2. If the current time is before the cutoff time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid for the selected report date. If not, it returns an error message.
4. It initializes counters and variables for possession, protection, and cancellation counts.
5. It queries TAMS_TAR table to retrieve possession and protection data based on the line type, track type, and access date.
6. It uses cursors to iterate through the retrieved data and update the counters and variables accordingly.
7. Finally, it returns the summary report with possession, protection, cancellation counts, and other relevant information.

### Data Interactions
* Reads: TAMS_TAR table for possession and protection data.
* Writes: None (the procedure only reads data from the database).