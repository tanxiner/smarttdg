# Procedure: sp_TAMS_RGS_OnLoad_20221118

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it selects the RGS parameters (RGSPossessionBG and RGSProtectionBG) based on the line number (@Line). If the current time is after a certain cutoff time ('06:00:00'), it sets the operation date to the current date; otherwise, it sets it to the previous day.

The procedure then declares two cursors (@Cur01 and @Cur02) to iterate through the TAMS_TAR and TAMS_TOA tables. For each row in these tables, it extracts various fields such as TARNo, TOANo, PartiesName, NoOfPersons, WorkDescription, ContactNo, etc.

Based on the line number (@Line), it performs different operations:

* If @Line = 'DTL', it sets the Remarks field to a combination of the ARRemark and TVFMode values.
* If @Line = 'NEL', it sets the Remarks field to a specific value indicating that it's a NEL (Network Extension Line) operation.

The procedure then inserts data into #TmpRGS based on the extracted fields. It also updates various counters and flags, such as PossessionCtr, IsGrantTOAEnable, etc.

Finally, it fetches the Sno, TARNo, ElectricalSections, PowerOffTime, CircuitBreakOutTime, PartiesName, NoOfPersons, WorkDescription, ContactNo, TOANo, CallbackTime, RadioMsgTime, LineClearMsgTime, Remarks, TOAStatus, IsTOAAuth, ColourCode, IsGrantTOAEnable, UpdQTSTime, AccessType, AckGrantTOATime, AckProtLimitTime, TARID, TOAID, and InchargeNRIC from #TmpRGS and orders the results by Sno.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector, TAMS_Access_Requirement, TAMS_Parameters.
* **Writes:** #TmpRGS, #TmpRGSSectors.