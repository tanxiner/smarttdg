# Procedure: sp_TAMS_Depot_Form_Submit
**Type:** Stored Procedure

The purpose of this stored procedure is to submit a Depot Form for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the depot form being submitted. |
| @TrackType | NVARCHAR(50) | The track type of the depot form being submitted. |
| @AccessDate | NVARCHAR(20) | The access date of the depot form being submitted. |
| @AccessType | NVARCHAR(20) | The access type of the depot form being submitted. |
| @TARType | NVARCHAR(10) | The type of TAR (Track Access Request) being submitted. |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sectors associated with the depot form. |
| @PowerSelVal | NVARCHAR(10) | The selected power value for the depot form. |
| @PowerSelTxt | NVARCHAR(100) | The text description of the selected power value for the depot form. |
| @IsExclusive | INT | A flag indicating whether the depot form is exclusive or not. |
| @HODForApp | NVARCHAR(20) | The login ID of the HOD (Head of Department) associated with the depot form. |
| @UserID | NVARCHAR(100) | The login ID of the user submitting the depot form. |
| @TARID | BIGINT | The ID of the TAR being submitted. |
| @Message | NVARCHAR(500) | An output parameter containing a message indicating the result of the submission process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Possession, TAMS_Workflow, TAMS Paramaters
* **Writes:** TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_SPKSZone, TAMS_TAR_Attachment