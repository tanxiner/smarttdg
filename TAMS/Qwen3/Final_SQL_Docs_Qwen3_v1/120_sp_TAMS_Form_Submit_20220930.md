# Procedure: sp_TAMS_Form_Submit_20220930

### Purpose
This stored procedure is used to submit a TAR (Track Access Management System) form for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the TAR form being submitted. |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has already been started, and if not, it starts one.
2. It retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. It determines the sector color code for the TAR form being submitted, depending on the access type and exclusive status.
4. It inserts new records into the TAMS_TAR_Sector table for each sector in the @Sectors parameter.
5. It inserts new records into the TAMS_TAR_Station table based on the stations associated with the TAR form.
6. It determines if a power sector is involved, and if so, it inserts a record into the TAMS_TAR_Power_Sector table.
7. It checks if the TAR form type is 'Late' and if so, it determines the workflow ID to use for approval.
8. It updates the TAR form with the determined workflow ID, TAR status ID, and other relevant information.
9. It inserts a new record into the TAMS_TAR_Workflow table to track the submission of the TAR form.
10. If the TAR form type is 'Late', it sends an email to the HOD (Head of Department) user with a link to access the TAR form.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Sector, TAMS_Station, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Calendar, TAMS_Workflow, TAMS_Endorser, TAMS Paramaters.
* **Writes:** TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Workflow.