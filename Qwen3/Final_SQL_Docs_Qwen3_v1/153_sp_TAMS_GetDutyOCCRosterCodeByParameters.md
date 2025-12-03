# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParameters

### Purpose
This stored procedure retrieves a list of duty OCR roster codes for a specific user, filtered by line, track type, operation date, shift, and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve duty OCR roster codes for. |
| @Line | nvarchar(10) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (optional). |
| @OperationDate | date | The operation date to filter by. |
| @Shift | nvarchar(1) | The shift to filter by (optional). |

### Logic Flow
The procedure starts by selecting data from the TAMS_OCC_Duty_Roster and TAMS_User tables based on the provided parameters. It filters the results to include only active records with a non-'SCO' roster code.

1. The procedure begins by joining the TAMS_OCC_Duty_Roster table with the TAMS_User table on the DutyStaffId column.
2. It then applies the filter conditions for line, track type, operation date, shift, and user ID.
3. The results are limited to only include active records (IsActive = 1) and exclude any records with a roster code of 'SCO'.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User