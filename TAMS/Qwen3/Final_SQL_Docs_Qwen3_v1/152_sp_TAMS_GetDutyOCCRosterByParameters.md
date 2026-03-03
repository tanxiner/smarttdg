# Procedure: sp_TAMS_GetDutyOCCRosterByParameters

### Purpose
This stored procedure retrieves a duty OCR roster by providing various parameters such as line, track type, operation date, shift, roster code, and ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter the roster by. |
| @TrackType | nvarchar(50) | The track type to filter the roster by. |
| @OperationDate | date | The operation date to filter the roster by. |
| @Shift | nvarchar(1) | The shift to filter the roster by. |
| @RosterCode | nvarchar(50) | The roster code to filter the roster by. |
| @ID | int | The ID of the duty OCR roster to retrieve. |

### Logic Flow
The procedure starts by selecting data from two tables: TAMS_OCC_Duty_Roster and TAMS_User. It filters the data based on the provided parameters, including line number, track type, operation date, shift, roster code, and ID. The procedure also checks if the duty OCR roster is active (IsActive = 1) before returning the results.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster and TAMS_User tables