Here are the documented procedures:

### Procedure: SP_CheckPagePermission

**Type:** Stored Procedure

**Purpose**: Checks if a user has permission to access a specific page.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @userid | nvarchar(50) | The ID of the user to check. |
| @menuid | nvarchar(50) | The ID of the menu item to check. |
| @res | bit OUTPUT | The result of the permission check (1 = allowed, 0 = denied). |

**Logic Flow**

1. Checks if the user exists in the TAMS_User table.
2. If the user exists, checks if they have access to the specified menu item in the TAMS_Menu_Role and TAMS_User_Role tables.
3. If access is found, sets @res to 1 (allowed).
4. If no access is found, sets @res to 0 (denied).

**Data Interactions**

* Reads: TAMS_User, TAMS_Menu_Role, TAMS_User_Role
* Writes: None

### Procedure: SP_SMTP_SMS_NetPage

**Type:** Stored Procedure

**Purpose**: Sends an SMS alert using the NetPage system.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From | varchar(100) | The sender's email address. |
| @To | varchar(max) | The recipient's mobile number. |
| @ActualMsg | varchar(max) | The message to send. |
| @AlertiD | int | The ID of the alert. |
| @SysName | varchar(100) | The system name. |

**Logic Flow**

1. Retrieves the current date and time.
2. Deletes any SMS alerts from the SMTP_SMSAlertQ table that are older than 60 days.
3. Inserts a new record into the SMTP_SMSAlertQ table with the sender's email address, recipient's mobile number, message, alert ID, system name, and current date and time.
4. Executes the C:\SMS_NetPage\SMS_NetPage.bat batch file using xp_cmdshell to send the SMS.

**Data Interactions**

* Reads: SMTP_SMSAlertQ
* Writes: SMTP_SMSAlertQ

### Procedure: SP_SMTP_Send_SMSAlert

**Type:** Stored Procedure

**Purpose**: Sends an SMS alert using the SMTP system.

**Parameters**

None

**Logic Flow**

1. Retrieves all alerts from the SMSEAlertQ table that are in status 'Q'.
2. For each alert, retrieves the recipient's mobile number and message.
3. Executes the SP_SMTP_SMS_NetPage stored procedure for each recipient to send an SMS.
4. Updates the alert record in the SMSEAlertQ table with the new status.

**Data Interactions**

* Reads: SMSEAlertQ
* Writes: SMSEAlertQ

### Procedure: SP_TAMS_Depot_GetDTCAuth

**Type:** Stored Procedure

**Purpose**: Retrieves the DTCAuth data for a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date to retrieve. |

**Logic Flow**

1. Retrieves all DTCAuth records from the TAMS_Depot_Auth table that match the specified access date.
2. Joins the retrieved records with other tables (TAMS_TAR, TAMS_Depot_Auth_Workflow, TAMS_WFStatus) to retrieve additional data.
3. Orders the results by DepotAuthStatusId.

**Data Interactions**

* Reads: TAMS_Depot_Auth
* Writes: None

### Procedure: SP_TAMS_Depot_GetDTCAuthEndorser

**Type:** Stored Procedure

**Purpose**: Retrieves the DTCAuth endorser data for a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date to retrieve. |
| @lanid | nvarchar(50) | The language ID. |

**Logic Flow**

1. Retrieves the workflow ID for DTCAuth endorser.
2. Joins the retrieved workflow with other tables (TAMS_Endorser, TAMS_WFStatus) to retrieve additional data.
3. Filters the results by language ID.

**Data Interactions**

* Reads: TAMS_Depot_Auth
* Writes: None

### Procedure: SP_TAMS_Depot_GetDTCAuthPowerzone

**Type:** Stored Procedure

**Purpose**: Retrieves the DTCAuth powerzone data for a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date to retrieve. |

**Logic Flow**

1. Retrieves all DTCAuth records from the TAMS_Depot_Auth table that match the specified access date.
2. Joins the retrieved records with other tables (TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector) to retrieve additional data.

**Data Interactions**

* Reads: TAMS_Depot_Auth
* Writes: None

### Procedure: SP_TAMS_Depot_GetDTCAuthSPKS

**Type:** Stored Procedure

**Purpose**: Retrieves the DTCAuth SPKS data for a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date to retrieve. |

**Logic Flow**

1. Retrieves all DTCAuth records from the TAMS_Depot_Auth table that match the specified access date.
2. Joins the retrieved records with other tables (TAMS_Depot_DTCAuth_SPKS, TAMS_WFStatus) to retrieve additional data.

**Data Interactions**

* Reads: TAMS_Depot_Auth
* Writes: None

### Procedure: SP_TAMS_Depot_GetDTCRoster

**Type:** Stored Procedure

**Purpose**: Retrieves the DTCRoster data for a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @date | Date | The date to retrieve. |

**Logic Flow**

1. Retrieves all roster codes from the TAMS_OCC_Duty_Roster table that match the specified track type.
2. Joins the retrieved roster codes with other tables (TAMS_User) to retrieve additional data.

**Data Interactions**

* Reads: TAMS_OCC_Duty_Roster
* Writes: None

### Procedure: SP_TAMS_Depot_GetParameters

**Type:** Stored Procedure

**Purpose**: Retrieves the parameters for a depot.

**Parameters**

None

**Logic Flow**

1. Retrieves all parameter records from the TAMS_Parameters table that match the specified effective date and expiry date.
2. Filters the results by ParaValue2 = 'Depot'.

**Data Interactions**

* Reads: TAMS_Parameters
* Writes: None

### Procedure: SP_TAMS_Depot_GetUserAccess

**Type:** Stored Procedure

**Purpose**: Checks if a user has access to a depot.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username to check. |
| @res | bit OUTPUT | The result of the access check (1 = allowed, 0 = denied). |

**Logic Flow**

1. Checks if the user exists in the TAMS_User table.
2. If the user exists, checks if they have access to the depot by matching the login ID with the username.

**Data Interactions**

* Reads: TAMS_User
* Writes: None

### Procedure: SP_TAMS_Depot_GetWFStatus

**Type:** Stored Procedure

**Purpose**: Retrieves the workflow status for a depot.

**Parameters**

None

**Logic Flow**

1. Retrieves all workflow records from the TAMS_WFStatus table that match the specified WFType = 'DTCAuth'.

**Data Interactions**

* Reads: TAMS_WFStatus
* Writes: None