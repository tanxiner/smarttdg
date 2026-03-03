# Procedure: sp_TAMS_RGS_Cancel_OSReq
**Type:** Stored Procedure

Purpose: Cancels an OS Request for a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to cancel the OS request for. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_OCC_Auth, TAMS_TAR
* **Writes:** TAMS_TOA, TAMS_OCC_Auth

---

# Procedure: sp_TAMS_RGS_Get_UpdDets
**Type:** Stored Procedure

Purpose: Retrieves updated details for a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to retrieve updated details for. |

### Logic Flow
1. Selects InChargeNRIC, MobileNo, and TetraRadioNo from TAMS_TOA where TARId = @TARID.

### Data Interactions
* **Reads:** TAMS_TOA

---

# Procedure: sp_TAMS_RGS_GrantTOA
**Type:** Stored Procedure

Purpose: Grants TOA for a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to grant TOA for. |
| @EncTARID | NVARCHAR(250) | The Encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The user ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message. |

### Logic Flow
1. Checks if TOA status is 2.
2. Generates a reference number for the TOA grant.
3. Updates TAMS_TOA with new TOA status and reference number.
4. Inserts into TAMS_TOA_Audit.
5. Sends SMS to the user's mobile number.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_OCC_Auth, TAMS_TOA
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_TOA_Audit