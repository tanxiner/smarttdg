# Procedure: SMTP_Update_Email_Lists

### Purpose
Updates the status and audit fields of a specific alert record in the EALERTQ table.

### Parameters
| Name          | Type          | Purpose |
| :---          | :---          | :--- |
| @p_AlertID    | int           | Identifier of the alert to update |
| @p_SysID      | varchar(50)   | System identifier used for audit tracking |
| @p_Status     | varchar(1)    | New status value to assign to the alert |
| @p_ErrorMsg   | varchar(255) OUTPUT | Receives any error message (currently unused) |

### Logic Flow
1. Initialize the output error message to an empty string.  
2. Execute an UPDATE on the EALERTQ table setting:
   - `Status` to the supplied @p_Status value.  
   - `LASTUPDATEDON` to the current date and time.  
   - `LASTUPDATEDBY` to the supplied @p_SysID value.  
   The update targets the row where `AlertID` equals @p_AlertID.

### Data Interactions
* **Reads:** None  
* **Writes:** EALERTQ (updates Status, LASTUPDATEDON, LASTUPDATEDBY for the specified AlertID)