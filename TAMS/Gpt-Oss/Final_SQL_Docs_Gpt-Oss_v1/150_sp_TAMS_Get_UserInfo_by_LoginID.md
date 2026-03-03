# Procedure: sp_TAMS_Get_UserInfo_by_LoginID

### Purpose
Retrieve all columns for a user identified by a specific LoginID.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @LoginID  | NVARCHAR(100) | The LoginID of the user to look up (optional, defaults to NULL). |

### Logic Flow
1. Check if any record exists in TAMS_User where LoginID equals the supplied @LoginID.  
2. If such a record exists, return every column from that record.  
3. If no record exists, the procedure completes without returning data.

### Data Interactions
* **Reads:** TAMS_User  
* **Writes:** None  

---