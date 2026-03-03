# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_PowerOnIssue

### Purpose
This stored procedure generates authorization for TAMS OCC operations based on the provided line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to generate authorization for. |
| @AccessDate | NVARCHAR(20) | The access date to use for generating authorization. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date if the current time is after 6:00 AM, otherwise use the current date minus one day.
3. Calculate the operation date based on the determined dates.
4. Retrieve the workflow ID for the specified line and workflow type (OCCAuth).
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store sector data and OCC authentication details.
7. Insert sector data into the temporary table based on the provided line number.
8. Iterate through the sector data, updating the OCC authentication details in the temporary table if necessary.
9. Insert the updated OCC authentication details into the TAMS_OCC_Auth table.
10. Create a workflow for each OCC authentication detail in the TAMS_OCC_Auth table.

### Data Interactions
* Reads: 
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Traction_Power_Detail
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* Writes:
	+ #TmpTARSectors (temporary table)
	+ #TmpOCCAuth (temporary table)
	+ #TmpOCCAuthWorkflow (temporary table)
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow