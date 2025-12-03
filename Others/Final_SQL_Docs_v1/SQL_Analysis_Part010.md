# Procedure: sp_TAMS_Approval_Endorse_20230410
**Type:** Stored Procedure

The procedure is used to approve a TAR (Transportation Authorization Request) and update its status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR. |
| @EID | INTEGER | The current endorser ID. |
| @ELevel | INTEGER | The current endorser level. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approval (mandatory for reject, optional for approved or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_Station, TAMS_TAR_TVF
* **Writes:** TAMS_TAR_Workflow, TAMS_TAR, TAMS_Action_Log

---

# Procedure: sp_TAMS_Approval_Get_Add_BufferZone
**Type:** Stored Procedure

The procedure is used to retrieve the buffer zone information for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR. |

### Logic Flow
1. Retrieves sector and sector ID from TAMS_Sector and TAMS_TAR_Sector tables.
2. Orders results by sector ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector

---

# Procedure: sp_TAMS_Approval_Get_Add_TVFStation
**Type:** Stored Procedure

The procedure is used to retrieve the TVF station information for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR. |

### Logic Flow
1. Retrieves station name, direction, and TVF ID from TAMS_Station and TAMS_TAR_TVF tables.
2. Orders results by station ID.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_TVF