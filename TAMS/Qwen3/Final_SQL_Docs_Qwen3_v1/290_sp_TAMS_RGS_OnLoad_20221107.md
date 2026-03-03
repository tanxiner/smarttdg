# Procedure: sp_TAMS_RGS_OnLoad_20221107

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it retrieves the RGS possession background (RGSPossBG) and protection background (RGSProtBG) values from the TAMS_Parameters table based on the line number (@Line).

The procedure then checks if the current time is greater than a certain cutoff time. If so, it sets the operation date to the current date and access date to the next day. Otherwise, it sets the operation date to the previous day and access date to the current date.

It then declares two cursors: @Cur01 for TAMS_TAR and TAMS_TOA tables, and @Cur02 for TAMS_TAR_Power_Sector table. The procedure iterates through each row in these tables, extracting relevant information such as TARNo, TOANo, PartiesName, NoOfPersons, WorkDescription, ContactNo, etc.

Based on the line number (@Line), it performs different operations:

- For 'DTL' lines:
  - It sets @lv_Remarks to a string containing the rack out remark and TVF mode.
  - If @lv_PossessionCtr is greater than 0, it sets @lv_IsGrantTOAEnable to 0. Otherwise, it sets @lv_IsGrantTOAEnable to 1.

- For other lines:
  - It sets @lv_Remarks to a string containing the TVF stations.
  - If @AccessType is 'Possession', it sets @lv_ColourCode to RGSPossBG and updates @lv_PossessionCtr accordingly. Otherwise, it sets @lv_ColourCode to RGSProtBG.

The procedure then inserts the extracted information into #TmpRGS table.

Finally, it fetches the operation date, access date, and other relevant information from #TmpRGS table and displays them in a list format.

### Data Interactions
* **Reads:**
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAR_Power_Sector
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
* **Writes:**
	+ #TmpRGS table
	+ #TmpRGSSectors table