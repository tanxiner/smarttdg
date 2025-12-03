# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the line is 'DTL' and retrieves the workflow ID from the TAMS_Workflow table.
2. If the line is 'DTL', it inserts data into two temporary tables: #TMP and #TMP_Endorser.
3. The procedure then iterates over each OCCAuthID in the #TMP_OCCAuthPFR table, retrieving the corresponding endorser data from the #TMP_Endorser table.
4. For each endorser ID, it updates the relevant fields in the #TMP_OCCAuthPFR table based on the workflow status and action taken by the endorser.
5. Finally, it selects all data from the #TMP_OCCAuthPFR table.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_Station], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** None