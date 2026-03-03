# Procedure: sp_TAMS_OCC_GetOCCTVFAckRemarkById

### Purpose
Retrieve the remark record and associated user information for a specified TVF Ack ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | Identifier of the TVF Ack whose remark is requested |

### Logic Flow
1. Declare two local variables, @TVFMode and @TVFDirection, but do not use them in the procedure.  
2. Execute a SELECT that pulls the following columns:  
   - The remark record’s ID, TVFAckId, Remark, CreatedOn, UpdatedOn.  
   - The name of the user who created the remark (aliased as CreatedBy).  
   - The name of the user who last updated the remark (aliased as UpdatedBy).  
3. The SELECT joins the TAMS_TVF_Ack_Remark table with the TAMS_User table on the CreatedBy field of the remark record matching the Userid of the user.  
4. The WHERE clause limits the result set to rows where TVFAckId equals the supplied @ID parameter.  
5. Return the resulting single row (or no rows if no match).

### Data Interactions
* **Reads:** TAMS_TVF_Ack_Remark, TAMS_User  
* **Writes:** None