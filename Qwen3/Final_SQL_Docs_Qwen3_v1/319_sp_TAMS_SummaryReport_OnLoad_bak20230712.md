# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20230712

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) on load, providing an overview of possession and protection status for specific lines and track types.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL | Specifies the line number to filter by. |
| @TrackType	NVARCHAR(50) = NULL | Specifies the track type to filter by. |
| @StrAccDate	NVARCHAR(20) = NULL | Specifies the access date to filter by. |

### Logic Flow
1. The procedure starts by determining the current cut-off time for operations based on the provided line and track type.
2. It then checks if the current time is before the cut-off time, and if so, sets the access date to the previous day; otherwise, it sets the access date to the current date.
3. If the access date is not equal to the specified access date, an error message is returned.
4. The procedure then initializes counters for possession and protection status, as well as variables to store the corresponding line numbers.
5. It uses two cursors (TARNo and TARNo2) to iterate through the TAMS_TAR table, filtering by access type, power on status, and line/track type. The cursors exclude rows with a TOAStatus of 0.
6. For each row in the cursors, it increments the corresponding counter for possession or protection status and appends the line number to the CancelPoss or CancelProt variable if it is not already set.
7. After iterating through all rows, it calculates the total count of possession and protection status using another two counters (ExtPossCtr and ExtProtCtr).
8. Finally, the procedure returns a result set containing the counts for possession, protection, and extended status.

### Data Interactions
* Reads: TAMS_TAR table
* Writes: None