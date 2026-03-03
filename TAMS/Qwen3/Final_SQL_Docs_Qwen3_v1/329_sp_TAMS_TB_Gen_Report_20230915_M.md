# Procedure: sp_TAMS_TB_Gen_Report_20230915_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and line type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (DTL or NEL). |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by (optional). |

### Logic Flow
1. The procedure checks if the `@Line` parameter is 'DTL'. If true, it proceeds with the DTL logic.
2. For DTL logic:
	* It selects data from the `TAMS_TAR` table where the access date falls within the specified range and matches the line type (`@Line`) and track type (`@TrackType`).
	* The selected columns include TAR ID, Company/Dept, Access Type, Name, Access Stations, TAR Date, Electrical Section, Nature of Work, and Remarks.
3. If the `@Line` parameter is not 'DTL', it proceeds with the NEL logic.
4. For NEL logic:
	* It selects data from the `TAMS_TAR` table where the access date falls within the specified range and matches the line type (`@Line`) and track type (`@TrackType`).
	* The selected columns include TAR ID, Company/Dept, Access Type, Name, Access Stations, TAR Date, Track Sector, Nature of Work, and Remarks.
5. In both cases, the data is ordered by TAR date and TAR ID.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No writes are performed in this procedure.