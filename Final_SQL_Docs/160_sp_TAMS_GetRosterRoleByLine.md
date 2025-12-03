# Procedure: sp_TAMS_GetRosterRoleByLine

### Purpose
Return the ordered list of roster roles for a specified line, track type, operation date, and shift, using either the base roster or the occurrence roster depending on data availability and line type.

### Parameters
| Name            | Type          | Purpose |
| :-------------- | :------------ | :------ |
| @Line           | nvarchar(10)  | Target line identifier; special handling when equal to 'DTL'. |
| @TrackType      | nvarchar(50)  | Category of the track to filter roster entries. |
| @OperationDate  | nvarchar(10)  | Date for which the roster should be retrieved. |
| @Shift          | nvarchar(1)   | Shift code used when selecting from the occurrence roster. |

### Logic Flow
1. Initialise a counter variable `@count` to zero.  
2. **If** the supplied line is `'DTL'`:  
   1. Count rows in `TAMS_OCC_Duty_Roster` that match the line, track type, and operation date.  
   2. **If** the count is zero (no occurrence data):  
      - Select `ID, Line, RosterCode, RoleId, [Order]` from `TAMS_Roster_Role` where the line and track type match, and the current date falls between `EffectiveDate` and `ExpiryDate`.  
      - Order the results by `[Order]` ascending.  
   3. **Else** (occurrence data exists):  
      - Select `ID, Line, RosterCode, [Shift] AS RoleId, ID AS [Order]` from `TAMS_OCC_Duty_Roster` where the line, track type, operation date, and shift match.  
      - Order the results by `[Order]` ascending.  
3. **Else** (line is not `'DTL'`):  
   1. Count rows in `TAMS_OCC_Duty_Roster` that match the line, track type, and operation date.  
   2. **If** the count is zero:  
      - Select `ID, Line, RosterCode, RoleId, [Order]` from `TAMS_Roster_Role` where the line and track type match, `RosterCode` is not `'SCO'`, and the current date is within the effective period.  
      - Order the results by `[Order]` ascending.  
   3. **Else**:  
      - Select `ID, Line, RosterCode, [Shift] AS RoleId, ID AS [Order]` from `TAMS_OCC_Duty_Roster` where the line, track type, operation date, and shift match.  
      - Order the results by `[Order]` ascending.  

The procedure returns the selected rows as a result set.

### Data Interactions
* **Reads:** `TAMS_OCC_Duty_Roster`, `TAMS_Roster_Role`  
* **Writes:** None
---