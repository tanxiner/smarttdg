# Procedure: SMTP_Update_Email_Lists

### Purpose
This procedure updates the status of an alert in the EALERTQ table and sends an email notification using SMTP.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_AlertID | int | The ID of the alert to be updated. |
| @p_SysID | varchar(50) | The system ID of the user updating the alert. |
| @p_Status | varchar(1) | The new status of the alert. |
| @p_ErrorMsg | varchar(255) OUTPUT | An output parameter to store any error messages. |

### Logic Flow
The procedure starts by setting an initial value for the @p_ErrorMsg parameter. It then updates the EALERTQ table with the provided @p_AlertID, @p_Status, and @p_SysID values. The LASTUPDATEDON field is also updated to the current date and time. If any errors occur during this process, they are stored in the @p_ErrorMsg parameter.

### Data Interactions
* **Reads:** EALERTQ table (specifically, the AlertID column)
* **Writes:** EALERTQ table (specifically, the Status, LASTUPDATEDON, and LASTUPDATEDBY columns)