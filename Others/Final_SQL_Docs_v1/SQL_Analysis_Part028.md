# Procedure: sp_TAMS_Depot_RGS_Update_Details
**Type:** Stored Procedure

The purpose of this stored procedure is to update depot RGS details for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to be updated. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR_AccessReq, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Parties_Audit
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Parties_Audit