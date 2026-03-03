# Procedure: sp_TAMS_OCC_GetOCCAuthorisationCCByParameters

### Purpose
This stored procedure retrieves OCC authorisation CC data by providing parameters such as user ID, line number, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID |

### Logic Flow
The procedure starts by checking if the provided line number is 'DTL'. If it is, it retrieves the workflow ID from the TAMS_Workflow table where the line number matches and the workflow type is 'OCCAuth' and the status is active. 

Next, it inserts data into temporary tables #TMP_Endorser and #TMP based on the retrieved workflow ID. The #TMP table contains traction power IDs with their corresponding station names, while the #TMP_Endorser table contains endorser IDs, levels, titles, and roles.

The procedure then selects OCCAuthID from the #TMP_OCCAuthCC temporary table and iterates through each value. For each OCCAuthID, it retrieves endorser ID, level, title, and role ID from the #TMP_Endorser table. 

Based on the retrieved endorser ID, it updates specific fields in the #TMP_OCCAuthCC table with values from the TAMS_OCC_Auth_Workflow table where the OCCAuthID matches.

Finally, it closes all cursors, deallocates memory, and selects all data from the #TMP_OCCAuthCC table for output.