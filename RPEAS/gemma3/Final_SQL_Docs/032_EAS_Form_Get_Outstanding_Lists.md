# Procedure: EAS_Form_Get_Outstanding_Lists

### Purpose
This procedure retrieves a list of outstanding forms, along with their status and associated authorization information, for a specified user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_UserID | varchar(15) | The identifier of the user requesting the form information. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Master` table.
2.  It filters the selection based on the `active` flag being set to 1, ensuring only currently active forms are considered.
3.  It further filters the selection to include only forms whose `FormGuid` is present in the `EAS_Form_Approve_Lvl` table, where the `userid` matches the input parameter `@P_UserID` and the `active` flag is also set to 1.
4.  The selection is further restricted to forms where the `FormStatus` is not 'Closed', 'Rejected', or 'Withdrawn'.
5.  The results are ordered by the `updatedon` column in ascending order.
6.  For each form, the procedure retrieves the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, and `updatedon` (aliased as `SubmitDate`).
7.  It then determines the `FormStatus`. This is achieved by querying the `EAS_Form_Approve_Lvl` table for the corresponding `FormGuid` and the input user.  If there are pending approvals, the status will indicate the number of days pending approval, otherwise it will indicate "Pending Approval by [User Name]".
8.  The procedure also retrieves authorization information for 'View', 'ReRoute', 'Withdraw', and 'ForApproval' access, using the `EAS_Form_Get_User_Authorized_Functios` function, based on the input user's ID.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`
* **Writes:** None