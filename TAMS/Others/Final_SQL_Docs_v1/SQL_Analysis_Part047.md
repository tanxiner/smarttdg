# Procedure: sp_TAMS_Form_Submit
**Type:** Stored Procedure

The purpose of this stored procedure is to submit a new TAMS (Track Access Management System) form and update the relevant records accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number associated with the form submission. |
| @TrackType | NVARCHAR(50) | The track type associated with the form submission. |
| @AccessDate | NVARCHAR(20) | The access date associated with the form submission. |
| @AccessType | NVARCHAR(20) | The access type associated with the form submission. |
| @TARType | NVARCHAR(10) | The TAMS type associated with the form submission. |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sectors associated with the form submission. |
| @PowerSelVal | NVARCHAR(10) | The power selection value associated with the form submission. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text associated with the form submission. |
| @IsExclusive | INT | A flag indicating whether the form is exclusive or not. |
| @HODForApp | NVARCHAR(20) | The HOD for the application associated with the form submission. |
| @UserID | NVARCHAR(100) | The user ID associated with the form submission. |
| @TARID | BIGINT | The TAMS ID associated with the form submission. |
| @Message | NVARCHAR(500) | An output parameter containing a message indicating the result of the procedure. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Sector, TAMS_Station, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Access_Requirement, TAMS_Workflow, TAMS Paramaters
* **Writes:** TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment