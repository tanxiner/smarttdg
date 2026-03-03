# Procedure: sp_TAMS_RGS_OnLoad_Trace

### Purpose
Generates a trace of RGS activities for a specified line and access date, producing a detailed RGS list and a cancel list.

### Parameters
| Name   | Type          | Purpose |
| :----- | :------------ | :------ |
| @Line  | NVARCHAR(20)  | Identifier of the line (e.g., DTL, NEL). |
| @ADStr | NVARCHAR(20)  | Access date string in dd/mm/yyyy format. |

### Logic Flow
1. **Setup Temporary Tables** – Create `#TmpRGS` for final output and `#TmpRGSSectors` for intermediate sector data; truncate them to ensure clean state.  
2. **Determine Dates** – Convert `@ADStr` to a date (`@AccessDate`) and set `@OperationDate` to the previous day.  
3. **Retrieve Background Colours** – Query `TAMS_Parameters` for possession and protection background colours based on the line.  
4. **Open Main Cursor** – Select TAR and TOA records where `AccessDate` matches, `Line` matches, `AccessType` is `Protection`, and `TOAStatus` is not zero.  
5. **Process Each Record**  
   - Increment line counter (`@lv_Sno`).  
   - Initialise flags and placeholders for power off, circuit break, colour, etc.  
   - Call helper functions to get ES, parties, contact numbers, and TVF stations.  
   - **Sector Handling**  
     - If line is `DTL`, cursor over TAR sectors; otherwise cursor over power sectors.  
     - For each sector, populate `#TmpRGSSectors` with OCC authorization data for the operation and access dates.  
     - Determine if TOA is authorised, if power is off, and if a circuit break occurred, setting corresponding times.  
   - **Remarks & Colour** – Build remarks string from AR remark, TVF mode, and TVF stations.  
   - **Access Type Logic** –  
     - If `AccessType` is `Possession`, set colour to possession background, adjust possession counter, and enable grant TOA.  
     - Otherwise set colour to protection background and decide grant TOA enable based on status and possession counter.  
   - **Insert into `#TmpRGS`** – Store all computed fields for the current record.  
6. **Close Cursors** – Release main and sector cursors.  
7. **Return Results**  
   - Select all rows from `#TmpRGS` ordered by line number.  
   - Select cancel list rows from `TAMS_TAR` and `TAMS_TOA` where `TOAStatus` is not 0, 5, or 6.  
   - Return operation and access dates.  
8. **Cleanup** – Drop temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Sector`  
  - `TAMS_OCC_Auth`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_Power_Sector`  

* **Writes:**  
  - None to permanent tables (only temporary tables `#TmpRGS` and `#TmpRGSSectors` are created and dropped).