# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParameters

### Purpose
Retrieve active duty roster entries for a specific user, filtered by line, track type, operation date, and shift, excluding entries with a roster code of 'SCO'.

### Parameters
| Name          | Type          | Purpose |
| :------------ | :------------ | :------ |
| @UserID       | int           | User identifier to match DutyStaffId. |
| @Line         | nvarchar(10)  | Line filter; optional. |
| @TrackType    | nvarchar(50)  | Track type filter; optional. |
| @OperationDate| date          | Operation date filter. |
| @Shift        | nvarchar(1)   | Shift filter; optional. |

### Logic Flow
1. Select columns ID, Line, OperationDate, Shift, RosterCode, DutyStaffId, and DutyStaffName from the roster and user tables.  
2. Implicitly join TAMS_OCC_Duty_Roster with TAMS_User on DutyStaffId = Userid.  
3. Apply filters:  
   - Line equals @Line.  
   - TrackType equals @TrackType.  
   - OperationDate equals @OperationDate.  
   - Shift equals @Shift.  
   - DutyStaffId equals @UserID.  
   - IsActive equals 1.  
   - RosterCode is not 'SCO'.  
4. Return the filtered rows.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User  
* **Writes:** None