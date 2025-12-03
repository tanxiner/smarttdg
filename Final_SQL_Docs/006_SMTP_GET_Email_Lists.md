# Procedure: SMTP_GET_Email_Lists

### Purpose
Retrieve all pending email alerts and their associated recipient lists for SMTP dispatch.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | – | – |

### Logic Flow
1. Set transaction isolation level to SERIALIZABLE to ensure consistent reads during the cleanup and selection phases.  
2. Remove any CC, BCC, or TO entries that reference alerts with a missing message (`AlertMsg IS NULL`).  
   - Delete from `EAlertQBCC` where `AlertID` appears in `EAlertQ` with a null `AlertMsg`.  
   - Delete from `EAlertQCC` under the same condition.  
   - Delete from `EAlertQTo` under the same condition.  
3. Delete the alert records themselves from `EAlertQ` where `AlertMsg` is null.  
4. Build a result set of alerts that are queued (`status='Q'`) and active (`Active = 1`).  
   - For each alert, select greeting, subject, message, sender, alert ID, and system flag.  
   - Call helper functions `SMTP_GET_EMAIL_CC_LISTS` and `SMTP_GET_EMAIL_BCC_LISTS` to obtain comma‑separated CC and BCC recipient strings.  
   - Aggregate all active TO recipients from `EALERTQTO` into a single comma‑separated string per alert.  
5. Return the assembled rows ordered by `ALERTID`.

### Data Interactions
* **Reads:** `EAlertQBCC`, `EAlertQCC`, `EAlertQTo`, `EAlertQ`, `EALERTQTO`, `EALERTQ`  
* **Writes:** `EAlertQBCC`, `EAlertQCC`, `EAlertQTo`, `EAlertQ` (deletions only)