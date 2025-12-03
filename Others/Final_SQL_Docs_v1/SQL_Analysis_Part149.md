### Procedure: sp_TAMS_SummaryReport_OnLoad_Trace
**Type:** Stored Procedure

### Purpose
This stored procedure generates a summary report for a specific date and time, including possession and protection data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to filter by. |
| @StrAccDate | NVARCHAR(20) | The access date to filter by. |

### Logic Flow
1. Checks if the current time is before the cut-off time for the specified line.
2. If so, sets the access date to the previous day; otherwise, sets it to the current date.
3. Checks if the access date is valid (i.e., not earlier than the specified date).
4. If invalid, returns an error message; otherwise, proceeds with the report generation.
5. Retrieves possession and protection data for the specified line and access date.
6. Iterates through the data to count the number of possessions and protections.
7. Iterates through the data again to find any cancelled possessions or protections.
8. Calculates the total number of extended possessions and protections.
9. Returns the summary report, including counts of possessions, protections, cancellations, and extensions.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** None