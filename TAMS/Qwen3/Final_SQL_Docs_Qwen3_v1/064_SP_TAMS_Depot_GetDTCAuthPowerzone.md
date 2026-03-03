# Procedure: SP_TAMS_Depot_GetDTCAuthPowerzone

The purpose of this stored procedure is to retrieve a list of depot authentication power zones, filtered by access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date for which to filter the results |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects all columns from a subquery that filters data from several tables based on the provided access date and active status in the TAMS_Power_Sector table.
3. The subquery joins multiple tables, including TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector, TAMS_WFStatus, and TAMS_User, to retrieve various authentication power zone details.
4. The results are ordered by AuthID and ID in ascending order.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector, TAMS_WFStatus, TAMS_User