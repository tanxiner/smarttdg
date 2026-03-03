# Procedure: sp_TAMS_RGS_OnLoad_AckSMS

### Purpose
Retrieve acknowledgment times and related identifiers for a specific TAR record.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TARID | BIGINT | Identifier of the TAR record to query |

### Logic Flow
1. Accept the TARID parameter, defaulting to 0 if not supplied.  
2. Perform an inner join between TAMS_TOA (alias a) and TAMS_TAR (alias b) on the TARId field.  
3. Filter the joined rows to those where a.TARId equals the supplied @TARID.  
4. For each matching row, select:  
   - b.AccessType  
   - a.AckGrantTOATime formatted as “dd/mm/yyyy hh:mm:ss”; if null, return “00:00:00”.  
   - a.AckProtectionLimitTime formatted similarly; if null, return “00:00:00”.  
   - b.TARNo  
   - a.TOANo  
5. Return the resulting set to the caller.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR  
* **Writes:** None