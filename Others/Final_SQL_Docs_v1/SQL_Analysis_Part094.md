# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters
**Type:** Stored Procedure

The procedure retrieves OCC authorisation data for a given set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID to retrieve data for. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_Station]
* **Writes:** [TAMS_OCC_Auth_Workflow]