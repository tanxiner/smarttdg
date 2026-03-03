# Procedure: sp_TAMS_TOA_Update_Details

### Purpose
Updates the MobileNo, TetraRadioNo, and UpdatedOn fields of a TAMS_TOA record identified by TOAID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @MobileNo | NVARCHAR(50) | New mobile number to store (spaces removed) |
| @TetraRadioNo | NVARCHAR(50) | New tetra radio number to store |
| @UserID | NVARCHAR(20) | Identifier of the user performing the update (unused in current logic) |
| @TOAID | BIGINT | Primary key of the TAMS_TOA record to update |
| @Message | NVARCHAR(500) OUTPUT | Status message returned after execution |

### Logic Flow
1. Declare a flag @IntrnlTrans and set it to 0.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set @IntrnlTrans to 1 and start a new transaction.  
3. Execute an UPDATE on TAMS_TOA:  
   - Trim and remove spaces from @MobileNo before assigning to MobileNo.  
   - Assign @TetraRadioNo to TetraRadioNo.  
   - Set UpdatedOn to the current date/time.  
   - Target the row where ID equals @TOAID.  
4. If the UPDATE causes an error (`@@ERROR <> 0`), set @Message to 'ERROR UPDATING TAMS_TOA' and jump to the error handling section.  
5. On normal completion, if an internal transaction was started, commit it. Return @Message.  
6. In the error handling section, if an internal transaction was started, roll it back. Return @Message.

### Data Interactions
* **Reads:** None  
* **Writes:** TAMS_TOA  

---