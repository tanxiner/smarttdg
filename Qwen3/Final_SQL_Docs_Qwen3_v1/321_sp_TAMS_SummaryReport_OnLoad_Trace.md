# Procedure: sp_TAMS_SummaryReport_OnLoad_Trace

### Purpose
This stored procedure generates a summary report for TAMS (Tactical Air Missile System) on-load tracing, providing an overview of possession and protection status for specific lines and dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL | Specifies the line number to filter by. |
| @StrAccDate	NVARCHAR(20) = NULL | Specifies the access date to filter by. |

### Logic Flow
The procedure follows these steps:

1. It determines the current cut-off time for operations based on the provided line number.
2. If the current time is before the cut-off time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid and not ready for reporting (i.e., not equal to the specified access date).
4. If the access date is valid, it retrieves counts of possession and protection status for specific lines and dates from TAMS_TAR and TAMS_TOA tables.
5. It iterates through the retrieved data using cursors to identify canceled possessions and protections by checking if a line is not in the TOA table with a non-zero status.
6. It calculates additional counters for extended possession and protection statuses based on specific conditions (e.g., TOAStatus = 3 or SurrenderTime > '04:00:00').
7. Finally, it returns the calculated counts as output.

### Data Interactions
* Reads:
	+ TAMS_TAR table
	+ TAMS_TOA table
* Writes:
	+ None