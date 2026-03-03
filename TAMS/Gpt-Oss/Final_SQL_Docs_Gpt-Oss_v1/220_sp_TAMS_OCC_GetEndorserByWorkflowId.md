# Procedure: sp_TAMS_OCC_GetEndorserByWorkflowId

### Purpose
Retrieve active level‑1 endorsers for a specified workflow ID that are currently effective.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | Workflow identifier used to filter endorsers |

### Logic Flow
1. Accept the workflow ID in @ID.  
2. Query the TAMS_Endorser table for rows where:  
   - WorkflowId equals @ID,  
   - [Level] equals 1,  
   - EffectiveDate is on or before the current date,  
   - ExpiryDate is on or after the current date,  
   - IsActive equals 1.  
3. Return the columns ID, Line, WorkflowId, [Level], RoleId, Title, RequireValidation, RequireBuffer, RequireTVF, and WFStatusId.  
4. Order the result set by ID.

### Data Interactions
* **Reads:** TAMS_Endorser  
* **Writes:** None