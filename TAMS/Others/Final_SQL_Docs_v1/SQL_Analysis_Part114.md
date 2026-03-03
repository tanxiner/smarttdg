# Procedure: sp_TAMS_RGS_AckSurrender_20230209_AllCancel
**Type:** Stored Procedure

The procedure performs an acknowledgement of a surrender for all types of OCC (Occupancy Control Certificate) transactions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Transaction Area) to be acknowledged. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_User
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow