# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParametersForTVFAck

This procedure retrieves a list of duty roster codes for a specific TVF (Training and Verification Facility) based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to filter by. |
| @Line | nvarchar(10) = NULL | The line number to filter by. |
| @TrackType | nvarchar(50) = NULL | The track type to filter by. |
| @OperationDate | date | The operation date to filter by. |
| @Shift | nvarchar(1) = NULL | The shift to filter by. |

### Logic Flow
The procedure starts by selecting data from the TAMS_OCC_Duty_Roster and TAMS_User tables based on the provided parameters. It filters the results to include only active records with a roster code that does not contain 'TC'. The final result set includes columns such as ID, Line, OperationDate, Shift, RosterCode, DutyStaffId, and DutyStaffName.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User