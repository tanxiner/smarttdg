# Procedure: sp_TAMS_Approval_Get_Add_BufferZone

### Purpose
Retrieve all sectors marked as buffer zones for a specified TAR.

### Parameters
| Name   | Type   | Purpose                     |
| :----- | :----- | :-------------------------- |
| @TARID | BIGINT | Identifier of the TAR record |

### Logic Flow
1. Accept a TAR identifier via @TARID.  
2. Join the sector master table with the TAR‑sector mapping table on sector ID.  
3. Filter the joined rows to those where the mapping’s TARId equals the supplied @TARID and the mapping’s IsBuffer flag is set to 1.  
4. Return each matching sector’s name and ID, ordering the results by sector ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector  
* **Writes:** None