# Procedure: sp_TAMS_RGS_OnLoad_20230707

### Purpose
This stored procedure performs a daily load of TAMS RGS data, including reading and processing various tables to generate reports.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used for parameterization |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets up various variables, including the current date and time, cutoff times, and parameters.

1. If the current time is after the cutoff time, it sets the operation date to the current date and the access date to the next day.
2. Otherwise, it sets the operation date to the previous day and the access date to the current date.
3. The procedure then selects various parameters from TAMS_Parameters based on the line number.
4. It uses two cursors (@Cur01 and @Cur02) to iterate through the TAMS_TAR table, selecting relevant data for each row.
5. For each row, it generates a new record in #TmpRGS by combining data from various tables, including TAMS_TOA, TAMS_TAR_Sector, and TAMS_TAR_Power_Sector.
6. It also inserts data into #TmpRGSSectors based on the sector ID.
7. After processing all rows, it fetches the final records from @Cur01 and inserts them into #TmpRGS.
8. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Power_Sector, TAMS_Parameters, TAMS_OCC_Auth
* **Writes:** #TmpRGS, #TmpRGSSectors