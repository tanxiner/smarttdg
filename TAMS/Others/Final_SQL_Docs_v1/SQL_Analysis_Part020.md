# Procedure: sp_TAMS_Depot_Approval_OnLoad
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data related to a depot approval, including access requirements, possession details, and workflow information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Depot ID |

### Logic Flow
1. The procedure starts by selecting relevant data from the TAMS_TAR table based on the provided depot ID.
2. It then retrieves additional information, including possession details and workflow data.
3. The procedure checks for sector conflicts and inserts any conflicting sectors into a temporary table.
4. It processes the temporary table to identify any exceptions that need to be addressed during the approval process.
5. Based on the access type, it selects the relevant access requirements from the TAMS_Access_Requirement table.
6. Finally, it returns the processed data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Possession, TAMS_Type_Of_Work, TAMS_Access_Requirement, TAMS_User, TAMS_Sector, TAMS_TAR_Sector, TAMS_Power_Sector, TAMS_SPKSZone, TAMS_TAR_Workflow
* **Writes:** #TmpExc, #TmpExcSector