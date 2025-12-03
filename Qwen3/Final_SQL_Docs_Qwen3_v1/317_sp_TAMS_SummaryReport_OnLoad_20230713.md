# Procedure: sp_TAMS_SummaryReport_OnLoad_20230713

### Purpose
This stored procedure generates a summary report for TAMS (Tactical Air Missile System) operations, including possession and protection counts, cancellations, and extended periods.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL, 
| @StrAccDate	NVARCHAR(20) = NULL |

### Logic Flow
1. The procedure starts by determining the current date and time.
2. It then checks if the current time is before a specified cut-off time for operations. If so, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. The procedure then checks if the access date is valid for the selected report period. If not, it returns an error message.
4. It then retrieves counts of possession and protection TARS (Tactical Air Missile Systems) with specific statuses and lines.
5. Next, it iterates through a cursor of protection TARS to identify cancellations and updates the corresponding cancellation counters and strings.
6. Similarly, it iterates through a cursor of possession TARS to identify cancellations and updates the corresponding cancellation counters and strings.
7. Finally, it calculates extended periods for possession and protection TARS based on TOA (Tactical Operations Area) status and surrenders.
8. The procedure returns the calculated counts and statistics.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR table
	+ TAMS_TOA table
	+ TAMS_Parameters table
* **Writes:** None