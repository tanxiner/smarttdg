# Procedure: sp_TAMS_Form_Submit_20220930
**Type:** Stored Procedure

The purpose of this stored procedure is to submit a TAR (Track and Record) form for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number associated with the TAR form. |
| @AccessDate | NVARCHAR(20) | The date of access to the TAR form. |
| @AccessType | NVARCHAR(20) | The type of access (e.g., Protection, Possession). |
| @TARType | NVARCHAR(10) | The type of TAR form (e.g., Late, Standard). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelVal | NVARCHAR(10) | The selected power value. |
| @PowerSelTxt | NVARCHAR(100) | The text description of the power selection. |
| @IsExclusive | INT | A flag indicating whether the TAR form is exclusive. |
| @HODForApp | NVARCHAR(20) | The HOD (Head of Department) for the application. |
| @UserID | NVARCHAR(20) | The user ID associated with the TAR form. |
| @TARID | BIGINT | The ID of the TAR form being submitted. |
| @Message | NVARCHAR(500) | An output parameter containing a message about the submission result. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Calendar, TAMS_Workflow, TAMS_Endorser, TAMS Paramaters.
* **Writes:** TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment, TAMS_Buffer_Zone, TAMS_Calendar, TAMS_Workflow, TAMS_Endorser.