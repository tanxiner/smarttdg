# Procedure: sp_TAMS_RGS_OnLoad_20221118_M

### Purpose
This stored procedure performs a series of tasks to load data into various tables, including TAMS_TAR and TAMS_TOA. The purpose is to update the status of possession and protection for each line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which data needs to be loaded |

### Logic Flow
The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors. It then sets the current date and time variables based on the input line.

Next, it checks if the current time is greater than a certain cutoff time (06:00:00). If true, it sets the operation date to the current date and the access date to the next day. Otherwise, it sets the operation date to the previous day and the access date to the current date.

The procedure then selects data from TAMS_TAR and TAMS_TOA tables based on the input line and access date. It loops through each record and performs the following steps:

1. Checks if the TOA status is 6 (cancelled). If true, it sets a flag indicating that the TOA has been cancelled.
2. Retrieves data from TAMS_TAMSSectors table for each sector ID in the current line.
3. Loops through each sector record and performs the following steps:
	* Checks if the sector ID exists in the TAMS_Sector table. If true, it inserts a new record into #TmpRGSSectors table.
	* Retrieves data from TAMS_TAR_Power_Sector table for each power sector ID in the current line.
4. Loops through each power sector record and performs the following steps:
	* Checks if the power sector ID exists in the TAMS_Power_Sector table. If true, it inserts a new record into #TmpRGSSectors table.
5. Inserts data from #TmpRGS temporary table into TAMS_TAR and TAMS_TOA tables.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAMSSectors
	+ TAMS_Power_Sector
	+ TAMS_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Parameters
* **Writes:** 
	+ #TmpRGS temporary table
	+ TAMS_TAR
	+ TAMS_TOA