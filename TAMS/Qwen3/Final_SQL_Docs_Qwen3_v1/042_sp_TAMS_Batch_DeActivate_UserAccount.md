# Procedure: sp_TAMS_Batch_DeActivate_UserAccount

### Purpose
This procedure deactivates a user account based on the number of days since their last login.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @DeAct | BIGINT | The number of days since the user's last login |

### Logic Flow
1. The procedure starts by declaring a variable `@DeAct` to store the number of days since the user's last login.
2. It then selects the value of `ParaValue1` from the `TAMS_Parameters` table where `ParaCode` is 'DeActivateAcct' and the current date falls within the range of `EffectiveDate` and `ExpiryDate`.
3. The selected value is assigned to the `@DeAct` variable.
4. The procedure then updates the `IsActive`, `UpdatedBy`, and `UpdatedOn` columns in the `TAMS_User` table for users who have had their account inactive for at least `@DeAct` days since their last login.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_User
* **Writes:** TAMS_User