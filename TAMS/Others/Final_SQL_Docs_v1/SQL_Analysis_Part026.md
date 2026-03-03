# Procedure: sp_TAMS_Depot_RGS_AckSurrender
**Type:** Stored Procedure

The procedure performs an acknowledgement of a surrender for a TAR (Track Access Record) and updates the TOA (Track Operations Authorization) status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be acknowledged. |
| @UserID | NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter containing a message indicating the result of the procedure. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus
* **Writes:** TAMS_TOA, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth

---

# Procedure: sp_TAMS_Depot_RGS_GrantTOA
**Type:** Stored Procedure

The procedure grants a Track Operations Authorization (TOA) for a TAR and updates the TOA status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be granted. |
| @EncTARID | NVARCHAR(250) | The ID of the enclosed TAR (if applicable). |
| @UserID | NVARCHAR(500) | The ID of the user performing the action. |
| @toacallbacktiming | datetime | The callback timing for the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter containing a message indicating the result of the procedure. |

### Logic Flow
1. Checks if TAR status is 2 (pending).
2. Generates a reference number for the TOA.
3. Updates the TOA status and inserts into Audit table.
4. Sends an SMS notification to the user.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus
* **Writes:** TAMS_TOA, TAMS_Depot_Auth_Workflow