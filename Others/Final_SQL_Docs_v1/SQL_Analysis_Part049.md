# Procedure: sp_TAMS_Form_Submit_20250313
**Type:** Stored Procedure

The purpose of this stored procedure is to submit a new TAMS (Track Access Management System) form and update the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number associated with the form submission |
| @TrackType | NVARCHAR(50) | The track type associated with the form submission |
| @AccessDate | NVARCHAR(20) | The access date associated with the form submission |
| @AccessType | NVARCHAR(20) | The access type associated with the form submission |
| @TARType | NVARCHAR(10) | The type of TAMS form being submitted (e.g. Urgent, Non-Urgent) |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

4. Retrieves sector information from TAMS_Sector table based on the provided sectors and track type.
5. Inserts into TAMS_TAR_Sector table with the retrieved sector information.
6. Retrieves station information from TAMS_Station table based on the retrieved sector information.
7. Inserts into TAMS_TAR_Station table with the retrieved station information.
8. Determines if a buffer zone is required based on the access type and power selection.
9. If a buffer zone is required, inserts into TAMS_TAR_Sector table with additional information.
10. Updates Colour Code of non-buffer zone sectors.
11. Retrieves workflow ID from TAMS_Workflow table based on the provided TARType and other conditions.
12. Inserts into TAMS_TAR_Workflow table with the retrieved workflow ID.
13. Generates a reference number for the submitted form using sp_Generate_Ref_Num stored procedure.
14. Updates relevant records in TAMS_TAR table with the generated reference number.

### Data Interactions
* **Reads:** 
	+ TAMS_Sector
	+ TAMS_Station
	+ TAMS_Workflow
	+ TAMS_Possession
	+ TAMS_User
	+ TAMS_TAR
* **Writes:** 
	+ TAMS_TAR_Sector
	+ TAMS_TAR_Station
	+ TAMS_TAR_Workflow