# Procedure: sp_TAMS_Depot_RGS_Update_Details20250403
**Type:** Stored Procedure

### Purpose
This stored procedure updates depot RGS details for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to update. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR_AccessReq, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties