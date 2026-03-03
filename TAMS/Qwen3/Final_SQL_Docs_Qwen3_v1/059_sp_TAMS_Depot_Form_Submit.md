# Procedure: sp_TAMS_Depot_Form_Submit

### Purpose
This stored procedure is used to submit a Depot Form for Urgent TAR (Track Access Management System) and update the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track type |
| @TrackType | NVARCHAR(50) | The track type of the depot form |
| @AccessDate | NVARCHAR(20) | The access date of the depot form |
| @AccessType | NVARCHAR(20) | The access type of the depot form |
| @TARType | NVARCHAR(10) | The type of TAR (Track Access Management System) |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction is already in progress and sets an internal transaction flag.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. It determines the sector color code for the depot form based on the access type and exclusive status.
4. It inserts the sector data into the TAMS_TAR_Sector table.
5. It inserts the station data into the TAMS_TAR_Station table.
6. It inserts the power sector data into the TAMS_TAR_Power_Sector table, first for non-buffer zones and then for buffer zones.
7. It inserts the SPKS zone data into the TAMS_TAR_SPKSZone table.
8. It inserts the attachment data from the TAMS_TAR_Attachment_Temp table into the TAMS_TAR_Attachment table.
9. If the TAR type is 'Urgent', it checks if Saturday, Sunday, and PH are included in the effective date range and updates the workflow status accordingly.
10. It generates a reference number for the depot form using the sp_Generate_Ref_Num stored procedure.
11. It updates the TAMS_TAR table with the new values.
12. If an error occurs during the insertion process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_SPKSZone, TAMS_TAR_Attachment_Temp, TAMS_TAR_AccessReq, TAMS_Workflow, TAMS_Endorser, TAMS Paramaters
* Writes: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_SPKSZone, TAMS_TAR_Attachment_Temp, TAMS_TAR_AccessReq, TAMS_Workflow, TAMS_Endorser