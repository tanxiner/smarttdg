# Procedure: sp_TAMS_SectorBooking_OnLoad
**Type:** Stored Procedure

The procedure populates a temporary table with sector booking data based on input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @AccessType | NVARCHAR(20) | The access type to filter by. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Station, TAMS_Entry_Station, TAMS_TAR, TAMS_Access_Requirement
* **Writes:** #ListES (temporary table)

The procedure first creates a temporary table to store the sector booking data. It then inserts rows into this table based on the input parameters.

For each row in the temporary table, it retrieves additional information from other tables:
- StationCode and ColourCode from TAMS_Station and TAMS_TAR_Sector.
- AccessType from TAMS_TAR.

Based on the TAR type and access type, it updates the IsEnabled field of the sector booking data. If the TAR type is '2' or '3', and the access type is 'Protection', it sets IsEnabled to 1; otherwise, it sets IsEnabled to 0.

Finally, it returns the populated temporary table with the updated sector booking data.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Station, TAMS_Entry_Station, TAMS_TAR, TAMS_Access_Requirement
* **Writes:** #ListES (temporary table)