# Procedure: sp_TAMS_OCC_RejectTVFAckByParameters_PFR

### Purpose
This stored procedure performs a rejection of TVF acknowledgement by parameters, updating the TAMS_TVF_Acknowledge table and creating an audit record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The ID of the user performing the action. |
| @StationId | int | The ID of the station. |
| @TVFMode | varchar(10) | The mode of TVF. |
| @TVFDirection1 | bit | The direction of TVF 1. |
| @TVFDirection2 | bit | The direction of TVF 2. |

### Logic Flow
The procedure starts by beginning a transaction. It then updates the TAMS_TVF_Acknowledge table with the provided parameters, setting the TVF mode and directions, and marking it as unverified. After updating the table, an audit record is created in the TAMS_TVF_Acknowledge_Audit table for each affected row, including the user ID, current date and time, action type, and other relevant details.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge