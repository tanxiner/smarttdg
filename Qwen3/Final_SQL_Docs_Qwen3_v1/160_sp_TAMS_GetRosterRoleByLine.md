# Procedure: sp_TAMS_GetRosterRoleByLine

### Purpose
This stored procedure retrieves roster roles for a specific line, track type, operation date, and shift.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line to retrieve roster roles for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @OperationDate | nvarchar(10) | The operation date to filter by. |
| @Shift | nvarchar(1) | The shift to filter by. |

### Logic Flow
The procedure first checks if the input line is 'DTL'. If it is, it retrieves a count of records from TAMS_OCC_Duty_Roster where the line, track type, and operation date match. If no records are found, it retrieves roster roles from TAMS_Roster_Role where the line, track type, and effective/expiry dates match. If records are found for 'DTL', it then checks if a shift is specified. If a shift is specified, it retrieves roster roles from TAMS_OCC_Duty_Roster with the matching shift. If no shift is specified or no records were found for 'DTL', it retrieves roster roles from TAMS_Roster_Role without the SCO code.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_Roster_Role