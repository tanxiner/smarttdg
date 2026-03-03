# Procedure: sp_TAMS_OPD_OnLoad

### Purpose
Retrieve sector and coordinate information for a specified line and track type, organized by direction, and return the relevant operation and access dates.

### Parameters
| Name       | Type          | Purpose |
| :--------- | :------------ | :------ |
| @Line      | NVARCHAR(20)  | Line identifier used to filter sectors and to determine direction logic. |
| @TrackType | NVARCHAR(50)  | Track type used to filter sectors. |

### Logic Flow
1. **Current Date/Time Capture**  
   - `@CurDate` is set to today’s date.  
   - `@CurTime` is set to the current time (HH:MM:SS).  

2. **Determine Operation and Access Dates**  
   - A cutoff time of 06:00:00 is defined.  
   - If the current time is after the cutoff, the operation date is today and the access date is tomorrow.  
   - If the current time is before the cutoff, the operation date is yesterday and the access date is today.  

3. **Prepare Access Date String**  
   - `@AccessDateStr` is the access date formatted as `dd/mm/yyyy`.  

4. **Create Temporary Table**  
   - `#TmpOPD` is created with columns for direction, sector details, coordinates, and two information fields.  
   - The table is truncated (cleared) to ensure it starts empty.  

5. **Populate Temporary Table**  
   - Rows are inserted from `TAMS_Sector` joined with `TAMS_Track_Coordinates` on sector ID.  
   - `DirID` is calculated:  
     - For line `DTL`, direction `BB` maps to 1, others to 2.  
     - For other lines, direction `NB` maps to 1, others to 2.  
   - `TARInformation` and `BGColor` are derived by calling `dbo.TAMS_Get_TOA_WPCount` with the line, sector ID, and access date string, then splitting the result on `;` and selecting the second and first values respectively.  
   - The join is filtered by the supplied `@Line` and `@TrackType`.  

6. **Return Direction‑Based Result Sets**  
   - **Dir2 Above**: Select rows where `DirID` equals 2 (or 1 when the line is not `DTL`) and `DHorizontalX` is non‑zero, ordered by `SectorID`.  
   - **Dir1 Below**: Select rows where `DirID` equals 1 (or 2 when the line is not `DTL`) and `DHorizontalX` is non‑zero, ordered by `SectorID`.  

7. **Return Dates**  
   - The procedure outputs the formatted operation and access dates.  

8. **Cleanup**  
   - The temporary table `#TmpOPD` is dropped.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_Track_Coordinates`  
* **Writes:** None (only temporary table operations)