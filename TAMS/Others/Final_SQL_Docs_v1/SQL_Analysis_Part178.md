# Procedure: sp_TAMS_WithdrawTarByTarID
**Type:** Stored Procedure

The procedure performs a withdrawal operation on a TAMS TAR record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR record to be withdrawn. |
| @UID | integer | The user ID performing the withdrawal. |
| @Remark | nvarchar(1000) | The remark for the withdrawal. |

### Logic Flow
1. Checks if a TAMS TAR record exists with the specified @TarId.
2. Retrieves the corresponding WFStatusId from the TAMS_WFStatus table based on the TAR record's line and WFType.
3. Retrieves the user name associated with the @UID.
4. Updates the TAR record with the new status, remark, and withdrawal information.
5. Inserts a log entry into the TAMS_Action_Log table to track the withdrawal action.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** TAMS_TAR