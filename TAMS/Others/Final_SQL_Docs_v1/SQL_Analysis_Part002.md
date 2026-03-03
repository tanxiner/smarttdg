# Procedure: SMSEAlertQ_EnQueue
**Type:** Stored Procedure

Purpose: This stored procedure enqueues a new SMS alert by inserting it into the SMSEAlertQ table and then processing its recipients.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's name. |
| @Subject | nvarchar(500) | The subject of the SMS alert. |
| @Sys | nvarchar(100) | The system that sent the SMS alert. |
| @Greetings | ntext | The greeting message for the SMS alert. |
| @AlertMsg | ntext | The main message for the SMS alert. |
| @UserId | nvarchar(50) | The ID of the user who sent the SMS alert. |
| @SendTo | ntext | The recipient's email address. |
| @CC | ntext | The CC recipient's email address. |
| @BCC | ntext | The BCC recipient's email address. |
| @Separator | nvarchar(1) | The separator used to split the recipients' email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly inserted SMS alert. |
| @From | nvarchar(250) = null | The sender's name (optional). |

Logic Flow:
1. Checks if the recipient is not null.
2. Inserts a new record into the SMSEAlertQ table with the provided details.
3. Retrieves the ntext pointer for the recipient's email address.
4. Loops through each recipient's email address, splitting it into individual addresses using the separator.
5. For each recipient, inserts a new record into the SMSEAlertQTo table and updates the corresponding record in the SMSEAlertQ table.
6. Drops the temporary table used to store the recipients' email addresses.

Data Interactions:
* Reads: SMSEAlertQ, EALERTQTO
* Writes: SMSEAlertQ, EALERTQTO

---

# Procedure: SMTP_GET_Email_Attachments
**Type:** Stored Procedure

Purpose: This stored procedure retrieves the attachments for a specific SMS alert.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AlertID | int | The ID of the SMS alert. |

Logic Flow:
1. Retrieves the attachments for the specified SMS alert from the EAlertQAtt table.
2. Returns the file paths of the attachments.

Data Interactions:
* Reads: EAlertQAtt

---

# Procedure: SMTP_GET_Email_Lists
**Type:** Stored Procedure

Purpose: This stored procedure generates an email list for a specific SMS alert.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None |  |  |

Logic Flow:
1. Deletes any existing records in the EAlertQCC, EAlertQTo, and SMSEAlertQBCC tables that have no corresponding record in the EAlertQ table.
2. Retrieves the recipients' email addresses for each SMS alert from the EALERTQTO table.
3. Loops through each recipient's email address, splitting it into individual addresses using the separator.
4. For each recipient, inserts a new record into the EAlertQCC, EAlertQTo, and SMSEAlertQBCC tables.
5. Updates the status of the SMS alert to 'S' in the SMSEAlertQ table.
6. Returns the email list for the specified SMS alert.

Data Interactions:
* Reads: EALERTQTO
* Writes: EAlertQCC, EAlertQTo, SMSEAlertQBCC

---

# Procedure: SMTP_GET_Email_Lists_Frm
**Type:** Stored Procedure

Purpose: This stored procedure generates an email list for a specific SMS alert.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None |  |  |

Logic Flow:
1. Deletes any existing records in the EAlertQCC, EAlertQTo, and SMSEAlertQBCC tables that have no corresponding record in the EAlertQ table.
2. Retrieves the recipients' email addresses for each SMS alert from the EALERTQTO table.
3. Loops through each recipient's email address, splitting it into individual addresses using the separator.
4. For each recipient, inserts a new record into the EAlertQCC, EAlertQTo, and SMSEAlertQBCC tables.
5. Updates the status of the SMS alert to 'S' in the SMSEAlertQ table.
6. Returns the email list for the specified SMS alert.

Data Interactions:
* Reads: EALERTQTO
* Writes: EAlertQCC, EAlertQTo, SMSEAlertQBCC

---

# Procedure: SMTP_Update_Email_Lists
**Type:** Stored Procedure

Purpose: This stored procedure updates the status of a specific SMS alert and its corresponding records in the EAlertQCC, EAlertQTo, and SMSEAlertQBCC tables.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_AlertID | int | The ID of the SMS alert. |
| @p_SysID | varchar(50) | The system that updated the SMS alert. |
| @p_Status | varchar(1) | The new status for the SMS alert. |
| @p_ErrorMsg | varchar(255) output | The error message (optional). |

Logic Flow:
1. Updates the status of the specified SMS alert in the SMSEAlertQ table.
2. Retrieves the recipients' email addresses for each SMS alert from the EALERTQTO table.
3. Loops through each recipient's email address, updating its corresponding record in the EAlertQCC and SMSEAlertQBCC tables.

Data Interactions:
* Reads: EALERTQTO
* Writes: EAlertQCC, SMSEAlertQBCC

---

# Procedure: SP_Call_SMTP_Send_SMSAlert
**Type:** Stored Procedure

Purpose: This stored procedure sends an SMS alert using SMTP.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Message | AS NVARCHAR(500) = NULL OUTPUT | The message to be sent as the SMS alert. |

Logic Flow:
1. Checks if a transaction is already in progress.
2. If not, starts a new transaction.
3. Retrieves the SMS alerts from the SMSEAlertQ table that have a status of 'Q'.
4. Loops through each SMS alert, splitting its recipients' email addresses into individual addresses using the separator.
5. For each recipient, sends an SMS alert using the SMTP_SMS_NetPage stored procedure.
6. Updates the status of the SMS alert to 'S' in the SMSEAlertQ table.
7. If an error occurs during the process, returns the error message.

Data Interactions:
* Reads: SMSEAlertQ
* Writes: None

---

# Procedure: SP_SMTP_SMS_NetPage
**Type:** Stored Procedure

Purpose: This stored procedure sends an SMS alert using SMTP.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From | nvarchar(250) = null | The sender's name (optional). |
| @To | ntext | The recipient's email address. |
| @Alertmsg | ntext | The main message for the SMS alert. |
| @Alertid | int | The ID of the SMS alert. |
| @Sysname | varchar(50) | The system that sent the SMS alert. |

Logic Flow:
1. Sends an SMS alert using SMTP.
2. Returns the success or failure status.

Data Interactions:
* Reads: None
* Writes: None