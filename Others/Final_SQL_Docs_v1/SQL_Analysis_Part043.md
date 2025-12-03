# Procedure: sp_TAMS_Email_Urgent_TAR
**Type:** Stored Procedure

The purpose of this stored procedure is to generate and send an email notification for urgent TAR (Track Access Management System) updates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR update. |
| @TARStatus | NVARCHAR(20) | The status of the TAR update (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR update. |
| @Remarks | NVARCHAR(1000) | Any remarks or comments related to the TAR update. |
| @Actor | NVARCHAR(100) | The actor who performed the action (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend | NVARCHAR(1000) | The list of recipients for the email notification. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR
* Writes: TAMS_TAR

# Procedure: sp_TAMS_Email_Urgent_TAR_20231009
**Type:** Stored Procedure

The purpose of this stored procedure is to generate and send an email notification for urgent TAR (Track Access Management System) updates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR update. |
| @TARStatus | NVARCHAR(20) | The status of the TAR update (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR update. |
| @Remarks | NVARCHAR(1000) | Any remarks or comments related to the TAR update. |
| @Actor | NVARCHAR(100) | The actor who performed the action (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend | NVARCHAR(1000) | The list of recipients for the email notification. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR
* Writes: TAMS_TAR