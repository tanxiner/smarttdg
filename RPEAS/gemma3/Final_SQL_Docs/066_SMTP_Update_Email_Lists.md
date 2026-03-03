# Procedure: SMTP_Update_Email_Lists

### Purpose
This procedure updates records in the EALERTQ table to reflect the status of an alert and records the update activity.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_AlertID | int | The unique identifier for the alert being processed. |
| @p_SysID | varchar(50) | The system identifier used to track the update activity. |
| @p_ErrorMsg | varchar(255) | An output parameter to hold any error messages encountered during the process. |

### Logic Flow
The procedure begins by initializing the @p_ErrorMsg output parameter to an empty string.  It then updates records within the EALERTQ table. The update sets the Status field to 'S', records the date and time of the last update using the current date and time function, and records the system identifier (@p_SysID) as the user who performed the update. The update is performed based on the provided @p_AlertID, identifying the specific alert record to be modified.

### Data Interactions
* **Reads:** EALERTQ
* **Writes:** EALERTQ