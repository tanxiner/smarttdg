# Procedure: sp_TAMS_Depot_RGS_OnLoad

### Purpose
This stored procedure performs a series of operations to retrieve and process data for Depot RGS (Railway Group Standard) on-load events.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |
| @TrackType | NVARCHAR(50) | The track type used to filter the data. |
| @accessDate | DATETIME | The access date used to filter the data. |

### Logic Flow
The procedure starts by declaring several variables and setting their initial values. It then retrieves the necessary parameters from the TAMS_Parameters table based on the provided line number.

Next, it calculates the operation date and cutoff time for the current day. It then selects the required data from various tables, including TAMS_TAR, TAMS_TOA, and TAMS_Depot_Auth, using a series of joins and subqueries.

The procedure then applies several conditions to filter the data, such as checking if the TOA status is not equal to 0, 5, or 6. It also orders the results by access type, TAR number, and ID.

Finally, it returns the processed data in a specific format, including the operation date, access date, and various other fields.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_Parameters