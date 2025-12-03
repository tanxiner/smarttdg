# Procedure: sp_TAMS_OCC_Generate_Authorization_Trace

### Purpose
This stored procedure generates an authorization trace for a given line of operation, taking into account the access date and effective dates of workflows.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of operation to generate the authorization trace for. |
| @AccessDate | NVARCHAR(20) | The access date to use when generating the authorization trace. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time, as well as a cutoff time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. Otherwise, use the provided access date.
4. Retrieve the workflow ID for the given line of operation that matches the calculated effective dates.
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store sector data and OCC authentication details.
7. Insert sector data into the temporary table based on the line of operation.
8. Iterate through the sector data, updating the OCC authentication details in the temporary table as necessary.
9. Insert the updated OCC authentication details into a final table.
10. Generate an authorization workflow for each OCC authentication detail.
11. Drop the temporary tables.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAR_Sector, TAMS_Traction_Power_Detail, TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: #TmpTARSectors, #TmpOCCAuth, #TmpOCCAuthWorkflow