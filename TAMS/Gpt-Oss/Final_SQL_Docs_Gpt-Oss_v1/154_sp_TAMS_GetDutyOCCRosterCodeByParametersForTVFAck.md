# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParametersForTVFAck

### Purpose
Retrieve the active duty roster record for a specific user that matches the supplied line, track type, operation date, and shift, excluding roster codes containing “TC”.

### Parameters
| Name           | Type          | Purpose |
| :---           | :---          | :--- |
| @UserID        | int           | The ID of the duty staff to filter the roster record. |
| @Line          | nvarchar(10)  | The production line identifier to filter the roster record. |
| @TrackType     | nvarchar(50)  | The track type to filter the roster record. |
| @OperationDate | date          | The date of operation to filter the roster record. |
| @Shift         | nvarchar(1)   | The shift identifier to filter the roster record. |

### Logic Flow
1. Join the tables `TAMS_OCC_Duty_Roster` (alias `r`) and `TAMS_User` (alias `u`) on `r.DutyStaffId = u.Userid`.  
2. Apply the following filters to the joined result set:  
   - `r.Line` equals the supplied `@Line`.  
   - `r.TrackType` equals the supplied `@TrackType`.  
   - `r.OperationDate` equals the supplied `@OperationDate`.  
   - `r.[shift]` equals the supplied `@Shift`.  
   - `r.DutyStaffId` equals the supplied `@UserID`.  
   - `r.IsActive` is 1.  
   - `r.RosterCode` does not contain the substring “TC”.  
3. Select the columns `ID`, `Line`, `OperationDate`, `[Shift]`, `RosterCode`, `DutyStaffId`, and the user’s name as `DutyStaffName` from the filtered rows.  
4. Return the resulting set to the caller.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User  
* **Writes:** None