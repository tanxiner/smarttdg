# Procedure: sp_TAMS_RGS_OnLoad_20230202_M

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
1. The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors.
2. It then retrieves the current date and time, as well as the operation and access dates for the day.
3. Based on the line number (@Line), it determines whether to process a DTL (Distribution Transformer Load) or NEL (Network Equipment Load) scenario.
4. For each line, it iterates through all TAMS_TAR records with an AccessDate matching the current date and TOAStatus not equal to 0 or 6.
5. It then fetches the corresponding TAMS_TOA record for each TARId and processes its data:
	* If the TOAStatus is 6 (cancelled), it updates the #TmpRGS table with the cancelled remark.
	* Otherwise, it populates the #TmpRGS table with various fields such as Sno, TARNo, ElectricalSections, PowerOffTime, CircuitBreakOutTime, PartiesName, NoOfPersons, WorkDescription, ContactNo, TOANo, CallbackTime, RadioMsgTime, LineClearMsgTime, Remarks, TOAStatus, IsTOAAuth, ColourCode, IsGrantTOAEnable, UpdQTSTime, AccessType, AckGrantTOATime, AckProtLimitTime, TARID, TOAID, and InchargeNRIC.
6. After populating the #TmpRGS table, it fetches the corresponding TAMS_TAR_Sector or TAMS_Power_Sector records for each line and processes their data:
	* For TAMS_TAR_Sector records, it updates the #TmpRGSSectors table with various fields such as OCCAuthStatusId, OperationDate, AccessDate, SectorID, Sector, WorkFlowTime.
	* For TAMS_Power_Sector records, it updates the #TmpRGSSectors table with various fields such as OCCAuthStatusId, OperationDate, AccessDate, PowerSectorId, WorkFlowTime.
7. Finally, it closes both cursors and deallocates resources.

### Data Interactions
* **Reads:**
	+ TAMS_TAR records
	+ TAMS_TOA records
	+ TAMS_TAR_Sector records
	+ TAMS_Power_Sector records
	+ TAMS_Parameters records (for retrieving RGS-related parameters)
* **Writes:**
	+ #TmpRGS table
	+ #TmpRGSSectors table