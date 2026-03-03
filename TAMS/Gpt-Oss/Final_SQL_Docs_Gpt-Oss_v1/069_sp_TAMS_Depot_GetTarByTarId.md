# Procedure: sp_TAMS_Depot_GetTarByTarId

### Purpose
Retrieve a TAR record by its ID, including aggregated PowerSector and SPKSZone names and related status information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | Identifier of the TAR to fetch |

### Logic Flow
1. Declare two string variables, @PowerZone and @SPKSZone, and set them to empty.  
2. Build @PowerZone by concatenating the PowerSector values from TAMS_Power_Sector that are active and linked to the given TAR via TAMS_TAR_Power_Sector, excluding buffer sectors. The values are joined with commas and grouped by PowerSector.  
3. Trim any trailing comma and surrounding spaces from @PowerZone.  
4. Build @SPKSZone similarly by concatenating the SPKSZone values from TAMS_SPKSZone that are active and linked to the TAR via TAMS_TAR_SPKSZone, grouped by SPKSZone.  
5. Trim any trailing comma and surrounding spaces from @SPKSZone.  
6. Select the TAR record from TAMS_TAR where Id equals @TarId.  
7. In the SELECT, include all standard TAR columns, replace null AccessTimeSlot with an empty string, and add the computed @SPKSZone and @PowerZone as columns.  
8. Convert WithdrawDate to a string in dd/mm/yyyy format.  
9. Resolve WithdrawBy to the user name from TAMS_User.  
10. Resolve TARStatus to the workflow status text from TAMS_WFStatus that matches the TAR’s status ID, line, and track type, and has WFType='TARWFStatus'.

### Data Interactions
* **Reads:** TAMS_Power_Sector, TAMS_TAR_Power_Sector, TAMS_SPKSZone, TAMS_TAR_SPKSZone, TAMS_TAR, TAMS_User, TAMS_WFStatus  
* **Writes:** None