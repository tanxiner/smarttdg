# Procedure: sp_TAMS_Depot_SectorBooking_OnLoad

### Purpose
This stored procedure performs a one-time load of sector booking data for depot sectors, including power zone and SPKS zone information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to process. |
| @TrackType | NVARCHAR(50) | The track type to process. |
| @AccessDate | NVARCHAR(20) | The access date for the sector booking data. |
| @TARType | NVARCHAR(20) | The TAR type to use for color code determination. |
| @AccessType | NVARCHAR(20) | The access type to determine operation requirements. |

### Logic Flow
1. The procedure starts by truncating a temporary table #ListES.
2. It then declares several variables, including @CurID, @CurLine, @CurSector, and @CurOrderID, which will be used to iterate through the sector booking data.
3. If the @Line parameter is 'NEL', it inserts data into #ListES from TAMS_Sector table based on the @TrackType parameter.
4. A cursor (@Cur01) is created to iterate through the sector booking data in TAMS_Sector table, filtering by Line and TrackType.
5. For each iteration, the procedure extracts power zone and SPKS zone information from TAMS_SPKSZone and TAMS_Power_Sector tables based on the SectorID.
6. It then determines the color code for the sector booking data using TAMS_TAR and TAMS_TAR_Sector tables.
7. If the @ColorCode is empty, it updates #ListES with the power zone and SPKS zone information. Otherwise, it updates #ListES with the existing color code.
8. Depending on the @AccessType parameter, it determines operation requirements from TAMS_Access_Requirement table.
9. Finally, it selects data from #ListES and returns it.

### Data Interactions
* **Reads:** 
	+ TAMS_Sector table
	+ TAMS_SPKSZone table
	+ TAMS_Power_Sector table
	+ TAMS_TAR table
	+ TAMS_TAR_Sector table
	+ TAMS_Access_Requirement table
* **Writes:** None