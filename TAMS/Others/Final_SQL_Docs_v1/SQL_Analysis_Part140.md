# Procedure: sp_TAMS_RGS_Update_Details
**Type:** Stored Procedure

The purpose of this stored procedure is to update details of a TAR (Terminal Acceptance Record) and its associated parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be updated. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_QTS_Error_Log
* **Writes:** TAMS_TOA_Audit, TAMS_TOA_Parties_Audit, TAMS_TOA_Parties