# Procedure: sp_TAMS_Approval_OnLoad_bak20230531
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data for a specific TAR (Technical Approval Request) ID, including its associated sectors, access types, and workflow information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be processed. |
| @LogInUser | NVARCHAR(20) | The login ID of the user performing the operation. |

### Logic Flow
1. Checks if a user exists with the specified login ID.
2. Retrieves data from TAMS_TAR and TAMS_Sector tables based on the TAR ID, including access dates, types, and sector IDs.
3. Processes sector data to identify sectors that are not gaps (i.e., sectors without gaps) or buffer zones (i.e., sectors with gaps).
4. Iterates through the processed sector data to identify any conflicts between the current TAR's sectors and existing sectors in the system.
5. For each conflict, checks if the current TAR has a higher level of access than the conflicting sector. If so, it inserts an exception record into the #TmpExc table.
6. Retrieves workflow information for the specified TAR ID, including the maximum workflow level, approved workflows, and pending workflows.
7. Iterates through the approved and pending workflows to identify any conflicts with existing sectors or access types.
8. For each conflict, checks if the current TAR has a higher level of access than the conflicting sector. If so, it inserts an exception record into the #TmpExc table.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Type_Of_Work, TAMS_Possession, TAMS_TAR_Workflow
* **Writes:** #TmpExc