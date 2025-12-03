# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202

### Purpose
This stored procedure performs a load of data for the RGS (Remote Grid System) onboarding process, including retrieving and processing relevant data from various tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to retrieve specific parameters. |

### Logic Flow
The procedure follows these steps:

1. It sets up two cursors, `@Cur01` and `@Cur02`, to iterate through the relevant data in the `TAMS_TAR` and `TAMS_TOA` tables.
2. For each iteration, it retrieves specific parameters such as `ARRemark`, `TVFMode`, `AccessType`, `TOAStatus`, `ProtTimeLimit`, `GrantTOATime`, `AckSurrenderTime`, `AckGrantTOATime`, `UpdateQTSTime`, and `InchargeNRIC`.
3. It then processes this data to determine the relevant RGS information, such as `ElectricalSections`, `PowerOffTime`, `CircuitBreakOutTime`, `PartiesName`, `NoOfPersons`, `WorkDescription`, `ContactNo`, `TOANo`, `CallBackTime`, `RadioMsgTime`, `LineClearMsgTime`, and `Remarks`.
4. It inserts this processed data into a temporary table, `#TmpRGS`.
5. Finally, it retrieves the data from the temporary table and returns it in a formatted output.

### Data Interactions
* **Reads:**
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_Parameters
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Get_ES
	+ TAMS_Get_TOA_TVF_Stations
* **Writes:**
	+ #TmpRGS