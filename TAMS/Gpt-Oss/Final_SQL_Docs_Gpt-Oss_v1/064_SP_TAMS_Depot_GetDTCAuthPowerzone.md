# Procedure: SP_TAMS_Depot_GetDTCAuthPowerzone

### Purpose
Retrieve all DTCAuth power zone records for a specified access date, including related power sector, workflow status, and user action details, and order them by authorization and record identifiers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date used to filter depot authorization records by their AccessDate field. |

### Logic Flow
1. Disable row‑count messages to keep the result set clean.  
2. Build a derived table that:
   - Selects every column from the depot authorization table.  
   - Joins the authorization to its power zone, power sector, and workflow status records.  
   - Joins user tables to translate action identifiers into user names for power‑off, rack‑off, power‑on, and rack‑in events.  
   - Filters rows where the authorization’s AccessDate matches the supplied @accessDate and the power sector is active.  
   - Adds a dense rank column (`rowspan`) that groups rows by AuthID.  
3. Return the derived table’s rows, ordering first by AuthID ascending and then by the authorization record ID ascending.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector, TAMS_WFStatus, TAMS_User  
* **Writes:** None