# Procedure: SP_TAMS_Depot_GetDTCAuthSPKS

### Purpose
This stored procedure retrieves data from various tables to provide a comprehensive view of DTCAuth SPK SID information, filtered by access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date for which to retrieve the data |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects data from several tables: TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, Z (TAMS_WFStatus), ProtectOffActionBy (TAMS_User), and ProtectOnActionBy (TAMS_User).
3. The procedure joins these tables based on their respective IDs and filters the results to only include data where the AccessDate matches the specified @accessDate parameter.
4. Finally, it returns the selected data, including AuthID, SPKSID, protect-related fields, StatusID, ProtectOffActionBy and ProtectOnActionBy names, and workflow ID.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, TAMS_WFStatus, TAMS_User (ProtectOffActionBy and ProtectOnActionBy)