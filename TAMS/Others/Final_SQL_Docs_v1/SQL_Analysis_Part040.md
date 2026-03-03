# Procedure: sp_TAMS_Email_Apply_Urgent_TAR_20231009
**Type:** Stored Procedure

Purpose: This stored procedure applies an urgent TAR (Track Access Request) for a specific department and sends an email to the relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | The type of email being sent (e.g. applicant HOD endorsement, TAP HOD endorsement, etc.) |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** None
* **Writes:** TAMS_TAR table

# Procedure: sp_TAMS_Email_Cancel_TAR
**Type:** Stored Procedure

Purpose: This stored procedure cancels a specific Track Access Request (TAR) and sends an email to the relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being cancelled |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** TAMS_TAR table