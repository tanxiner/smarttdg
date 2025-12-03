# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202
**Type:** Stored Procedure

### Purpose
This stored procedure performs a series of checks and updates for a specific business task, including retrieving data from various tables and performing calculations based on the input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to retrieve specific parameters. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector, TAMS_TAR_AccessReq
* **Writes:** #TmpRGS, #TmpRGSSectors