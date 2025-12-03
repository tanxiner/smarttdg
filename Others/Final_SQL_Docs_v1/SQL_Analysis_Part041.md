### Procedure: sp_TAMS_Email_CompanyRegistrationLinkByRegID

**Type:** Stored Procedure

**Purpose:** This procedure generates an email to a registered company with a link to register their company details.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | NVARCHAR(200) | The ID of the registered company |

**Logic Flow**

1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

**Data Interactions**

* Reads: TAMS_Registration
* Writes: None

### Procedure: sp_TAMS_Email_Late_TAR

**Type:** Stored Procedure

**Purpose:** This procedure generates an email to a late TAR (TAR with a delay) record, informing the recipient of their status and actions required.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR record |
| @TARStatus | NVARCHAR(20) | The status of the late TAR record (e.g. Approved, Rejected, Cancelled) |
| @TARNo | NVARCHAR(50) | The number of the late TAR record |
| @Remarks | NVARCHAR(1000) | Additional remarks about the late TAR record |
| @Actor | NVARCHAR(100) | The actor who endorsed or approved the late TAR record (e.g. Applicant HOD Endorsement, TAP HOD Endorsement) |
| @ToSend | NVARCHAR(1000) | The email address to send the notification to |
| @Message | NVARCHAR(500) = OUTPUT | The generated email message |

**Logic Flow**

1. Checks if user exists.
2. Inserts into Audit table.
3. Generates an email message with the recipient's details and actions required.
4. Executes the EAlertQ_EnQueue stored procedure to send the email.

**Data Interactions**

* Reads: TAMS_TAR
* Writes: None

### Procedure: sp_TAMS_Email_Late_TAR_OCC

**Type:** Stored Procedure

**Purpose:** This procedure generates an email to a late TAR (TAR with a delay) record, informing the recipient of their status and actions required.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR record |
| @TARStatus | NVARCHAR(20) | The status of the late TAR record (e.g. Approved, Rejected, Cancelled) |
| @TARNo | NVARCHAR(50) | The number of the late TAR record |
| @Remarks | NVARCHAR(1000) | Additional remarks about the late TAR record |
| @ToSend | NVARCHAR(1000) | The email address to send the notification to |
| @Message | NVARCHAR(500) = OUTPUT | The generated email message |

**Logic Flow**

1. Checks if user exists.
2. Inserts into Audit table.
3. Generates an email message with the recipient's details and actions required.
4. Executes the EAlertQ_EnQueue stored procedure to send the email.

**Data Interactions**

* Reads: TAMS_TAR
* Writes: None