# Procedure: sp_TAMS_Batch_DeActivate_UserAccount

### Purpose
Deactivates user accounts that have not logged in for a configurable number of months.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
1. Initialise a variable `@DeAct` to 0.  
2. Retrieve the de‑activation threshold (in months) from `TAMS_Parameters` where `ParaCode` equals `DeActivateAcct` and the current date falls between `EffectiveDate` and `ExpiryDate`. The retrieved value is stored in `@DeAct`.  
3. Update every record in `TAMS_User` whose last login is at least `@DeAct` months ago:  
   - Set `IsActive` to 0.  
   - Record the change by setting `UpdatedBy` to 1 and `UpdatedOn` to the current date/time.  

### Data Interactions
* **Reads:** `TAMS_Parameters`  
* **Writes:** `TAMS_User`