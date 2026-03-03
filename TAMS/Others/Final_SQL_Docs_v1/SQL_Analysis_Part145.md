# Procedure: sp_TAMS_SectorBooking_QTS_Chk
**Type:** Stored Procedure

The procedure checks if a user has valid access to a specific sector and qualification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The National Registration Identity Number of the user. |
| @qualdate | NVARCHAR(MAX) | The date of the qualification. |
| @line | NVARCHAR(MAX) | The line number associated with the sector. |
| @TrackType | NVARCHAR(50) | The type of track (e.g., 'Traction Power ON'). |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Personnel, TAMS_Qualification, TAMS_Sector
* **Writes:** Audit table

# Procedure: sp_TAMS_SectorBooking_Special_Rule_Chk
**Type:** Stored Procedure

The procedure checks if a sector has valid access for a specific type of track.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessType | NVARCHAR(20) | The type of access (e.g., 'Possession' or 'Protection'). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(50) | The text associated with the power selection (e.g., 'Traction Power ON'). |

### Logic Flow
1. Checks if access type is valid.
2. Checks if sectors are valid.
3. If access type is 'Possession' and power selection is off, checks for missing combinations.
4. If access type is 'Protection', checks for missing combinations.

### Data Interactions
* **Reads:** TAMS_Special_Sector_Booking, TAMS_Sector
* **Writes:** None

# Procedure: sp_TAMS_SectorBooking_SubSet_Chk
**Type:** Stored Procedure

The procedure checks if two sets of sector IDs are subsets of each other.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @D1SelSec | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @D2SelSec | NVARCHAR(2000) | A comma-separated list of sector IDs. |

### Logic Flow
1. Splits the input strings into lists of sector IDs.
2. Checks if one list is a subset of the other.

### Data Interactions
* **Reads:** None
* **Writes:** None