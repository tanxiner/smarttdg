# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215

### Purpose
This stored procedure generates an authorization for a TAMS OCC (Traction and Maintenance Services Operations Control) operation, based on the provided line number and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAMS OCC operation. |
| @AccessDate | NVARCHAR(20) | The access date for the TAMS OCC operation. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. Calculate the effective date range for the workflow by checking if the current date and time falls within the workflow's effective date range.
4. Retrieve the workflow ID, WFStatusId, and EndorserID from the TAMS_Workflow table.
5. Create temporary tables to store the sector data and OCC authentication details.
6. Insert data into the temporary tables based on the provided line number.
7. Iterate through the sector data and update the OCC authentication details in the temporary tables accordingly.
8. Insert the updated OCC authentication details into the TAMS_OCC_Auth table.
9. Insert the workflow-related data into the TAMS_OCC_Auth_Workflow table.

### Data Interactions
* **Reads:**
	+ TAMS_Workflow
	+ TAMS_Traction_Power
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* **Writes:**
	+ #TmpTARSectors (temporary table)
	+ #TmpOCCAuth (temporary table)
	+ #TmpOCCAuthWorkflow (temporary table)