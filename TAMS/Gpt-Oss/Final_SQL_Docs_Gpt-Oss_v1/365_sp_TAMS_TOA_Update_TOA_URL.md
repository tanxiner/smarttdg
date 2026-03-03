# Procedure: sp_TAMS_TOA_Update_TOA_URL

### Purpose
Insert a new TOA URL record into the TAMS_TOA_URL table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PLine | NVARCHAR(50) | Physical line identifier for the TOA |
| @PLoc | NVARCHAR(50) | Physical location identifier for the TOA |
| @PType | NVARCHAR(50) | Physical type identifier for the TOA |
| @EncPLine | NVARCHAR(100) | Encoded physical line identifier |
| @EncPLoc | NVARCHAR(100) | Encoded physical location identifier |
| @EncPType | NVARCHAR(100) | Encoded physical type identifier |
| @GenURL | NVARCHAR(500) | Generated URL string |
| @Message | NVARCHAR(500) OUTPUT | Error or status message returned to caller |

### Logic Flow
1. Initialize a flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Insert a row into `TAMS_TOA_URL` using the supplied parameters.  
4. If the insert fails (`@@ERROR <> 0`), set `@Message` to `'ERROR UPDATING TAMS_TOA'` and jump to the error handling section.  
5. If the insert succeeds, commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
6. Return the (possibly null) `@Message`.  
7. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_TOA_URL` (INSERT)