# Procedure: sp_TAMS_OPD_OnLoad
**Type:** Stored Procedure

Purpose: This stored procedure performs an on-load operation for TAMS OPD data, including retrieving and processing track coordinates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process (DTL or NB) |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Track_Coordinates
* **Writes:** #TmpOPD, TAMS_TOA

# Procedure: sp_TAMS_RGS_AckReg
**Type:** Stored Procedure

Purpose: This stored procedure acknowledges a registration for a TAMS RGS (Registration and Granting System) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Track and Asset Record) to acknowledge |
| @UserID | NVARCHAR(500) | The user ID who is acknowledging the registration |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter for any error messages |

### Logic Flow
1. Checks if the TAR status is valid.
2. If valid, updates the TAR status to 2 (acknowledged).
3. Generates an SMS message with the acknowledgement details.
4. Sends the SMS message using a third-party API.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_AckReg_20221107
**Type:** Stored Procedure

Purpose: This stored procedure acknowledges a registration for a TAMS RGS record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Track and Asset Record) to acknowledge |
| @UserID | NVARCHAR(500) | The user ID who is acknowledging the registration |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter for any error messages |

### Logic Flow
1. Updates the TAR status to 2 (acknowledged).
2. Generates an SMS message with the acknowledgement details.
3. Sends the SMS message using a third-party API.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_AckReg_20230807
**Type:** Stored Procedure

Purpose: This stored procedure acknowledges a registration for a TAMS RGS record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Track and Asset Record) to acknowledge |
| @UserID | NVARCHAR(500) | The user ID who is acknowledging the registration |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter for any error messages |

### Logic Flow
1. Updates the TAR status to 2 (acknowledged).
2. Generates an SMS message with the acknowledgement details.
3. Sends the SMS message using a third-party API.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA