# Procedure: SMTP_GET_Email_Lists_Frm

### Purpose
This procedure retrieves email lists for sending alerts using SMTP, filtering active and queued alerts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Retrieves the ALERTID parameter. |

### Logic Flow
1. The procedure starts by setting the transaction isolation level to SERIALIZABLE.
2. It then selects data from several tables, including EALERTQ and EALERTQTO, based on specific conditions (status='Q' and Active=1).
3. For each ALERTID in the selected data, it retrieves the corresponding RECIPIENT list by joining EALERTQTO with a subquery that filters out inactive recipients.
4. The procedure then selects additional data from EALERTQ for each ALERTID, including GREETINGS, SUBJECT, AlertMsg, SENDER, and FROM fields.
5. Finally, it orders the results by ALERTID.

### Data Interactions
* **Reads:** EALERTQ, EALERTQTO