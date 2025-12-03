# Procedure: sp_TAMS_Depot_Form_OnLoad

### Purpose
This stored procedure performs a series of checks and calculations to determine the availability of depot access for a given line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number being processed. |
| @TrackType | NVARCHAR(50) | The track type of the line. |
| @AccessDate | NVARCHAR(20) | The access date for which depot access is being checked. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Possession, Protection). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text. |

### Logic Flow
1. The procedure first checks if the selected sectors are DW only by comparing them with the DWSectors value from TAMS_Parameters.
2. It then retrieves the Company name and other relevant information for the given line, access date, and track type.
3. Next, it selects the Access Requirement records based on the line, track type, and access date.
4. Depending on the access type, it either retrieves or filters the Access Requirement records further.
5. The procedure then calculates the availability of depot access by checking if there are any approved TARs for the selected sectors in TAMS_TAR_Sectors.
6. If the access is for a weekend or PH, it checks if there are any approved TARs for the selected sectors in TAMS_TAR_Sectors and returns 'false' otherwise.
7. Finally, the procedure creates a temporary table to store the power sector information and executes a query to retrieve the power on/off status.

### Data Interactions
* Reads: 
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
	+ TAMS_Sector
	+ TAMS_Power_Sector
	+ TAMS_Track_Power_Sector
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_Role
* Writes: 
	+ #TmpPossPowSector (temporary table)