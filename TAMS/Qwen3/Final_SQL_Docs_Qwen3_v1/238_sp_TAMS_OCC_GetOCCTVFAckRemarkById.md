# Procedure: sp_TAMS_OCC_GetOCCTVFAckRemarkById

### Purpose
This stored procedure retrieves a specific acknowledgement record for a TVF (Transaction Video Feedback) from the TAMS database, including relevant details such as ID, remark, and creation/update timestamps.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | The ID of the TVF acknowledgement to retrieve |

### Logic Flow
1. The procedure starts by declaring two variables: `@TVFMode` and `@TVFDirection`, which are not used in the provided code snippet.
2. It then selects data from the `TAMS_TVF_Ack_Remark` table, aliasing it as `tvf`, and joins it with the `TAMS_User` table on the `CreatedBy` column.
3. The procedure filters the results to only include records where the `TVFAckId` matches the provided `@ID`.
4. It returns a list of columns including `ID`, `TVFAckId`, `Remark`, `CreatedOn`, `CreatedBy`, `UpdatedOn`, and `UpdatedBy`.

### Data Interactions
* **Reads:** TAMS_TVF_Ack_Remark, TAMS_User