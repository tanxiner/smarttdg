# Procedure: SP_TAMS_Depot_GetWFStatus

### Purpose
Retrieve the identifiers and workflow status IDs for all records in the workflow status table that are of type “DTCAuth”.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
1. Disable the automatic return of row‑count messages to avoid interference with the result set.  
2. Execute a SELECT statement that returns the columns `ID` and `WFStatusId` from the table `TAMS_WFStatus` where the column `WFType` equals the literal value `DTCAuth`.

### Data Interactions
* **Reads:** TAMS_WFStatus  
* **Writes:** None