# Procedure: sp_TAMS_OCC_Generate_Authorization

### Purpose
This stored procedure generates an authorization for a TAMS OCC (Traction and Maintenance Services Operations Center) operation, based on the provided line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the operation. |
| @TrackType | NVARCHAR(50) | The type of track for the operation. |
| @AccessDate | NVARCHAR(20) | The access date for the operation. |

### Logic Flow
1. The procedure first determines the current date and time, as well as a cutoff time.
2. If no access date is provided, it calculates the previous day's date based on the current date and time.
3. It then checks if there are any existing authorizations for the specified line and track type on the calculated date. If not, it proceeds to generate a new authorization.
4. The procedure creates temporary tables to store sector data and OCC authentication details.
5. It populates these tables with relevant data from the main database.
6. It then iterates through each sector in the temporary table, checking if there is an existing authorization for that sector on the specified date.
7. If no authorization exists, it generates a new one by inserting into the #TmpOCCAuth table and updating the corresponding sector details.
8. The procedure also inserts into the TAMS_OCC_Auth table with the generated authorization details.
9. It then creates a workflow for the newly generated authorization and inserts into the TAMS_OCC_Auth_Workflow table.
10. Finally, it inserts into the TAMS_OCC_Auth_Audit and TAMS_OCC_Auth_Workflow_Audit tables to track changes.

### Data Interactions
* **Reads:** 
	+ [dbo].[TAMS_Traction_Power]
	+ [dbo].[TAMS_TAR]
	+ [dbo].[TAMS_TAR_Sector]
	+ [dbo].[TAMS_Power_Sector]
	+ [dbo].[TAMS_Endorser]
	+ [dbo].[TAMS_Workflow]
* **Writes:** 
	+ #TmpOCCAuth
	+ #TmpTARSectors
	+ #TmpOCCAuthWorkflow