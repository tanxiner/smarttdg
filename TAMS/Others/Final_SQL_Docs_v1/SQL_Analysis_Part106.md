# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters
**Type:** Stored Procedure

The procedure updates the OCC authorization status for a given user ID and OCC level.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to update. |
| @OCCAuthID | int | The ID of the OCC authorization to update. |
| @OCCLevel | int | The level of the OCC authorization to update. |
| @Line | nvarchar(10) | The line number for the OCC authorization. |
| @TrackType | nvarchar(50) | The type of track for the OCC authorization. |
| @RemarksPFR | nvarchar(1000) | The remarks for the PFR (Power Factor Record). |
| @SelectionValue | nvarchar(50) | The selected value for the OCC authorization. |
| @StationName | nvarchar(50) | The name of the station for the OCC authorization. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], [TAMS_OCC_Auth_Audit]
* **Writes:** [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], [TAMS_OCC_Auth_Audit]