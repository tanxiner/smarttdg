# Procedure: sp_TAMS_RGS_GrantTOA_20230801
**Type:** Stored Procedure

The purpose of this stored procedure is to grant a TAR (Track and Record) to an operator.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be granted. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The ID of the user granting the TAR. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message if an error occurs. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_GrantTOA_20230801_M
**Type:** Stored Procedure

The purpose of this stored procedure is to grant a TAR (Track and Record) to an operator.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be granted. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The ID of the user granting the TAR. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message if an error occurs. |

### Logic Flow
1. Checks if TAR status is 2 (pending).
2. If pending, generates a reference number for the TAR.
3. Updates the TAR status to 3 (granted).
4. Inserts into Audit table.
5. Returns a message indicating whether the TAR was granted successfully.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* **Writes:** TAMS_TOA