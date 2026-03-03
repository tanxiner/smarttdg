# Procedure: sp_TAMS_TB_Gen_Report

### Purpose
This stored procedure generates a report for TAMS TB data based on specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to filter the report. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter the report. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access data filtering. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access data filtering. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter the report. |

### Logic Flow
1. The procedure checks if the specified line type (@Line) is 'DTL'. If true, it proceeds with the DTL logic.
2. For DTL logic:
	* It selects data from TAMS_TAR table where the access date falls within the specified range (@AccessDateFrom and @AccessDateTo).
	* It filters by TARStatusId based on the line type (@Line) and track type (@TrackType).
	* It also filters by access type (@AccessType) or an empty string if no value is provided.
	* The selected data is ordered by access date and TARNo.
3. If the specified line type (@Line) is not 'DTL', it proceeds with the NEL logic.
4. For NEL logic:
	* It selects data from TAMS_TAR table where the access date falls within the specified range (@AccessDateFrom and @AccessDateTo).
	* It filters by TARStatusId based on the line type (@Line) and track type (@TrackType).
	* It also filters by access type (@AccessType) or an empty string if no value is provided.
	* The selected data is ordered by access date and TARNo.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No writes are performed in this procedure.