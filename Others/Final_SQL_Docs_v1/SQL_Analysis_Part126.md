# Procedure: sp_TAMS_RGS_OnLoad_20221107
**Type:** Stored Procedure

### Purpose
This stored procedure performs a series of checks and updates for a specific business task, specifically related to the possession and authorization of transmission assets.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number being processed |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_Power_Sector, TAMS_Access_Requirement
* **Writes:** #TmpRGS, #TmpRGSSectors