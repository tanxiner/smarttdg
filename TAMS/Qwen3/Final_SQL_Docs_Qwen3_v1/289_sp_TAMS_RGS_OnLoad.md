# Procedure: sp_TAMS_RGS_OnLoad

### Purpose
This stored procedure is used to retrieve and process data related to possession, protection, and cancellation of railway goods (RGs) for a specific line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the RG data is being processed. |
| @TrackType | NVARCHAR(50) | The track type (e.g., mainline, NEL) for which the RG data is being processed. |

### Logic Flow
The procedure follows these steps:

1. It determines the current date and time.
2. Based on the current time, it sets the operation date and access date accordingly.
3. It retrieves the possession, protection, and cancellation background values from the TAMS_Parameters table based on the line number and track type.
4. It checks if there are any existing possessions for the specified line and track type. If yes, it sets a flag indicating that there is an existing possession.
5. It processes the data by retrieving additional information such as electrical sections, power off times, circuit break out times, parties involved, work descriptions, contact numbers, and remarks.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_TAR_Power_Sector
* Writes: None