# Procedure: sp_TAMS_OCC_GetEndorserByWorkflowId

This procedure retrieves a list of endorsers for a specific workflow ID, filtered by level and effective/expiry dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | The ID of the workflow to retrieve endorses for. |

### Logic Flow
1. The procedure starts by selecting columns from the TAMS_Endorser table.
2. It filters the results to only include rows where the WorkflowId matches the input parameter @ID, and the Level is 1.
3. The EffectiveDate must be less than or equal to the current date, and the ExpiryDate must be greater than or equal to the current date.
4. Only active records are included in the results.
5. The results are ordered by ID.

### Data Interactions
* **Reads:** TAMS_Endorser