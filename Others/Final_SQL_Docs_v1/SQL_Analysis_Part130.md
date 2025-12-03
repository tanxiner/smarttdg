# Procedure: sp_TAMS_RGS_OnLoad_20230202_M
**Type:** Stored Procedure

The purpose of this stored procedure is to load data into temporary tables for further processing and analysis.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number or type (DTL/NEL) |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Traction_Power_Detail, TAMS_Power_Sector, TAMS_Access_Requirement, TAMS_OCC_Auth
* **Writes:** #TmpRGS, #TmpRGSSectors