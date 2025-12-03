# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_M

### Purpose
This stored procedure generates authorization for TAMS OCC operations based on the provided line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to generate authorization for. |
| @AccessDate | NVARCHAR(20) | The access date to use for generating authorization. |

### Logic Flow
1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. If an access date is provided, use it; otherwise, use the calculated previous day's date.
4. Retrieve the workflow ID for the specified line and workflow type (OCCAuth).
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store TARSectors and OCCAuth data.
7. Iterate through the TAMS_Traction_Power table, updating the IsBuffer and PowerOn columns in #TmpOCCAuth based on the presence of matching TARSectors.
8. Insert new records into #TmpOCCAuth if necessary.
9. Retrieve existing records from TAMS_OCC_Auth that match the line, access date, and operation date.
10. If no matches are found, insert a new record into #TmpOCCAuthWorkflow for each matching record in TAMS_OCC_Auth.

### Data Interactions
* **Reads:** 
	+ TAMS_Traction_Power
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_OCC_Auth
	+ TAMS_OCC_AuthWorkflow
* **Writes:** 
	+ #TmpOCCAuth
	+ #TmpTARSectors