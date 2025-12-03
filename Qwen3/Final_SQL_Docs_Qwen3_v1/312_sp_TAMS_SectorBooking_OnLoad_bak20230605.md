# Procedure: sp_TAMS_SectorBooking_OnLoad_bak20230605

### Purpose
This stored procedure loads sector booking data for TAMS (Track and Manage Systems) based on the provided line, access date, TAR type, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(10) | The line number to load sector booking data for. |
| @AccessDate	| NVARCHAR(20) | The access date to filter sector booking data by. |
| @TARType	| NVARCHAR(20) | The TAR type to filter sector booking data by. |
| @AccessType	| NVARCHAR(20) | The access type to filter sector booking data by. |

### Logic Flow
1. The procedure starts by creating a temporary table #ListES to store the loaded sector booking data.
2. It truncates the existing data in #ListES and declares several cursor variables to iterate through the sector booking data.
3. Based on the provided line, it inserts data into #ListES from TAMS_Sector table if the line is 'DTL'. If the line is 'NEL', it inserts data into #ListES from TAMS_Sector table based on specific conditions.
4. It opens a cursor to iterate through the sector booking data for the specified line and access date.
5. For each iteration, it updates the EntryStation and ColorCode columns in #ListES based on the corresponding TAR type and access type.
6. If the access type is 'Protection', it filters the sector booking data further based on specific conditions.
7. Finally, it selects the loaded sector booking data from #ListES and returns the results.

### Data Interactions
* **Reads:** TAMS_Sector table
* **Writes:** TAMS_Sector table