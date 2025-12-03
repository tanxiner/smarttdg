# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL

### Purpose
This stored procedure retrieves and updates OCC (Operations Control Centre) authorisation data based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID for authentication purposes. |

### Logic Flow
The procedure follows these steps:

1. It first checks if a workflow exists with the specified Line, TrackType, and is active.
2. If a workflow exists, it retrieves endorser data from TAMS_Endorser table based on the workflow ID and line.
3. For each endorser, it updates corresponding fields in #TMP_OCCAuthNEL table based on the endorser's role and status.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_OCC_AuthNEL]