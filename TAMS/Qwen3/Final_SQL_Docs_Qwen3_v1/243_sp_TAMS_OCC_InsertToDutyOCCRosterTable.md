# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable

### Purpose
This stored procedure inserts or updates a new record to the TAMS_OCC_Duty_Roster table based on the provided data from the @TAMS_OCC_DutyRoster READONLY parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | The input data to be inserted or updated in the TAMS_OCC_Duty_Roster table. |

### Logic Flow
The procedure checks if a record with the same operation date, shift, line, and track type already exists in the TAMS_OCC_Duty_Roster table for the provided @TAMS_OCC_DutyRoster READONLY parameter. If no matching record is found, it inserts a new record into the TAMS_OCC_Duty_Roster table along with an audit log entry. If a matching record is found, it updates the existing record in the TAMS_OCC_Duty_Roster table and also creates an audit log entry.

### Data Interactions
* **Reads:** @TAMS_OCC_DutyRoster
* **Writes:** TAMS_OCC_Duty_Roster, TAMS_OCC_Duty_Roster_Audit