# Procedure: sp_TAMS_RGS_OnLoad_20221118
**Type:** Stored Procedure

The purpose of this stored procedure is to load data into various tables for a specific business task.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_Power_Sector, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters
* **Writes:** #TmpRGS, #TmpRGSSectors