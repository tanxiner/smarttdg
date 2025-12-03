# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116_M

### Purpose
This stored procedure inserts or updates a record in the TAMS_OCC_Duty_Roster table based on the provided data from the @TAMS_OCC_DutyRoster READONLY parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | The input data to be inserted or updated in the TAMS_OCC_Duty_Roster table. |

### Logic Flow
The procedure checks if a record with the same operation date, shift, and line already exists in the TAMS_OCC_Duty_Roster table. If no record is found, it inserts a new record into the table along with an audit log entry. If a record is found, it updates the existing record with the provided data and also creates an audit log entry.

### Data Interactions
* **Reads:** @TAMS_OCC_DutyRoster (the input data)
* **Writes:** TAMS_OCC_Duty_Roster (for insertion or update), TAMS_OCC_Duty_Roster_Audit (for audit log entries)