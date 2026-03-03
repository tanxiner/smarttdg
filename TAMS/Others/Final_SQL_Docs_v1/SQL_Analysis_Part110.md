# Procedure: sp_TAMS_RGS_AckReg_20230807_M
**Type:** Stored Procedure

The procedure acknowledges a registration and updates the status of the TAR (Transportation Authorization Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be acknowledged. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_AckSMS
**Type:** Stored Procedure

The procedure acknowledges an SMS and updates the status of the TAR (Transportation Authorization Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be acknowledged. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR. |
| @SMSType | NVARCHAR(5) | The type of SMS (e.g., 2 for acknowledgement). |

### Logic Flow
1. Checks if user exists.
2. Updates TAMS_TOA table with new status and timestamp.
3. Sends an SMS to the mobile number associated with the TAR.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_AckSMS_20221107
**Type:** Stored Procedure

The procedure acknowledges an SMS and updates the status of the TAR (Transportation Authorization Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be acknowledged. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR. |
| @SMSType | NVARCHAR(5) | The type of SMS (e.g., 2 for acknowledgement). |

### Logic Flow
1. Checks if user exists.
2. Updates TAMS_TOA table with new status and timestamp.
3. Sends an SMS to the mobile number associated with the TAR.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

# Procedure: sp_TAMS_RGS_AckSMS_20221214
**Type:** Stored Procedure

The procedure acknowledges an SMS and updates the status of the TAR (Transportation Authorization Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be acknowledged. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR. |
| @SMSType | NVARCHAR(5) | The type of SMS (e.g., 2 for acknowledgement). |

### Logic Flow
1. Checks if user exists.
2. Updates TAMS_TOA table with new status and timestamp.
3. Inserts into Audit table.
4. Sends an SMS to the mobile number associated with the TAR.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA, TAMS_TOA_Audit