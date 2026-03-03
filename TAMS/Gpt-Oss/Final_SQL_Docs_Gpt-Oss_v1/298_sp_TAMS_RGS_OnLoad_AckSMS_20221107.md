# Procedure: sp_TAMS_RGS_OnLoad_AckSMS_20221107

### Purpose
Retrieve acknowledgment times and related identifiers for a specific TAR record.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TARID | BIGINT | Identifier of the TAR to load; defaults to 0 if not supplied |

### Logic Flow
1. Accepts a TAR identifier via @TARID.  
2. Performs a join between TAMS_TOA and TAMS_TAR on the TARId field.  
3. Filters the joined rows to those where the TARId equals the supplied @TARID.  
4. For each matching row, selects the AccessType from TAMS_TAR, the TOANo from TAMS_TOA, and the TARNo from TAMS_TAR.  
5. Formats the AckGrantTOATime and AckProtectionLimitTime from TAMS_TOA into a combined date‑time string; if either value is null, substitutes the string '00:00:00'.  
6. Returns the resulting set of rows to the caller.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR  
* **Writes:** None