# Procedure: sp_TAMS_RGS_OnLoad_M

### Purpose
This stored procedure performs a daily maintenance task for the RGS (Remote Grid System) system, updating and populating various tables with data from the TAMS (Transmission Automation Management System) database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors, which are used to store intermediate data during the processing.

1. It then retrieves the current date and time.
2. Based on the value of @Line, it determines whether to use the sector or power sector cursor to retrieve data from TAMS_TAR and TAMS_TAR_Power_Sector tables.
3. For each record retrieved, it populates a temporary table with various fields such as ElectricalSections, PowerOffTime, PartiesName, etc.
4. It then inserts these records into #TmpRGS.
5. After processing all records, it fetches the final data from #TmpRGS and orders it by Sno.
6. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector
* **Writes:** #TmpRGS