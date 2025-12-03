# Procedure: sp_TAMS_RGS_OnLoad_Enq_20221107

### Purpose
This stored procedure is used to retrieve and process data related to RGS (Remote Ground Station) operations, specifically for possession and non-possession scenarios.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the current time is greater than a specified cutoff time (06:00:00). If true, it sets the operation date and access date accordingly.
2. It then retrieves the TOA callback time, RGS possession background, and RGS protection background from the TAMS_Parameters table based on the line number.
3. The procedure then loops through each TAR record that matches the specified conditions (TOAStatus <> 0) and fetches the corresponding TOA details.
4. For each TAR record, it checks if the sector is a power sector or not. If it's a power sector, it processes the data accordingly. Otherwise, it treats it as a non-power sector scenario.
5. The procedure then inserts the processed data into two temporary tables: #TmpRGS and #TmpRGSSectors.
6. Finally, it retrieves the data from these temporary tables and returns it in a formatted structure.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_Traction_Power_Detail, TAMS_Power_Sector