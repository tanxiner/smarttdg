# Procedure: sp_TAMS_TOA_QTS_Chk_20230323_M
**Type:** Stored Procedure

This procedure checks if a user has valid access to a qualification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identity Number of the user. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** #tmpnric, #tmpqtsqc
* **Writes:** #tmpnric, #tmpqtsqc