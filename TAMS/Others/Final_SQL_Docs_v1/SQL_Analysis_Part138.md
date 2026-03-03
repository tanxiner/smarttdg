# Procedure: sp_TAMS_RGS_OnLoad_Trace
**Type:** Stored Procedure

The procedure performs a series of checks and inserts data into various tables based on user input.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used for authentication. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector, TAMS_TAR_Power_Sector
* **Writes:** #TmpRGS, #TmpRGSSectors