# Procedure: sp_TAMS_Form_Submit

### Purpose
This stored procedure submits a new TAR (Track Access Request) form for approval and updates the associated records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track. |
| @TrackType | NVARCHAR(50) | The type of track. |
| @AccessDate | NVARCHAR(20) | The access date. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Protection, Possession). |
| @TARType | NVARCHAR(10) | The type of TAR (e.g., Urgent). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelVal | NVARCHAR(10) | The selected power value. |
| @PowerSelTxt | NVARCHAR(100) | The text description of the power selection. |
| @IsExclusive | INT | A flag indicating whether the TAR is exclusive. |
| @HODForApp | NVARCHAR(20) | The HOD login ID for the application. |
| @UserID | NVARCHAR(100) | The user ID submitting the form. |
| @TARID | BIGINT | The ID of the new TAR to be created. |
| @Message | NVARCHAR(500) | An output parameter containing a message about the result of the procedure. |

### Logic Flow
1. The procedure checks if there are any open transactions and sets an internal transaction flag accordingly.
2. It retrieves the user ID from the TAMS_User table based on the provided user ID.
3. If the access type is 'Protection' and the TAR is exclusive, it selects the sector color code from the TAMS_Type_Of_Work table.
4. The procedure inserts a new record into the TAMS_TAR_Sector table with the selected sector color code and other relevant details.
5. It inserts records into the TAMS_TAR_Station table based on the station IDs in the Sectors input parameter.
6. The procedure checks if there are any power sectors that need to be inserted, either for non-buffer or buffer zones, and inserts them accordingly.
7. If the TAR type is 'Urgent', it determines whether Saturday, Sunday, or PH should be considered and updates the workflow status accordingly.
8. It generates a reference number for the new TAR using the sp_Generate_Ref_Num stored procedure.
9. The procedure updates the TAMS_TAR table with the generated reference number, TAR type, and other relevant details.
10. If there are any errors during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Type_Of_Work, TAMS_Sector, TAMS_Station, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Calendar, TAMS Paramaters, TAMS_Access_Requirement, TAMS_Endorser, TAMS_Workflow
* Writes: TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment, TAMS_TAR_Workflow