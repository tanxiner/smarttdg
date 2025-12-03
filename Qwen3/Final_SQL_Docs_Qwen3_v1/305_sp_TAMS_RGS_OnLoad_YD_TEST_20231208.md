# Procedure: sp_TAMS_RGS_OnLoad_YD_TEST_20231208

### Purpose
This stored procedure performs a series of operations to load data into temporary tables for further processing, specifically for the RGS (Remote Grid System) system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
1. The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors.
2. It then sets the current date and time variables based on the system clock.
3. Depending on the value of @Line (either 'DTL' or 'NEL'), it performs different operations:
	* For 'DTL', it checks for rackout records, calculates possession counters, and updates grant TOA enable flags.
	* For 'NEL', it follows a similar process but with some differences in logic.
4. It then fetches data from the TAMS_TAR and TAMS_TOA tables based on the specified line number and track type.
5. The procedure processes each record by:
	* Calculating possession counters
	* Updating grant TOA enable flags
	* Setting colors for rackout and grant TOA records
	* Inserting data into #TmpRGS
6. After processing all records, it fetches the operation date and access date.
7. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Sector, TAMS_Sector, TAMS_Parameters
* **Writes:** #TmpRGS