# Procedure: sp_TAMS_SummaryReport_OnLoad

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) by retrieving data from various tables based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL). |

### Logic Flow
The procedure follows these steps:

1. It checks if the current time is before a specified cut-off time based on the provided line and track type parameters.
2. If the current time is before the cut-off, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid for the selected report date.
4. If the access date is not valid, it returns an error message.
5. Otherwise, it retrieves data from various tables (TAMS_TAR, TAMS_TOA) based on the provided parameters and line type.
6. It calculates the number of approved tar for possession, protection, executed, and not executed categories.
7. It constructs lists of approved tar numbers for each category by concatenating the retrieved IDs.
8. Finally, it returns a summary report with the calculated values.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: None