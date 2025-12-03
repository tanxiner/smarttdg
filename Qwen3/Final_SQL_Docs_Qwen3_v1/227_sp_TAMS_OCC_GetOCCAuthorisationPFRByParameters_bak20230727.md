# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters_bak20230727

### Purpose
This stored procedure retrieves and processes OCC authorisation data for a given set of parameters, including user ID, line number, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number for which to retrieve data (optional). |
| @TrackType | nvarchar(50) | The track type for which to retrieve data (optional). |
| @OperationDate | date | The operation date for which to retrieve data. |
| @AccessDate | date | The access date for which to retrieve data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the line number is 'DTL' and retrieves the corresponding workflow ID.
2. If the line number is 'DTL', it then inserts data into temporary tables #TMP_Endorser and #TMP based on the retrieved workflow ID.
3. The procedure then creates a cursor to iterate over the OCCAuthID column in the #TMP_OCCAuthPFR table.
4. For each OCCAuthID, it iterates over the EndorserID column in the #TMP_Endorser table and updates the corresponding data in #TMP_OCCAuthPFR based on the EndorserLevel.
5. The procedure then checks the WFStatus for each EndorserID and updates the corresponding data in #TMP_OCCAuthPFR accordingly.
6. Finally, it selects all data from #TMP_OCCAuthPFR.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** None