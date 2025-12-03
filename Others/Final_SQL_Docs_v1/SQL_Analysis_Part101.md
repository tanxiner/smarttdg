### Procedure: sp_TAMS_OCC_InsertTVFAckByParameters

**Purpose**: This stored procedure inserts a new TVF Acknowledgement into the TAMS_TVF_Acknowledge table and logs an audit entry.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation |
| @AccessDate | datetime | The date of access |
| @UserID | int | The ID of the user who performed the action |
| @StationId | int | The ID of the station where the TVF was acknowledged |
| @TVFMode | varchar(10) | The mode of the TVF |
| @TVFDirection1 | bit | The direction of the first TVF |
| @TVFDirection2 | bit | The direction of the second TVF |

**Logic Flow**

1. Checks if a user exists for the given station ID and operation date.
2. Inserts into the TAMS_TVF_Acknowledge table with the provided parameters.
3. Logs an audit entry in the TAMS_TVF_Acknowledge_Audit table.

**Data Interactions**

* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge

### Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable

**Purpose**: This stored procedure inserts a new duty roster entry into the TAMS_OCC_Duty_Roster table and logs an audit entry.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | dbo.TAMS_OCC_DutyRoster | The duty roster to be inserted |

**Logic Flow**

1. Checks if a new duty roster needs to be inserted.
2. If not, updates the existing entry with the provided parameters.
3. Logs an audit entry in the TAMS_OCC_Duty_Roster_Audit table.

**Data Interactions**

* **Reads:** @TAMS_OCC_DutyRoster
* **Writes:** TAMS_OCC_Duty_Roster

### Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116

This procedure is identical to the previous one, with the same logic flow and data interactions.

### Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116_M

This procedure is also identical to the previous ones, with the same logic flow and data interactions.

### Procedure: sp_TAMS_OCC_InsertToOCCAuthTable

**Purpose**: This stored procedure inserts a new OCC Auth entry into the TAMS_OCC_Auth table.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth | dbo.TAMS_OCC_Auth | The OCC Auth to be inserted |

**Logic Flow**

1. Inserts into the TAMS_OCC_Auth table with the provided parameters.
2. Logs an audit entry in the TAMS_OCC_Auth_Audit table.

**Data Interactions**

* **Reads:** @TAMS_OCC_Auth
* **Writes:** TAMS_OCC_Auth

### Procedure: sp_TAMS_OCC_InsertToOCCAuthWorkflowTable

**Purpose**: This stored procedure inserts a new OCC Auth Workflow entry into the TAMS_OCC_Auth_Workflow table.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth_Workflow | dbo.TAMS_OCC_Auth_Workflow | The OCC Auth Workflow to be inserted |

**Logic Flow**

1. Inserts into the TAMS_OCC_Auth_Workflow table with the provided parameters.
2. Logs an audit entry in the TAMS_OCC_Auth_Workflow_Audit table.

**Data Interactions**

* **Reads:** @TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_OCC_Auth_Workflow

### Procedure: sp_TAMS_OCC_RejectTVFAckByParameters_PFR

**Purpose**: This stored procedure rejects a TVF Acknowledgement and logs an audit entry.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation |
| @AccessDate | datetime | The date of access |
| @UserID | int | The ID of the user who performed the action |
| @StationId | int | The ID of the station where the TVF was acknowledged |
| @TVFMode | varchar(10) | The mode of the TVF |
| @TVFDirection1 | bit | The direction of the first TVF |
| @TVFDirection2 | bit | The direction of the second TVF |

**Logic Flow**

1. Updates the TAMS_TVF_Acknowledge table to reflect that the TVF has been rejected.
2. Logs an audit entry in the TAMS_TVF_Acknowledge_Audit table.

**Data Interactions**

* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge

Tables used:

1. TAMS_TVF_Acknowledge
2. TAMS_OCC_Duty_Roster
3. TAMS_OCC_Duty_Roster_Audit
4. TAMS_OCC_Auth
5. TAMS_OCC_Auth_Audit
6. TAMS_OCC_Auth_Workflow
7. TAMS_OCC_Auth_Workflow_Audit