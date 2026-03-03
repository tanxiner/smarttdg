# Procedure: sp_TAMS_SummaryReport_OnLoad_20240112_M

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Asset Management System) on a specific date, providing insights into various aspects of the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL). |

### Logic Flow
The procedure follows these steps:

1. It determines the current date and time.
2. If the current time is before a specified cut-off time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the selected access date matches the specified date in the report. If not, it returns an error message.
4. It retrieves data from various tables (TAMS_TAR and TAMS_TOA) based on the line type, track type, and access date.
5. For each retrieved record, it categorizes the TAR status into one of five categories: Possession, Protection, Executed, Not Executed, and Cancelled.
6. It counts and lists the number of records in each category for both Possession and Protection lines.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA