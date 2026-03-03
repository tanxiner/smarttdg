# Procedure: sp_TAMS_GetDutyOCCRosterByParameters

### Purpose
Retrieve a single duty roster record that matches all supplied parameters and is active.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Filter by line identifier |
| @TrackType | nvarchar(50) | Filter by track type |
| @OperationDate | date | Filter by operation date |
| @Shift | nvarchar(1) | Filter by shift code |
| @RosterCode | nvarchar(50) | Filter by roster code |
| @ID | int | Filter by unique roster identifier |

### Logic Flow
1. The procedure receives the six parameters, with defaults for the first, second, fourth, fifth, and sixth.
2. It performs a SELECT that joins the duty roster table with the user table on the duty staff ID.
3. The WHERE clause applies the following filters in sequence:
   - The roster line equals @Line.
   - The roster track type equals @TrackType.
   - The roster duty staff ID matches a user ID in the user table.
   - The roster operation date equals @OperationDate.
   - The roster shift equals @Shift.
   - The roster code equals @RosterCode.
   - The roster ID equals @ID.
   - The roster record is marked active (IsActive = 1).
4. The SELECT returns the roster ID, line, operation date, shift, roster code, duty staff ID, and the user’s name as DutyStaffName.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User
* **Writes:** None

---