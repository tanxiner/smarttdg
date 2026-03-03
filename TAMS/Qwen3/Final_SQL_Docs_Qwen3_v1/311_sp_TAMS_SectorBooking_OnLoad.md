# Procedure: sp_TAMS_SectorBooking_OnLoad

### Purpose
This stored procedure is used to load sector booking data into a temporary table, which can then be used for further processing or reporting.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track type. |
| @TrackType | NVARCHAR(50) | The track type (e.g., 'DTL', 'NEL'). |
| @AccessDate | NVARCHAR(20) | The access date for the sector booking. |
| @TARType | NVARCHAR(20) | The TAR type (e.g., '2', '3'). |
| @AccessType | NVARCHAR(20) | The access type (e.g., 'Protection', 'Possession'). |

### Logic Flow
The procedure follows these steps:

1. It truncates an existing temporary table (`#ListES`) to ensure it is empty before loading new data.
2. Based on the `@Line` parameter, it determines whether to load data for a 'DTL' or 'NEL' track type.
3. For each line number, it selects relevant sector data from the `TAMS_Sector` table based on the track type and active status.
4. It then iterates through the selected sectors, updating the temporary table with entry station information, color codes, and other relevant details.
5. Depending on the access type, it updates the temporary table to reflect whether a sector is enabled or disabled.
6. Finally, it selects data from the temporary table for both 'DirID' values (1 and 2) and orders the results by `OrderID` and `SectorID`.

### Data Interactions
* Reads: `TAMS_Sector`, `TAMS_Station`, `TAMS_Entry_Station`, `TAMS_TAR`, `TAMS_Access_Requirement`
* Writes: `#ListES`