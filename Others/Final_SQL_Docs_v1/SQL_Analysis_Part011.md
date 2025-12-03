# Procedure: sp_TAMS_Approval_OnLoad
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data related to a specific TAR (Test And Measurement System) record, including its status, access type, and sector information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be processed. |
| @LogInUser | NVARCHAR(20) | The login ID of the user performing the operation. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Type_Of_Work, TAMS_Possession, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User.
* **Writes:** Audit table.

### Logic
The procedure starts by selecting relevant data from various tables based on the TAR ID provided. It then processes this data to identify any sector conflicts and updates the #TmpExc table accordingly.

1. The procedure first checks if there are any sector conflicts for the given TAR record. If a conflict is found, it inserts the conflicting sector information into the #TmpExcSector table.
2. Next, it retrieves the TAR record's access type and exclusive status.
3. It then iterates through the #TmpExcSector table to identify any sectors that have been marked as exclusive but are not actually part of the TAR record. If such a sector is found, it inserts the sector information into the #TmpExc table.
4. The procedure then checks if there are any additional requirements for the current level endorser and updates the TAR record accordingly.

The final step is to update the TAR record with the processed data and return its ID.