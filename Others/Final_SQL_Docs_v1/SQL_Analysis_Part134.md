# Procedure: sp_TAMS_RGS_OnLoad_Enq_20221107
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data related to Traction Power Grid (TPG) sectors for a given line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the data needs to be retrieved. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector
* **Writes:** #TmpRGS, #TmpRGSSectors