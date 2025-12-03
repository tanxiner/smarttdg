# Procedure: sp_TAMS_TAR_View_Detail_OnLoad

### Purpose
This stored procedure is used to view detailed information on a specific TAMS TAR record, including its status, access details, and related data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to be viewed. |
| @LogInUser | NVARCHAR(20) | The login user's username. |

### Logic Flow

1. The procedure starts by selecting the Line and AccessDate from the TAMS_TAR table where the ID matches the provided @TARID.
2. It then selects all columns from the TAMS_TAR table where the ID is equal to @TARID, which includes detailed information such as TARNo, TARType, Company, Designation, Name, OfficeNo, MobileNo, Email, SubmitDate, AccessDate, and more.
3. The procedure then performs several group-by operations on related tables:
	* TAMS_TAR_Sector: groups sectors by their ID and selects the SectorId where the IsBuffer flag is 0 or 1.
	* TAMS_TAR_Station: groups stations by their StationCode and selects the StationCode where the TARId matches @TARID and the station is active.
4. It then calculates the IsGap value based on the selected sectors, which indicates whether a sector is not gap (IsBuffer = 0) or gap (IsBuffer = 1).
5. The procedure then performs several SELECT operations on other related tables:
	* TAMS_TAR_AccessReq: selects access requirements for the TARId where the IsSelected flag is 1 and the OperationRequirement matches a specific ID.
	* TAMS_Possession: selects possession details for the TARId, including summary, work description, type of work, and more.
	* TAMS_Possession_Limit: selects limit details for the PossessionId, including type of protection limit and red flashing lamps location.
	* TAMS_Possession_WorkingLimit: selects working limit details for the PossessionId, including ID and red flashing lamps location.
	* TAMS_Possession_OtherProtection: selects other protection details for the PossessionId, including ID and other protection information.
	* TAMS_Possession_PowerSector: selects power sector details for the PossessionId, including ID, power on/off status, number of SCDs, and breaker out.
6. It then calculates the maximum workflow level, pending workflow count, and approved workflow count based on the TARId.
7. The procedure then performs several SELECT operations on workflows:
	* TAMS_TAR_Workflow: selects workflows for the TARId where the WFStatus is 'Approved' or 'Pending'.
8. Finally, it creates two temporary tables (#TmpExc and #TmpExcSector) to store excluded data and truncates them before selecting all sectors from the TAMS_Sector table that do not match any excluded data.

### Data Interactions
* Reads: 
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_TAR_Station
	+ TAMS_Access_Requirement
	+ TAMS_Possession
	+ TAMS_Possession_Limit
	+ TAMS_Possession_WorkingLimit
	+ TAMS_Possession_OtherProtection
	+ TAMS_Possession_PowerSector
	+ TAMS_TAR_Workflow
* Writes: None