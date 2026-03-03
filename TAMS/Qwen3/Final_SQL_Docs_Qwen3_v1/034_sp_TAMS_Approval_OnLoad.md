# Procedure: sp_TAMS_Approval_OnLoad

### Purpose
This stored procedure performs a series of checks and operations on a TAMS TAR record, including retrieving relevant data from other tables, performing calculations, and updating records as necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to process. |

### Logic Flow
The procedure follows these steps:

1. Retrieve relevant data from the TAMS_TAR table based on the provided @TARID.
2. Calculate and retrieve additional data from other tables, including TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Possession, and TAMS_Type_Of_Work.
3. Perform calculations to determine if there are any sector conflicts or exceptions that need to be addressed.
4. Update records in the #TmpExc table based on the results of the calculations.
5. Retrieve additional data from the #TmpExc table to identify any sector conflicts or exceptions that require attention.
6. If necessary, update records in the TAMS_TAR_Sector table to resolve sector conflicts.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Possession, TAMS_Type_Of_Work, #TmpExc
* **Writes:** #TmpExc