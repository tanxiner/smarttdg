# Procedure: sp_TAMS_SummaryReport_OnLoad
**Type:** Stored Procedure

This procedure generates a summary report for TAMS (Tracking and Management System) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL) to filter TAR records. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter TAR records. |
| @StrAccDate | NVARCHAR(20) | Specifies the access date for which the report is generated. |

### Logic Flow
1. The procedure checks if the current time is before the cut-off time specified in the TAMS_Parameters table.
2. If the current time is before the cut-off time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It then checks if the access date is valid for the selected report date.
4. If the access date is not valid, it returns an error message.
5. Otherwise, it retrieves the TAR records for the specified line type and track type.
6. For each TAR record, it calculates the number of approved TARs (Possession or Protection) and the corresponding list of TAR numbers.
7. It also identifies the TARs that are not executed (Not Executed) and those that have been cancelled or extended.
8. Finally, it returns a summary report with the calculated values.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** None