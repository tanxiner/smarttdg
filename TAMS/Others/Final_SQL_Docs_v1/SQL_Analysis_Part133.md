# Procedure: sp_TAMS_RGS_OnLoad_Enq
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data from various tables in the database, specifically for the RGS (Radio Frequency System) system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number or type (DTL/NEL) to filter data |
| @TrackType | nvarchar(50) | The track type to filter data |
| @OPDate | NVARCHAR(20) | The operation date to filter data |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Sector, TAMS_Sector, TAMS_TAR_Power_Sector, TAMS_Access_Requirement, TAMS_Parameters
* **Writes:** #TmpRGS table