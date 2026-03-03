# Procedure: sp_TAMS_OCC_InsertToOCCAuthWorkflowTable

This procedure inserts data into the TAMS_OCC_Auth_Workflow table from a temporary storage location.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth_Workflow | [dbo].[TAMS_OCC_Auth_Workflow] READONLY | Temporary storage location for data to be inserted |

### Logic Flow
1. The procedure takes a temporary storage location, @TAMS_OCC_Auth_Workflow, which contains data to be inserted into the TAMS_OCC_Auth_Workflow table.
2. The procedure selects all columns from this temporary storage location and inserts them into the TAMS_OCC_Auth_Workflow table.

### Data Interactions
* **Reads:** TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_OCC_Auth_Workflow