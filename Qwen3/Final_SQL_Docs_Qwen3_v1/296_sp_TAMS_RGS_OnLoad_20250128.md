# Procedure: sp_TAMS_RGS_OnLoad_20250128

### Purpose
This stored procedure performs a series of operations to retrieve and process data related to TAMS (Track and Maintenance System) for RGS (Railway Group Standardization) on-board equipment.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |
| @TrackType | NVARCHAR(50) | The track type used to filter the data. |

### Logic Flow

1. The procedure starts by setting up variables for the current date and time, as well as a cutoff time.
2. It then checks if the current time is after the cutoff time. If it is, the procedure sets the operation date to the current date and the access date to the next day. Otherwise, it sets the operation date to the previous day and the access date to the current date.
3. The procedure retrieves three parameters from the TAMS_Parameters table: RGSPossessionBG, RGSProtectionBG, and RGSCancelledBG, based on the line number provided.
4. It then checks if there are any existing possession controls for the specified line and track type. If there are, it sets a flag to 1; otherwise, it sets the flag to 0.
5. The procedure then selects data from the TAMS_TAR and TAMS_TOA tables based on the access date, track type, and line number provided. It orders the results by AccessType, TOAStatus, and TARId.
6. For each row in the result set, it calculates various values such as PowerOffTime, CircuitBreakOutTime, and CallBackTime using subqueries and case statements.
7. The procedure then joins the TAMS_TAR and TAMS_TOA tables again to retrieve additional data such as PartiesName, NoOfParties, WorkDescription, ContactNo, TOANo, and Remarks.
8. Finally, it orders the results by AccessType, TOAStatus, and TARId.

### Data Interactions

* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters
* **Writes:** None