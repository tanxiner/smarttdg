# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters_bak20230711

The purpose of this stored procedure is to update the OCC Authorisation PFR status for a given set of parameters.

### Parameters

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the operation. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The level of the OCC Authorisation. |
| @Line | nvarchar(10) | The line number for which the update is being performed. |
| @RemarksPFR | nvarchar(100) | The remarks for the PFR status. |
| @SelectionValue | nvarchar(50) | The selected value for the OCC Authorisation level. |
| @StationName | nvarchar(50) | The name of the station associated with the update. |

### Logic Flow

The procedure follows a series of conditional statements based on the value of `@OCCLevel`. For each level, it performs the following steps:

1.  Retrieves the workflow ID and endorser ID from the TAMS_Workflow and TAMS_Endorser tables.
2.  Updates the OCC Authorisation status in the TAMS_OCC_Auth table based on the selected value for `@OCCLevel`.
3.  Inserts a new record into the TAMS_OCC_Auth_Workflow table with the updated status and station ID.
4.  If the update is for level 18, it updates the FISTestResult field in the TAMS_OCC_Auth_Workflow table.

### Data Interactions

*   **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
*   **Writes:** TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow