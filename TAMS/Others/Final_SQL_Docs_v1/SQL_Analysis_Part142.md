# Procedure: sp_TAMS_RGS_Update_QTS_test
**Type:** Stored Procedure

The purpose of this stored procedure is to update the QTS status for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to be updated. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration, TAMS_Action_Log, EAlertQ_EnQueue

---

# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID
**Type:** Stored Procedure

The purpose of this stored procedure is to reject a user registration request based on the status of the corresponding registration module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module. |

### Logic Flow
1. Retrieves the registration module details.
2. Checks if the module is in a pending status and rejects it.
3. Sends an email to the user with the rejection reason.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration, EAlertQ_EnQueue

---

# Procedure: sp_TAMS_TOA_QTS_Chk
**Type:** Stored Procedure

The purpose of this stored procedure is to check the QTS status for a given user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @InchargeNRIC | NVARCHAR(50) | The Incharge NRIC. |
| @QualDate | NVARCHAR(20) | The Qualification date. |
| @Line | NVARCHAR(10) | The Line number. |
| @QTSQualCode | NVARCHAR(100) | The QTS qualification code. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR