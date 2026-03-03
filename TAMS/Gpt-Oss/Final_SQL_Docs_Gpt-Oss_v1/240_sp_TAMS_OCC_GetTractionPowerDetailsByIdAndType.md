# Procedure: sp_TAMS_OCC_GetTractionPowerDetailsByIdAndType

### Purpose
Retrieve active traction power details for a specific ID where the type is 'Sector'.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | int | Identifier of the traction power record to filter on |

### Logic Flow
1. Accept an integer @ID (default 0).  
2. Query the table `TAMS_Traction_Power_Detail`.  
3. Filter rows where `TractionPowerId` equals the supplied @ID.  
4. Further restrict to rows whose `TractionPowerType` equals the literal string 'Sector'.  
5. Ensure only rows marked active (`IsActive = 1`) are considered.  
6. Return the columns `ID`, `TractionPowerId`, `TractionPowerType`, `StationId`, `SectorId`, and `PowerSectionId`.  
7. Order the result set by `ID` in ascending order.

### Data Interactions
* **Reads:** TAMS_Traction_Power_Detail  
* **Writes:** None