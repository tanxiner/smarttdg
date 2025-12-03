# Procedure: sp_TAMS_Email_Urgent_TAR_OCC
**Type:** Stored Procedure

This procedure sends an urgent email to a user with TAR status information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR record. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Parameters
* **Writes:** TAMS_TAR, TAMS_TAR_Attachment_Temp