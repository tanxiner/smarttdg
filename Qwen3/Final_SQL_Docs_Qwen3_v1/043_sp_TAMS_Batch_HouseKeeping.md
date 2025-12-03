# Procedure: sp_TAMS_Batch_HouseKeeping

### Purpose
This stored procedure performs a batch housekeeping operation on various TAMS tables, updating and deleting records as necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Inferred usage |

### Logic Flow
1. The procedure starts by declaring a variable `@DeAct` to store the value of a parameter.
2. It then selects the value of `ParaValue1` from the `TAMS_Parameters` table where `ParaCode` is 'DeActivateAcct' and the current date falls within the specified effective and expiry dates.
3. Based on this value, it updates or deletes records in various TAMS tables, including `TAMS_TAR_AccessReq`, `TAMS_TAR_Attachment`, `TAMS_TAR_Power_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR_Station`, `TAMS_TAR_TVF`, and others.
4. The procedure also selects records from tables like `TAMS_Block_TARDate`, `TAMS_OCC_Auth`, `TAMS_OCC_Auth_Workflow`, `TAMS_OCC_Duty_Roster`, `TAMS_Possession`, `TAMS_Possession_Limit`, `TAMS_Possession_OtherProtection`, `TAMS_Possession_PowerSector`, and `TAMS_Possession_WorkingLimit`.
5. Additionally, it selects records from tables like `TAMS_TOA`, `TAMS_TOA_Parties`, `TAMS_TVF_Ack_Remark`, and `TAMS_TVF_Acknowledge`.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters
	+ TAMS_TAR_AccessReq
	+ TAMS_TAR_Attachment
	+ TAMS_TAR_Power_Sector
	+ TAMS_TAR_Sector
	+ TAMS_TAR_Station
	+ TAMS_TAR_TVF
	+ TAMS_Block_TARDate
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
	+ TAMS_OCC_Duty_Roster
	+ TAMS_Possession
	+ TAMS_Possession_Limit
	+ TAMS_Possession_OtherProtection
	+ TAMS_Possession_PowerSector
	+ TAMS_Possession_WorkingLimit
	+ TAMS_TOA
	+ TAMS_TOA_Parties
	+ TAMS_TVF_Ack_Remark
	+ TAMS_TVF_Acknowledge
* **Writes:** None