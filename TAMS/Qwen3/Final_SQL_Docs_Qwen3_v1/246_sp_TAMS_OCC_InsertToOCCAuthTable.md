# Procedure: sp_TAMS_OCC_InsertToOCCAuthTable

### Purpose
This stored procedure inserts data from a temporary table (@TAMS_OCC_Auth) into the TAMS_OCC_Auth table, effectively updating or adding new records to the OCCAuthStatusId column.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth | [dbo].[TAMS_OCC_Auth] READONLY | A temporary table containing data to be inserted into TAMS_OCC_Auth. |

### Logic Flow
1. The procedure selects all columns from the @TAMS_OCC_Auth table.
2. It then inserts these selected values into the TAMS_OCC_Auth table.

### Data Interactions
* **Reads:** TAMS_OCC_Auth, @TAMS_OCC_Auth
* **Writes:** TAMS_OCC_Auth