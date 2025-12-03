# Procedure: sp_TAMS_RGS_OnLoad
**Type:** Stored Procedure

The procedure performs a series of checks and operations for a specific track type, including possession, to retrieve relevant data from various tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number being processed. |
| @TrackType | NVARCHAR(50) | The track type being processed (e.g., mainline). |

### Logic Flow
1. Checks if the user exists for the specified line and track type.
2. Retrieves possession control status from the TAMS_TAR table based on the access date, track type, and line number.
3. If possession control is enabled, retrieves additional data such as electrical sections, power off times, circuit break out times, and TOA parties.
4. Iterates through the TOA parties to retrieve relevant information, including TOA status, grant TOA status, and acknowledgement dates.
5. Performs checks on the TOA status to determine if it's a cancelled or granted operation.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_TAR_Power_Sector
* **Writes:** None