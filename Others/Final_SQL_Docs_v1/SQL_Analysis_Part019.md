Here are the documented procedures:

### Procedure: sp_TAMS_Depot_Applicant_List_Child_OnLoad

**Type:** Stored Procedure

**Purpose:** This stored procedure retrieves a list of applicants for a specific sector and track type, filtered by access dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by |
| @TrackType | NVARCHAR(50) | The track type to filter by |
| @ToAccessDate | NVARCHAR(20) | The end access date (inclusive) |
| @FromAccessDate | NVARCHAR(20) | The start access date (inclusive) |
| @TARType | NVARCHAR(20) | The TAR type to filter by |
| @SectorID | INT | The sector ID to filter by |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_WFStatus, TAMS_TAR_Sector
* **Writes:** None

### Procedure: sp_TAMS_Depot_Applicant_List_Master_OnLoad

**Type:** Stored Procedure

**Purpose:** This stored procedure retrieves a list of sectors for a specific line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by |
| @TrackType | NVARCHAR(50) | The track type to filter by |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector
* **Writes:** None