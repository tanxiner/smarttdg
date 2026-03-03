# Procedure: SMTP_GET_Email_Lists_Frm

### Purpose
Retrieve all queued email alert details, including primary, CC, and BCC recipients, for sending via SMTP.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| | | |

### Logic Flow
1. Set transaction isolation level to SERIALIZABLE to prevent concurrent modifications while reading alert data.  
2. Build a derived table `X` that aggregates active, non‑empty recipients from `EALERTQTO` for each distinct `ALERTID`.  
3. Join `EALERTQ` (`A`) with this derived table on `ALERTID`.  
4. Filter rows where `A.status` equals `'Q'` (queued) and `A.Active` is `1`.  
5. For each matching alert, call `[dbo].[SMTP_GET_EMAIL_CC_LISTS]` and `[dbo].[SMTP_GET_EMAIL_BCC_LISTS]` with `A.ALERTID` to obtain comma‑separated CC and BCC recipient lists.  
6. Select the alert greeting, subject, message, sender, alert ID, system flag, the aggregated primary recipient list (`X.RECIPIENT`), and the `from` field.  
7. Order the result set by `A.ALERTID`.

### Data Interactions
* **Reads:** `EALERTQ`, `EALERTQTO`, `[dbo].[SMTP_GET_EMAIL_CC_LISTS]`, `[dbo].[SMTP_GET_EMAIL_BCC_LISTS]`  
* **Writes:** None