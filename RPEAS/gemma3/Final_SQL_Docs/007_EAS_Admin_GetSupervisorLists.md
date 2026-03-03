# Procedure: EAS_Admin_GetSupervisorLists

### Purpose
This procedure retrieves a list of supervisor details, including their name, designation, and active status, based on a provided user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PAID | VARCHAR(50) | The UserID of the employee for whom to retrieve supervisor details. |

### Logic Flow
1.  The procedure begins by selecting supervisor details from the `EAS_User` table (aliased as `r`) and the `EAS_PA_Supervisor` table (aliased as `ur`) where the `supervisorid` in `EAS_PA_Supervisor` matches the `UserID` in `EAS_User` and the `userid` in `EAS_PA_Supervisor` matches the input parameter `@PAID`.  It selects the supervisor's ID as `LanID`, name, designation, business area, department, section, active status (represented as 'True' or 'False'), and a flag indicating if the supervisor is selected ('True' or 'False').
2.  The procedure then adds a second set of results by selecting all users from the `EAS_User` table (aliased as `r`) whose `UserID` is *not* present in the `EAS_PA_Supervisor` table where the `userid` matches the input parameter `@PAID`. This effectively identifies supervisors who are not directly associated with the specified user.
3.  The results from both queries are combined using a `UNION ALL` operation.
4.  Finally, the combined result set is ordered by the supervisor's ID (`LanID`).

### Data Interactions
* **Reads:** `EAS_User`, `EAS_PA_Supervisor`
* **Writes:** None