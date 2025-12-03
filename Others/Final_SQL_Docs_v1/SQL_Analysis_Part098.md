# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216_M
**Type:** Stored Procedure

The procedure retrieves OCC authorisation data for a specified user ID, line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID		as int | The ID of the user to retrieve OCC authorisation data for. |
| @Line		as nvarchar(10) = NULL | The line number to filter by (optional). |
| @OperationDate as date | The operation date to filter by. |
| @AccessDate as date | The access date to filter by. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power_Detail], [TAMS_Station], [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** [TAMS_OCC_AuthTC]