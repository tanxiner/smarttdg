# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116_M

### Purpose
Insert or update duty roster records for a specific operation date, shift, and line, and record the change in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | A table-valued parameter containing one or more duty roster rows to be processed. |

### Logic Flow
1. **Initialize variables** – `@count`, `@loop`, `@operationdate`, `@shift`, and `@line` are declared.  
2. **Extract key identifiers** – The first row of `@TAMS_OCC_DutyRoster` supplies `@operationdate`, `@shift`, and `@line`.  
3. **Check for existing roster** – Count rows in `TAMS_OCC_Duty_Roster` that match the extracted `operationdate`, `shift`, and `line`.  
4. **If no existing roster** (`@count = 0`):  
   - **Insert** all rows from `@TAMS_OCC_DutyRoster` into `TAMS_OCC_Duty_Roster`.  
   - **Audit** the insertion by inserting a row into `TAMS_OCC_Duty_Roster_Audit` for each inserted record, marking `AuditAction` as `'I'`.  
5. **If a roster already exists** (`@count > 0`):  
   - **Update** matching rows in `TAMS_OCC_Duty_Roster` using the `ID`, `Line`, `OperationDate`, `Shift`, and `RosterCode` from `@TAMS_OCC_DutyRoster`. Only `DutyStaffId`, `UpdatedOn`, and `UpdatedBy` are changed.  
   - **Audit** the update by inserting a row into `TAMS_OCC_Duty_Roster_Audit` for each updated record, marking `AuditAction` as `'U'`.  

### Data Interactions
* **Reads:**  
  - `TAMS_OCC_Duty_Roster`  
  - `@TAMS_OCC_DutyRoster` (table-valued parameter)  

* **Writes:**  
  - `TAMS_OCC_Duty_Roster` (INSERT or UPDATE)  
  - `TAMS_OCC_Duty_Roster_Audit` (INSERT)