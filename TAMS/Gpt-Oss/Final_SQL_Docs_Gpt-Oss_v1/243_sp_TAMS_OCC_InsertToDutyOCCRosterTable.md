# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable

### Purpose
Insert or update duty roster records and log the action in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | A table-valued parameter containing one or more duty roster rows to be processed. |

### Logic Flow
1. Declare local variables for counting, looping, and holding key values.  
2. Extract the `operationdate`, `shift`, `line`, and `TrackType` from the first row of the input table.  
3. Count how many rows already exist in `TAMS_OCC_Duty_Roster` that match the extracted `TrackType` (case‑insensitive), `operationdate`, `shift`, and `line`.  
4. **If no matching rows exist** (`@count = 0`):  
   - Insert every row from the input table into `TAMS_OCC_Duty_Roster`.  
   - For each inserted row, insert a corresponding audit record into `TAMS_OCC_Duty_Roster_Audit` with `AuditAction` set to `'I'`.  
5. **If matching rows exist** (`@count > 0`):  
   - Update the existing rows in `TAMS_OCC_Duty_Roster` that have the same `ID`, `Line`, `TrackType`, `OperationDate`, `Shift`, and `RosterCode` as a row in the input table, setting `DutyStaffId`, `UpdatedOn`, and `UpdatedBy` to the values from the input.  
   - For each updated row, insert a corresponding audit record into `TAMS_OCC_Duty_Roster_Audit` with `AuditAction` set to `'U'`.  

### Data Interactions
* **Reads:** `TAMS_OCC_Duty_Roster` (count query).  
* **Writes:** `TAMS_OCC_Duty_Roster` (insert or update), `TAMS_OCC_Duty_Roster_Audit` (insert).