# Procedure: sp_TAMS_OCC_GetWorkflowByLineAndType

### Purpose
Retrieve the active workflow record(s) for a specified line and workflow type that are currently effective.

### Parameters
| Name   | Type          | Purpose |
| :----- | :------------ | :------ |
| @Line  | NVARCHAR(10)  | Line identifier to filter workflows. |
| @Type  | NVARCHAR(50)  | Workflow type to filter workflows. |

### Logic Flow
1. Begin execution of the procedure.  
2. Query the TAMS_Workflow table selecting columns ID, Line, WorkflowType, InvolvePower.  
3. Apply filters:  
   - Line equals the supplied @Line value.  
   - WorkflowType equals the supplied @Type value.  
   - EffectiveDate is on or before the current date.  
   - ExpiryDate is on or after the current date.  
   - IsActive equals 1.  
4. Order the resulting rows by ID in ascending order.  
5. Return the result set to the caller.

### Data Interactions
* **Reads:** TAMS_Workflow  
* **Writes:** None