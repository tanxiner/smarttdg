# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters_Preview

### Purpose
This stored procedure retrieves a preview of TVF acknowledge data for a specified operation date, line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID (not used in this procedure) |

### Logic Flow
1. The procedure starts by checking if the input parameter `@Line` is 'DTL'. If it is, it proceeds with the logic.
2. It then retrieves the count of TVF acknowledge records for the specified operation date using a SELECT statement.
3. If there are any records found, it inserts data into temporary tables to store station information and TVF acknowledge details.
4. The procedure then joins the TAMS_TVF_Acknowledge table with the #TMP_Station temporary table on the StationId column and filters for records where OperationDate equals @OperationDate and AccessDate equals @AccessDate.
5. It selects specific columns from this joined table, including SNO, ID, AccessDate, OperationDate, StationId, StationName, TVFDirection1, TVFDirection2, TVFMode, AcknowledgedBy, AcknowledgedOn, TVFOnTime, OperatedBy, VerifiedBy, and VerifiedOn.
6. The selected data is then inserted into the #TMP_OCCTVF_Ack temporary table in order of StationId ASC.
7. Finally, the procedure drops the temporary tables.

### Data Interactions
* **Reads:** [TAMS_TVF_Acknowledge], [TAMS_Station]
* **Writes:** #TMP_Station, #TMP_OCCTVF_Ack