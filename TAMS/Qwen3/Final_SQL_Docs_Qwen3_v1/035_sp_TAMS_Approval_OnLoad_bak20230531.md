# Procedure: sp_TAMS_Approval_OnLoad_bak20230531

### Purpose
This stored procedure performs a series of checks and operations on a TAMS TAR record, including validation, data extraction, and approval processes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to process. |

### Logic Flow
The procedure follows these steps:

1. Retrieves relevant data from the TAMS_TAR table based on the provided TARID.
2. Extracts sector information and checks for sector conflicts.
3. Iterates through a list of sectors, checking if each sector is in conflict with another sector.
4. For each sector, it checks if there are any existing exceptions or conflicts that need to be addressed.
5. If a conflict is found, the procedure inserts an exception record into the #TmpExc table.
6. After processing all sectors, the procedure retrieves additional data from related tables (e.g., TAMS_TAR_Attachment, TAMS_Possession).
7. It then iterates through a list of workflow records associated with the TARID and checks for pending or approved workflows.
8. For each workflow record, it checks if there are any exceptions or conflicts that need to be addressed.
9. If an exception is found, the procedure inserts an exception record into the #TmpExc table.
10. Finally, the procedure retrieves a list of access requirements for the TARID and displays them.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Attachment, TAMS_Possession, TAMS_Type_Of_Work, TAMS_Access_Requirement, TAMS_Endorser, TAMS_User.
* **Writes:** #TmpExc, #TmpExcSector.