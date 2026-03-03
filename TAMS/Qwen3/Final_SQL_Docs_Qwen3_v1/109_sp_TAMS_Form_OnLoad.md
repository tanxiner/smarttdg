# Procedure: sp_TAMS_Form_OnLoad

### Purpose
This stored procedure performs a series of tasks to prepare data for form loading, including retrieving parameters, access requirements, and sector information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number. |
| @TrackType | NVARCHAR(50) | The track type. |
| @AccessDate | NVARCHAR(20) | The access date. |
| @AccessType | NVARCHAR(20) | The access type. |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text. |

### Logic Flow
1. Retrieve parameters from TAMS_Parameters based on the line number and access date.
2. Retrieve access requirements from TAMS_Access_Requirement based on the line number, track type, and access date.
3. If the access type is 'Protection', retrieve additional access requirements with specific conditions.
4. Otherwise, retrieve all access requirements without the protection condition.
5. Retrieve sector information from TAMS_Type_Of_Work based on the line number and track type.
6. Declare variables to store selected sectors that are not gaps and those that are gaps.
7. Populate these variables by selecting sectors from TAMS_Sector where the ID is in the list of provided sector IDs.
8. Select entry stations from TAMS_Station where the sector ID is in the list of provided sector IDs.
9. Create a temporary table to store power sector information and populate it with selected sectors.
10. Retrieve power on/off information for each sector.

### Data Interactions
* Reads: 
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
	+ TAMS_Type_Of_Work
	+ TAMS_Sector
	+ TAMS_Station
* Writes: None