# Procedure: sp_TAMS_SectorBooking_OnLoad

### Purpose
Loads sector booking details for a specified line and track type, applies TAR and access rules, and returns two ordered result sets for each direction along with applicable power operation requirements.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Identifier of the railway line (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Code for the track type. |
| @AccessDate | NVARCHAR(20) | Date string used to locate the relevant TAR record. |
| @TARType | NVARCHAR(20) | Indicator of TAR type; used to decide color logic. |
| @AccessType | NVARCHAR(20) | Access category (e.g., Protection, Possession) that influences requirement selection. |

### Logic Flow
1. Create a temporary table #ListES to hold sector information and flags.  
2. Truncate #ListES to ensure it starts empty.  
3. Declare variables for current sector processing and initialize @EntryStation and @ColorCode to empty strings.  
4. Insert base sector rows into #ListES from TAMS_Sector where the line, track type, active status, and effective dates match.  
   - For line DTL: set DirID to 1 when Direction is BB, otherwise 2; set IsChkPair to 1.  
   - For line NEL: set DirID to 1 when Direction is NB, otherwise 2; set IsChkPair to 0 for sectors 801_RT1, 803_RT3, 802_RT2, otherwise 1.  
5. Open a cursor over the same TAMS_Sector rows to process each sector sequentially.  
6. For each sector in the cursor:  
   a. Reset @EntryStation and @ColorCode.  
   b. Build @EntryStation by concatenating StationCode values from TAMS_Station joined with TAMS_Entry_Station where the station is active, an entry station, and the sector ID matches the current sector. Remove any trailing comma.  
   c. Retrieve @ColorCode and @CCAccessType from TAMS_TAR joined with TAMS_TAR_Sector where the TAR record matches the access date, line, status (DTL status 8 or NEL status 9), IsExclusive=1, and the sector ID matches.  
   d. If @ColorCode is empty, update the #ListES row for the current sector: set IsEnabled=1, clear ColorCode, and store @EntryStation.  
   e. If @ColorCode is not empty, update ColorCode and EntryStation. Then apply additional rules:  
      - If @TARType is 2 or 3, @AccessType is Protection, @ColorCode is empty, and @CCAccessType is Possession, set IsEnabled=1, clear ColorCode, and store @EntryStation.  
      - Otherwise, set IsEnabled=0 and store @EntryStation.  
7. Close and deallocate the cursor.  
8. Return two result sets:  
   - First, rows from #ListES where DirID=1, ordered by OrderID and SectorID.  
   - Second, rows from #ListES where DirID=2, ordered similarly.  
9. Finally, based on @AccessType, select operation requirements from TAMS_Access_Requirement where Line and TrackType match, IsPowerReq=1, IsActive=1, and:  
   - If @AccessType is Protection, exclude rows where OperationRequirement is 'Traction Power ON'.  
   - Otherwise, include all matching rows. Order the results by Order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Station, TAMS_Entry_Station, TAMS_TAR, TAMS_TAR_Sector, TAMS_Access_Requirement  
* **Writes:** #ListES (insert and update operations only; no permanent tables are modified)