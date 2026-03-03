# Procedure: sp_TAMS_Depot_RGS_OnLoad
**Type:** Stored Procedure

The procedure performs an on-load operation for depot RGS (Railway Group Standard) data, including retrieving and processing various parameters and data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_TAR, TAMS_TOA
* Writes: TAMS_Depot_Auth (Audit table)

# Procedure: sp_TAMS_Depot_RGS_OnLoad_Enq
**Type:** Stored Procedure

The procedure performs an on-load operation for depot RGS data, including retrieving and processing various parameters and data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |
| @TrackType | nvarchar(50) | The track type to process. |
| @accessDate | Date | The access date to process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_TAR, TAMS_TOA
* Writes: TAMS_Depot_Auth (Audit table)