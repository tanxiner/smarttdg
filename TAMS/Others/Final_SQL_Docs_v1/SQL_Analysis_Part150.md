# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20240223
**Type:** Stored Procedure

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type ('DTL' or 'NEL') to filter TAMS data. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter TAMS data. |
| @StrAccDate | NVARCHAR(20) | Specifies the access date for which the report is generated. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters tables
* **Writes:** None