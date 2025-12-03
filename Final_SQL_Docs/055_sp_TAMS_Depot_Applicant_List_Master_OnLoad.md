# Procedure: sp_TAMS_Depot_Applicant_List_Master_OnLoad

### Purpose
Retrieve a list of active sectors for a specified line and track type, ordered by their defined sequence.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier |
| @TrackType | NVARCHAR(50) | Target track type |
| @ToAccessDate | NVARCHAR(20) | Upper bound for access date (unused in current logic) |
| @FromAccessDate | NVARCHAR(20) | Lower bound for access date (unused in current logic) |
| @TARType | NVARCHAR(20) | TAR type filter (unused in current logic) |

### Logic Flow
1. Capture the current date in `@CurrDate` using the system clock, formatted to `dd/MM/yyyy`.
2. Create a temporary table `#TmpSector` with columns for line, sector ID, sector string, and sector order.
3. Truncate `#TmpSector` to ensure it is empty before use.
4. Insert into `#TmpSector` all rows from `TAMS_Sector` that match the supplied `@Line` and `@TrackType`, are marked active, and whose effective period includes `@CurrDate`. The rows are ordered by the sector order field.
5. Select from `#TmpSector` the distinct combination of line, sector ID, sector string, and sector order, grouping by these columns to eliminate duplicates. The result set is ordered by sector order.
6. Drop the temporary table `#TmpSector` before exiting.

### Data Interactions
* **Reads:** `TAMS_Sector`
* **Writes:** None (only temporary table operations)