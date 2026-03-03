# Procedure: sp_TAMS_TOA_Get_PointNo

### Purpose
Retrieve the protection type and ordered point numbers for a specified TOA record.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TOAID | BIGINT | Identifier of the TOA record to query |

### Logic Flow
1. Query the `TAMS_TOA` table to obtain the `ProtectionType` for the row whose `Id` matches the supplied `@TOAID`.  
2. Query the `TAMS_TOA_PointNo` table to retrieve each point’s `ID` (aliased as `Sno`) and `PointNo` where the `TOAID` equals the supplied `@TOAID`.  
3. Return the point numbers sorted by `ID` in ascending order.

### Data Interactions
* **Reads:** `TAMS_TOA`, `TAMS_TOA_PointNo`  
* **Writes:** None