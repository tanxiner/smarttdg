# Procedure: sp_TAMS_SectorBooking_OnLoad_bak20230605

### Purpose
Generate sector booking information for a specified line and access date, including entry stations, color codes, and enablement flags, and return the data for both travel directions along with applicable access requirements.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., 'DTL', 'NEL') |
| @AccessDate | NVARCHAR(20) | Date of access in dd/mm/yyyy format |
| @TARType | NVARCHAR(20) | Type of TAR (e.g., '1', '2', '3') |
| @AccessType | NVARCHAR(20) | Access category ('Protection', 'Possession', etc.) |

### Logic Flow
1. **Temp Table Setup**  
   - Create `#ListES` with columns for sector details, flags, and display attributes.  
   - Truncate the table to ensure it starts empty.

2. **Initial Sector Load**  
   - If `@Line` is 'DTL', insert active sectors from `TAMS_Sector` where the line matches, ordering by `[Order]`.  
   - If `@Line` is 'NEL', perform a similar insert but set `DirID` based on `Direction` ('NB' → 1, else 2) and `IsChkPair` based on sector codes.  
   - All inserted rows have `IsEnabled` set to 1 initially.

3. **Cursor Processing of Sectors**  
   - Open a cursor over the same set of active sectors.  
   - For each sector record:  
     a. Build a comma‑separated list of active station codes from `TAMS_Station` joined with `TAMS_Entry_Station` where the sector matches.  
     b. Trim the trailing comma.  
     c. Retrieve the first matching TAR record for the sector on the specified `@AccessDate` where `TARStatusId = 8` (Approved) and `IsExclusive = 1`.  
        - Capture `ColourCode` and `AccessType` from the joined `TAMS_TAR` and `TAMS_TAR_Sector`.  
     d. **Update `#ListES` for the current sector**:  
        - If no `ColourCode` is found, set `IsEnabled = 1`, clear `ColorCode`, and store the entry station list.  
        - If a `ColourCode` exists, store it and the entry station list.  
          * If `@TARType` is '2' or '3', `@AccessType` is 'Protection', `ColourCode` is empty, and the TAR’s `AccessType` is 'Possession', then enable the sector and clear the color.  
          * Otherwise, disable the sector (`IsEnabled = 0`) while keeping the entry station list.

4. **Result Sets for Directions**  
   - Return two result sets: one where `DirID = 1` and another where `DirID = 2`, each ordered by `OrderID` and `SectorID`.

5. **Access Requirement Retrieval**  
   - If `@AccessType` is 'Protection', select active power‑required access requirements for the line where `OperationRequirement` is not 'Traction Power ON'.  
   - Otherwise, select all active power‑required access requirements for the line.  
   - Return this list as the final result set.

### Data Interactions
* **Reads:**  
  - `TAMS_Sector`  
  - `TAMS_Station`  
  - `TAMS_Entry_Station`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Access_Requirement`

* **Writes:**  
  - Temporary table `#ListES` (inserted and updated within the procedure only)