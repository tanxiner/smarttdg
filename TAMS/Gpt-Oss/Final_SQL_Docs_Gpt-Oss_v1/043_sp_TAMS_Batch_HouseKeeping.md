# Procedure: sp_TAMS_Batch_HouseKeeping

### Purpose
Collects and returns a comprehensive set of records from the TAMS system that are relevant to current TAR entries and other housekeeping tables, likely for reporting, archival, or cleanup purposes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | – | – |

### Logic Flow
1. Initializes a variable `@DeAct` to 0.  
2. Retrieves the de‑activation threshold value from `TAMS_Parameters` where the parameter code is `DeActivateAcct` and the current date falls within the parameter’s effective period. The value is stored in `@DeAct`.  
3. (Commented out) An update statement that would set `IsActive` to 0 for users whose last login exceeds the threshold defined by `@DeAct`.  
4. Executes a series of `SELECT *` queries:  
   - For each TAR‑related table (`TAMS_TAR_AccessReq`, `TAMS_TAR_Attachment`, `TAMS_TAR_Attachment_Temp`, `TAMS_TAR_Power_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR_Station`, `TAMS_TAR_TVF`, `TAMS_TAR_Workflow`), it selects rows whose `TARId` matches any existing `ID` in `TAMS_TAR`.  
   - Retrieves all rows from `TAMS_Block_TARDate`.  
   - Retrieves all rows from `TAMS_OCC_Auth`, `TAMS_OCC_Auth_Workflow`, `TAMS_OCC_Duty_Roster`.  
   - Retrieves all rows from all possession‑related tables (`TAMS_Possession`, `TAMS_Possession_Limit`, `TAMS_Possession_OtherProtection`, `TAMS_Possession_PowerSector`, `TAMS_Possession_WorkingLimit`).  
   - Retrieves all rows from `TAMS_TOA`, `TAMS_TOA_Parties`, `TAMS_TVF_Ack_Remark`, `TAMS_TVF_Acknowledge`.  
   - Retrieves all rows from `TAMS_TAR`.  

The procedure performs only read operations; no data is inserted, updated, or deleted.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_TAR_Attachment`  
  - `TAMS_TAR_Attachment_Temp`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_TAR_Sector`  
  - `TAMS_TAR_Station`  
  - `TAMS_TAR_TVF`  
  - `TAMS_TAR_Workflow`  
  - `TAMS_Block_TARDate`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Auth_Workflow`  
  - `TAMS_OCC_Duty_Roster`  
  - `TAMS_Possession`  
  - `TAMS_Possession_Limit`  
  - `TAMS_Possession_OtherProtection`  
  - `TAMS_Possession_PowerSector`  
  - `TAMS_Possession_WorkingLimit`  
  - `TAMS_TOA`  
  - `TAMS_TOA_Parties`  
  - `TAMS_TVF_Ack_Remark`  
  - `TAMS_TVF_Acknowledge`  

* **Writes:** None.