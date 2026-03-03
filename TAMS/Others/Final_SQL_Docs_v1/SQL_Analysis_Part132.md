# Procedure: sp_TAMS_RGS_OnLoad_20250128
**Type:** Stored Procedure

The procedure performs a series of checks and operations for a specific track type, including possession control, power section management, and TOA (Train Operations Authority) status updates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to check. |
| @TrackType | NVARCHAR(50) | The track type to perform operations on. |

### Logic Flow
1. Checks if the user exists and performs possession control checks.
2. Retrieves relevant parameters from TAMS_Parameters table based on the line and track type.
3. Performs TOA status updates, including checking for grant and protection limit times.
4. Updates TOA records with new information, such as TOANo and InChargeNRIC.
5. Returns a list of TOA records in order by access type and TOA status.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_TAR_Sector
* **Writes:** TAMS_TAR, TAMS_TOA