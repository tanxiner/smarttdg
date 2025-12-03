# Procedure: sp_TAMS_Depot_Approval_OnLoad

### Purpose
This stored procedure performs a series of checks and operations on a TAMS Depot Approval, including verifying sector conflicts, checking access requirements, and updating workflow statuses.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS Depot to be approved. |

### Logic Flow

1. The procedure starts by selecting relevant data from the TAMS_TAR table based on the provided TARID.
2. It then performs a series of checks and operations, including:
	* Verifying sector conflicts using the TAMS_Sector table.
	* Checking access requirements for traction power and other operations.
	* Updating workflow statuses for approved and pending workflows.
3. The procedure also updates the #TmpExc table to track any sector conflicts or exceptions that need to be addressed.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR
	+ TAMS_Sector
	+ TAMS_Power_Sector
	+ TAMS_SPKSZone
	+ TAMS_TAR_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Type_Of_Work
	+ TAMS_User
	+ TAMS_TAR_Workflow
	+ TAMS_Endorser
* **Writes:** 
	+ #TmpExc (temporary table to track sector conflicts and exceptions)
	+ #TmpExcSector (temporary table to store sector data)