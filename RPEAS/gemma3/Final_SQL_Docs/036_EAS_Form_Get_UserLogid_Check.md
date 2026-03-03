# Procedure: EAS_Form_Get_UserLogid_Check

### Purpose
This procedure determines if a user's session GUID and system ID match existing records in the EAS_User_login table within a specified active period.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) | System identifier associated with the user session. |
| @p_GUID | varchar(225) | The unique identifier for the user session. |
| @p_Cnt | varchar(225) | Output parameter containing the count of matching records. |

### Logic Flow
1.  The procedure begins by executing a count query against the EAS_User_login table.
2.  The count query filters the table based on three criteria: the provided session GUID, the provided system ID, and the current date falling within the start and end dates of a logged-in session.
3.  The count of matching records is then assigned to the output parameter @p_Cnt.

### Data Interactions
* **Reads:** EAS_User_login
* **Writes:** None