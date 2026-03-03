# Procedure: EAS_Form_Save_ReRoute_ProceedNxtLevel

### Purpose
This procedure updates a form record and initiates a re-routing or progression to the next approval level based on a specified re-route type, logging the actions and potentially sending related emails.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_Userid | varchar(15) | The identifier of the user performing the action. |
| @P_FormLevel | int | The current approval level of the form. |
| @P_ReRouteType | varchar(15) | Indicates the type of re-routing or progression ('R' for Re-Route, 'N' for Next Level). |
| @P_ReRouteTo | varchar(15) | The identifier of the user to which the form is re-routed. |
| @P_Remarks | varchar(1000) |  A description of the action taken. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  **Initialization:** Sets the output error message parameter to an empty string.
2.  **Try Block:** Encloses the core logic within a transaction to ensure atomicity.
3.  **Transaction Start:** Begins a new database transaction.
4.  **Form Master Update:** Updates the `EAS_Form_Master` table with the user ID and timestamp, associated with the form's GUID.
5.  **Re-Route Logic (if @P_ReRouteType = 'R'):**
    *   **Existing Record Update:** Updates the `EAS_Form_Approve_Lvl` table, setting the action to 'Re-Routed', the remarks, the re-route type, the re-route to user, and marking the record as inactive. The action is performed by the user, and the timestamp is recorded.
    *   **New Record Insertion:** Inserts a new record into the `EAS_Form_Approve_Lvl` table with the form GUID, approval level, re-route to user, active status set to 1, created by the user, and the creation timestamp.
    *   **Log History Insertion:** Inserts a record into the `EAS_Form_Log_History` table with the form GUID, remarks, action (determined by the re-route type), action by the user, and the timestamp.
    *   **Re-Route Email Execution:** Executes the stored procedure `EAS_Send_ReRoute_Email` to send a re-route email.
6.  **Proceed to Next Level Logic (if @P_ReRouteType = 'N'):**
    *   **Next Level User Retrieval:** Selects the next approval level user ID and approval level from the `EAS_Form_Approve_Lvl` table, filtering for active records with an approval level greater than the current level, no action taken, and ordered by approval level.
    *   **Existing Record Update:** Updates the `EAS_Form_Approve_Lvl` record, setting the action to 'Proceed to Next Level', the remarks, the re-route type, the re-route to the next level user, and marking the record as inactive. The action is performed by the user, and the timestamp is recorded.
    *   **Log History Insertion:** Inserts a record into the `EAS_Form_Log_History` table with the form GUID, remarks, action (determined by the re-route type), action by the user, and the timestamp.
    *   **Proceed to Next Level Email Execution:** Executes the stored procedure `EAS_Send_ProcdNxtLvl_Email` to send a proceed to next level email.
7.  **Transaction Commit:** Commits the database transaction.
8.  **Error Handling (Catch Block):** If any error occurs within the try block:
    *   Sets the output error message parameter with the error message.
    *   Rolls back the database transaction.
9.  **Error Message Assignment:** Assigns the value of the output error message parameter to the output parameter @P_ErrorMsge.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
* **Writes:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`