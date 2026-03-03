# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116

### Purpose
Synchronises a set of duty roster records supplied via a table‑valued parameter with the persistent roster and audit tables, inserting new entries or updating existing ones.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | A table‑valued parameter containing one or more duty roster rows to be processed. |

### Logic Flow
1. Initialise counters and variables for the operation date, shift, and line.  
2. Extract the operation date, shift, and line from the first row of the supplied TVP.  
3. Count how many rows already exist in **TAMS_OCC_Duty_Roster** that match that operation date, shift, and line.  
4. **If no matching rows exist**  
   1. Insert every row from the TVP into **TAMS_OCC_Duty_Roster**.  
   2. For each inserted row, create an audit record in **TAMS_OCC_Duty_Roster_Audit** with the action code `'I'`.  
5. **If matching rows exist**  
   1. Update the existing roster rows whose ID, line, operation date, shift, and roster code match those in the TVP, setting the new duty staff ID, updated timestamp, and updated user.  
   2. For each updated row, create an audit record in **TAMS_OCC_Duty_Roster_Audit** with the action code `'U'`.  

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster  
* **Writes:** TAMS_OCC_Duty_Roster, TAMS_OCC_Duty_Roster_Audit