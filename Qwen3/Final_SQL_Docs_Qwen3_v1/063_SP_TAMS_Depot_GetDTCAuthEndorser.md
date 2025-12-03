# Procedure: SP_TAMS_Depot_GetDTCAuthEndorser

The purpose of this stored procedure is to retrieve a list of DTCAuth Endorsers for a specific depot, filtered by access date and user role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date range for which to filter the endorser data. |
| @lanid | nvarchar(50) | The login ID of the user to retrieve endorser data for. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then declares a variable `@workflowid` and selects its value from the TAMS_Workflow table, where WorkflowType is 'OCCAuth' and TrackType is 'Depot'.
3. Next, it selects data from the TAMS_Endorser table, joining it with the TAMS_WFStatus table on the WFStatusId column.
4. The procedure filters the endorser data based on the `@accessDate` parameter, selecting only rows where EffectiveDate is greater than or equal to and ExpiryDate is less than or equal to the specified date range.
5. It also filters the data by user role, selecting only rows where the RoleID matches the value in the TAMS_OCC_Duty_Roster table for the specified `@lanid` parameter.
6. The procedure returns a list of DTCAuth Endorsers, including their WorkflowId, Title, RoleId, and Access status.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_OCC_Duty_Roster, TAMS_User