# Procedure: EAS_Form_Get_Completed_Lists

### Purpose
This procedure retrieves a list of completed forms for a specified user, ordered by the most recently updated form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_UserID | varchar(15) | The identifier for the user requesting the form list. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Master` table.
2.  It filters the selection to include only active forms.
3.  It further filters the selection to include only forms whose `FormGuid` is present in the `EAS_Form_Approve_Lvl` table, associated with the provided `@P_UserID`.
4.  The selection is further refined to include only forms where the `FormStatus` is 'Closed', 'Rejected', or 'Withdrawn'.
5.  The results are ordered by the `updatedon` column in descending order, ensuring the most recently updated forms appear first.
6.  The procedure returns the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, `SubmitDate`, `FormStatus`, `Show_View`, `Show_ReRoute`, `Show_Withdraw`, and `Show_ForApproval` columns for each matching form.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`
* **Writes:** None