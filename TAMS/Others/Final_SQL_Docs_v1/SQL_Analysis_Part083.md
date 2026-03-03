# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215
**Type:** Stored Procedure

The purpose of this stored procedure is to generate an authorization for a specific line of equipment.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the equipment. |

### Logic Flow
1. Checks if access date is provided, and if not, determines the current day based on the time.
2. Calculates the operation date and access date for the authorization.
3. Retrieves the workflow ID and endorser ID for the specified line.
4. Creates temporary tables to store sector data and OCC authentication details.
5. Iterates through the sector data and updates the OCC authentication table with the necessary information.
6. Inserts the updated OCC authentication details into the TAMS_OCC_Auth table.
7. Inserts the workflow details into the TAMS_OCC_Auth_Workflow table.

### Data Interactions
* **Reads:** [dbo].[TAMS_TAR], [dbo].[TAMS_TAR_Sector], [dbo].[TAMS_Power_Sector], [dbo].[TAMS_Traction_Power], [dbo].[TAMS_Workflow], [dbo].[TAMS_Endorser]
* **Writes:** [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_OCC_Auth_Workflow]