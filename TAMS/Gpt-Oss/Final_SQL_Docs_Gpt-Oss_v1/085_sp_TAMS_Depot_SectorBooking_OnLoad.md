# Procedure: sp_TAMS_Depot_SectorBooking_OnLoad

### Purpose
Generate a sector‑level booking view for a specified line and track type, applying TAR status and access‑type rules, and return any required access operations.

### Parameters
| Name          | Type          | Purpose |
| :------------ | :------------ | :------ |
| @Line         | NVARCHAR(10)  | Target line identifier (e.g., 'NEL', 'DTL'). |
| @TrackType    | NVARCHAR(50)  | Track type filter for sectors and requirements. |
| @AccessDate   | NVARCHAR(20)  | Date used to locate the TAR record for the line. |
| @TARType      | NVARCHAR(20)  | TAR category indicator that influences color logic. |
| @AccessType   | NVARCHAR(20)  | Access mode ('Protection' or other) that determines requirement selection. |

### Logic Flow
1. **Temp Table Setup**  
   - Create a temporary table `#ListES` with columns for sector details, zone lists, selection flags, enable flag, color code, and order.  
   - Truncate the table to ensure it starts empty.

2. **Initial Sector Load (NEL only)**  
   - If the line is `NEL`, insert all active sectors for that line and track type into `#ListES`, setting `IsEnabled` to 1 and ordering by the sector order.

3. **Cursor Preparation**  
   - Declare a cursor that selects all active sectors for the specified line and track type, ordered by the sector order.

4. **Sector‑by‑Sector Processing**  
   For each sector fetched by the cursor:
   - Reset zone and color variables.
   - **SPKS Zone Aggregation**: Concatenate all active SPKS zones linked to the sector, removing the trailing comma.
   - **Power Zone Aggregation**: Concatenate all active power sectors (non‑buffer) linked to the sector, removing the trailing comma.
   - **TAR Lookup**: Retrieve the color code and access type from the TAR tables for the sector, matching the access date, line, track type, and an approved status (TARStatusId 9 for NEL, 8 for DTL). Only exclusive TARs are considered.
   - **Update Rules**  
     - If no color code is found, set `IsEnabled` to 1 and clear `ColorCode` while storing the zone lists.  
     - If a color code exists, update `ColorCode` and zone lists.  
       - If the TAR type is 2 or 3, the access type is `Protection`, the color code is empty, and the TAR access type is `Possession`, then enable the sector and clear the color.  
       - Otherwise, keep the sector disabled (commented out in code) and store the zone lists.

5. **Result Set**  
   - Select all columns from `#ListES`, ordered by `OrderID` and `SectorID`, to return the sector booking view.

6. **Access Requirement Retrieval**  
   - If the access type is `Protection`, select all active power‑required access requirements for the line and track type where the operation requirement is `'Traction Power ON'`.  
   - Otherwise, select all active power‑required access requirements for the line and track type.  
   - Return these rows as the second result set.

### Data Interactions
* **Reads:**  
  - `TAMS_Sector`  
  - `TAMS_SPKSZone` & `TAMS_Track_SPKSZone`  
  - `TAMS_Power_Sector` & `TAMS_Track_Power_Sector`  
  - `TAMS_TAR` & `TAMS_TAR_Sector`  
  - `TAMS_Access_Requirement`

* **Writes:**  
  - Temporary table `#ListES` (insert, update, truncate)  

---