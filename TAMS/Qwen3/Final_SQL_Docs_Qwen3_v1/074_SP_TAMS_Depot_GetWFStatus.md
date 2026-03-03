# Procedure: SP_TAMS_Depot_GetWFStatus

### Purpose
This stored procedure retrieves the workflow status for a specific type of work order ('DTCAuth') from the TAMS_WFStatus table.

### Parameters
| Name | Type | Purpose |
| @ID | int | The ID of the work order to retrieve the workflow status for |

### Logic Flow
1. The procedure sets NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects the ID and WFStatusId columns from the TAMS_WFStatus table where the WFType is 'DTCAuth'.

### Data Interactions
* **Reads:** TAMS_WFStatus