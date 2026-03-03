# Procedure: SP_Test

### Purpose
Determines the final QTS status for a specific NRIC by invoking the QTS check procedure twice with different access types and evaluating the returned status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | | The procedure does not accept any parameters. |

### Logic Flow
1. Disable row‑count messages to keep result sets clean.  
2. Declare local variables for the in‑charge name, status, and access type.  
3. Create a temporary table `#tmpnric` with columns for NRIC, name string, line, qualification date, code, and status.  
4. Truncate `#tmpnric` to ensure it starts empty.  
5. Set a hard‑coded qualification date (`2023/08/29`).  
6. Build an execution string for logging purposes (the string is printed but never executed).  
7. Assign `'Protection'` to `@AccessType`.  
8. Execute `sp_TAMS_TOA_QTS_Chk` with NRIC `S8719031E`, the qualification date, line `DTL`, and access type `PC (ML)`, inserting the result into `#tmpnric`.  
9. Retrieve the returned name string and status into `@InChargeName` and `@InChargeStatus`.  
10. Pause execution for 10 seconds.  
11. Initialize `@QTSFinStatus` as an empty string.  
12. If the returned status is `'InValid'`:  
    * If the current access type is `'Protection'`:  
        - Truncate `#tmpnric` and clear the name and status variables.  
        - Build a new execution string for logging (again only printed).  
        - Execute `sp_TAMS_TOA_QTS_Chk` again with the same NRIC, date, and line but with access type `TPO (NT)`, inserting into `#tmpnric`.  
        - Retrieve the new name and status.  
        - If the new status is `'InValid'`, set `@QTSFinStatus` to `'InValid'`; otherwise set it to `'Valid'`.  
    * If the access type is not `'Protection'`, set `@QTSFinStatus` to `'InValid'`.  
13. If the initial status was not `'InValid'`, set `@QTSFinStatus` to `'Valid'`.  
14. Drop the temporary table `#tmpnric`.  
15. Print the final status stored in `@QTSFinStatus`.

### Data Interactions
* **Reads:** None from permanent tables; data is retrieved from the temporary table `#tmpnric` after each call to `sp_TAMS_TOA_QTS_Chk`.  
* **Writes:** Inserts into and truncates the temporary table `#tmpnric`; no permanent tables are modified.