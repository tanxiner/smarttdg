# Procedure: sp_TAMS_SummaryReport_OnLoad_20240112_M
**Type:** Stored Procedure

The procedure generates a summary report for TAMS (Tracking and Management System) on a specific date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type |
| @StrAccDate | NVARCHAR(20) | Specifies the access date |

### Logic Flow
1. The procedure checks if the current time is before a specified cut-off time for the given line and track type.
2. If the current time is before the cut-off, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It then checks if the access date is valid (i.e., not earlier than the specified access date).
4. If the access date is valid, it retrieves and processes data for three categories:
	* Booked: TARs that are currently booked
	* Executed: TARs that have been executed (TOA surrendered after 0400)
	* Not Executed: TARs that have not been executed (not registered for TOA)
5. For each category, it retrieves and processes data by iterating through a cursor of TAR records.
6. It then returns the processed data in a structured format.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** None