# Procedure: SP_TAMS_Depot_GetDTCAuth

The purpose of this stored procedure is to retrieve a list of depot authentication details for a given access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The access date for which the depot authentication details are required. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then joins multiple tables, including TAMS_TAR, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Remark, and TAMS_WFStatus, on various conditions based on the provided access date.
3. The procedure filters the results to include only rows where the AccessDate matches the specified @accessDate parameter.
4. Finally, it orders the results by DepotAuthStatusId in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Remark, and TAMS_WFStatus