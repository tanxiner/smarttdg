# Procedure: sp_TAMS_Depot_Form_OnLoad
**Type:** Stored Procedure

The purpose of this stored procedure is to perform a series of checks and calculations for a depot form on-load event.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number being processed. |
| @TrackType | NVARCHAR(50) | The track type being processed. |
| @AccessDate | NVARCHAR(20) | The access date being processed. |
| @AccessType | NVARCHAR(20) | The access type being processed. |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text. |

### Logic Flow
1. Checks if the user exists and retrieves their details.
2. Inserts into the Audit table.
3. Returns the ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role, TAMS_Parameters, TAMS_Sector, TAMS_Power_Sector, TAMS_Track_Power_Sector, TAMS_SPKSZone, TAMS_TAR, TAMS_TAR_Sector.
* **Writes:** Audit table.

### Logic
The procedure performs a series of checks and calculations based on the input parameters. It first retrieves the user details and inserts them into the Audit table. Then it checks if the selected sector is DW only and sets a flag accordingly. It also checks if the power selection text matches certain conditions and updates variables accordingly.

Next, it retrieves the company details for the line number being processed and orders them by ID. It then retrieves the access requirements for the line number and track type, and orders them by ID.

The procedure then checks if the day is a weekend or public holiday, and if so, it retrieves the weekend/PH status from the TAMS_Parameters table. If not, it checks if the sector is DW only and sets a flag accordingly.

Finally, it creates a temporary table to store the power sector details and populates it with data from the TAMS_Power_Sector table. It then selects the power on/off status for each sector based on the input parameters.

The procedure also includes comments that suggest how to execute the stored procedure with different inputs.