# Procedure: sp_TAMS_TB_Gen_Report_20231009

This procedure generates a report for TAMS TB data based on specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (e.g., NEL, TAMS_TAR). |
| @TrackType | NVARCHAR(50) | Specifies the track type. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access. |
| @AccessType | NVARCHAR(20) | Specifies the access type (e.g., ''). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table based on the specified parameters.
2. It filters the data to include only records where the AccessDate falls within the specified range (@AccessDateFrom and @AccessDateTo).
3. For NEL lines, it includes records with a TARStatusId of 9; otherwise, it includes records with a TARStatusId of 8.
4. It also filters by access type (if specified) or allows empty strings for this parameter.
5. The procedure then joins the selected data with two additional tables: TAMS_Get_Station and TAMS_Get_ES_NoBufferZone to retrieve related information.
6. Finally, it orders the results by AccessDate and TARNo.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone