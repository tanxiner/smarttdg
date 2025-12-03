# Procedure: sp_TAMS_Depot_SectorBooking_OnLoad
**Type:** Stored Procedure

Purpose: This stored procedure loads data from various tables into a temporary table, performs calculations and updates based on the loaded data, and then returns the updated data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter data by. |
| @TrackType | NVARCHAR(50) | The track type to filter data by. |
| @AccessDate | NVARCHAR(20) | The access date to filter data by. |
| @TARType | NVARCHAR(20) | The TAR type to filter data by. |
| @AccessType | NVARCHAR(20) | The access type to filter data by. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_TAR, TAMS_Access_Requirement
* **Writes:** #ListES (temporary table)

---

# Procedure: sp_TAMS_Depot_SectorBooking_QTS_Chk
**Type:** Stored Procedure

Purpose: This stored procedure checks if a QTS record exists for a given NRIC and qualification date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The NRIC to filter data by. |
| @qualdate | NVARCHAR(MAX) | The qualification date to filter data by. |
| @line | NVARCHAR(MAX) | The line number to filter data by. |
| @TrackType | NVARCHAR(50) | The track type to filter data by. |

### Logic Flow
1. Retrieves NRIC and qualification date from input parameters.
2. Checks if a QTS record exists for the given NRIC and qualification date.
3. If no record exists, updates the NRIC with an invalid status.
4. If a record exists, checks if suspension information is available.
5. If suspension information is not available, updates the NRIC with a valid status.
6. If suspension information is available, checks if the qualification date falls within the valid access period.
7. If the qualification date does not fall within the valid access period, updates the NRIC with an invalid status.

### Data Interactions
* **Reads:** QTS_Personnel_Qualification, QTS_Qualification, QTS_Personnel
* **Writes:** #tmpnric (temporary table), #tmpqtsqc (temporary table)