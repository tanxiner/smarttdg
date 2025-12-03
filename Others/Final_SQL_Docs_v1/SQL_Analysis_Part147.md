# Procedure: sp_TAMS_SummaryReport_OnLoad_20230713
**Type:** Stored Procedure

The procedure generates a summary report for TAMS (Technical Assistance Management System) based on the provided line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) | Specifies the line number to filter TAR records. |
| @StrAccDate	NVARCHAR(20) | Specifies the access date to filter TAR records. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns a detailed report with various counters and values.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA tables explicitly selected from.
* **Writes:** None.