# Procedure: sp_TAMS_RGS_OnLoad_20230202

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it retrieves the RGS possession background (RGSPossBG) and protection background (RGSProtBG) values from the TAMS_Parameters table based on the line number (@Line). If the current time is after a certain cutoff time, it sets the operation date to the current date; otherwise, it sets the operation date to the previous day.

The procedure then declares two cursors: @Cur01 and @Cur02. The first cursor fetches data from the TAMS_TAR and TAMS_TOA tables based on the line number (@Line) and access date (@AccessDate). The second cursor is used for electrical sector processing, but its logic is not fully explained in the provided code.

For each row fetched by the cursors, the procedure updates various fields in the #TmpRGS table. It also checks for certain conditions, such as the TOA status (6) and the possession counter, to determine whether to grant or cancel a TOA (Temporary Occupation Authorization).

Finally, the procedure inserts the updated data into the #TmpRGS table and fetches the next row from the cursors.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_TAR_Power_Sector, TAMS_Access_Requirement, TAMS_Traction_Power_Detail, TAMS_OCC_Auth, TAMS_Power_Sector
* **Writes:** #TmpRGS