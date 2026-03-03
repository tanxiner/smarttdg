# Procedure: sp_TAMS_Form_Submit_20250313

### Purpose
This stored procedure is used to submit a new TAMS (Track Access Management System) form for review and approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track. |
| @TrackType | NVARCHAR(50) | The type of track (e.g., NEL, OCC). |
| @AccessDate | NVARCHAR(20) | The access date of the track. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Protection, Possession). |
| @TARType | NVARCHAR(10) | The type of TAMS form (e.g., Urgent, Standard). |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has already started and sets the internal transaction flag accordingly.
2. It retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. It determines the sector color code for the track based on the access type and exclusive status.
4. It inserts new records into the TAMS_TAR_Sector table, which includes the sector ID, buffer flag, and color code.
5. It inserts new records into the TAMS_TAR_Station table, which includes the station ID.
6. It determines whether to insert non-buffer power sector or buffer power sector based on the power selection value.
7. It inserts new records into the TAMS_TAR_Power_Sector table, which includes the power sector ID and power section.
8. It retrieves the attachment files from the TAMS_TAR_Attachment_Temp table and inserts them into the TAMS_TAR_Attachment table.
9. If the access type is 'Possession', it determines whether to add a buffer zone or not based on the cross-over indicator.
10. It updates the TAMS_TAR table with the new values, including the TAR ID, track type, status ID, and power on value.
11. It inserts a new record into the TAMS_TAR_Workflow table, which includes the workflow ID, endorser ID, user ID, and workflow status.
12. If the access type is 'Urgent', it sends an email to the HOD (Head of Department) with a link to access the TAR form.

### Data Interactions
* Reads: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Attachment_Temp, TAMS_TAR_Attachment, TAMS_Buffer_Zone, TAMS_TAMs, TAMS_Access_Requirement, TAMS_Workflow, TAMS Paramaters
* Writes: TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment, TAMS_TAR, TAMS_TAR_Workflow