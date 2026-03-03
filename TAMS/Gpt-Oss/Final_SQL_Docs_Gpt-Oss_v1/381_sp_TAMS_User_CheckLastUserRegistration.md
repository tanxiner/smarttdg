# Procedure: sp_TAMS_User_CheckLastUserRegistration

### Purpose
Determine whether a user identified by a login ID is allowed to register again based on the time elapsed since their last registration.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @LoginID | NVARCHAR(200) | The login identifier to check for recent registration activity. |

### Logic Flow
1. Verify that @LoginID is not an empty string.  
2. Check if a record with the supplied @LoginID exists in the TAMS_Registration table.  
   - **If it exists**:  
     1. Retrieve the most recent CreatedOn timestamp for that login.  
     2. Retrieve the rate‑limiting threshold (in SECOND) from TAMS_Parameters where ParaCode equals 'Rate Limiting-UserReg'.  
     3. Calculate the difference in SECOND between the current time and the retrieved timestamp.  
     4. If this difference is less than the rate‑limiting threshold, return **-1** (registration not allowed).  
     5. Otherwise, return **1** (registration allowed).  
   - **If it does not exist**: return **1** (registration allowed).  
3. If @LoginID is an empty string, the procedure completes without returning a value.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Parameters  
* **Writes:** None