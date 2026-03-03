# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202_M

### Purpose
This stored procedure performs a load of data for the RGS (Radio Frequency System) onboarding process, including retrieving and processing data from various tables in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to be processed. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure a clean start.
2. It retrieves the current date and time using the GETDATE() function.
3. It sets up variables for the operation date and access date based on the current date and time.
4. If the current time is greater than 6:00 AM, it sets the operation date to the current date; otherwise, it sets it to the previous day's date.
5. It retrieves parameters from the TAMS_Parameters table using the @Line parameter.
6. It loops through each sector in the TAMS_TAR_Power_Sector or TAMS_TAR_Sector tables and processes the data accordingly:
	* For sectors with a power sector ID, it inserts data into #TmpRGSSectors.
	* For sectors without a power sector ID, it inserts data into #TmpRGS.
7. It retrieves additional parameters from the TAMS_TAR table using the @Line parameter.
8. If the line number is 'DTL', it sets up variables for the electrical sections and parties name based on the retrieved data.
9. It loops through each record in the TAMS_TOA table and processes the data accordingly:
	* For records with a TOA status of 6, it inserts data into #TmpRGS.
	* For records without a TOA status of 6, it sets up variables for the electrical sections and parties name based on the retrieved data.
10. It inserts the processed data from #TmpRGS into the TAMS_TAR table.
11. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:**
	+ TAMS_Parameters
	+ TAMS_TAR_Power_Sector
	+ TAMS_TAR_Sector
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAMSSectors
* **Writes:**
	+ #TmpRGS
	+ #TmpRGSSectors
	+ TAMS_TAR