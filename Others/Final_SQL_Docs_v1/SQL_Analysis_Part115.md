# Procedure: sp_TAMS_RGS_AckSurrender_20230308
**Type:** Stored Procedure

The purpose of this stored procedure is to acknowledge a surrender for a TAMS (Technical Assistance Management System) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS record being surrendered. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_OCC_Auth