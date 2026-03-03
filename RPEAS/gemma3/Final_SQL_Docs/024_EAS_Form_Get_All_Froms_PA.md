# Procedure: EAS_Form_Get_All_Froms_PA

### Purpose
This stored procedure retrieves form data based on the form status and title, filtering for forms that have been submitted by a user with a PA role and within a specified date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormStatus | varchar(1) | Specifies the form status ('P' for Progress, 'C' for Completed). |
| @P_FormTitle | varchar(100) | Specifies the form title to search for. |
| @P_DateFrom | varchar(10) | Specifies the start date for the date range. |
| @P_DateTo | varchar(10) | Specifies the end date for the date range. |
| @P_UserID | varchar(10) | The UserID of the user to filter by. |

### Logic Flow
1.  **User Role Check:** The procedure first checks if the provided @P_UserID has a PA role. It does this by querying the `EAS_User_Role` table to determine if the user has the 'PA' role and is active. If the user does not have a PA role, the procedure will not return any data.
2.  **Form Status Handling:**
    *   **Progress Forms ('P'):** If @P_FormStatus is 'P', the procedure retrieves form data from the `EAS_Form_Master` table. It filters for forms that are not in the 'Closed', 'Rejected', or 'Withdrawn' status. It also filters based on the @P_FormTitle using a LIKE operator, allowing for partial matches. The date range is applied to filter forms created within the specified @P_DateFrom and @P_DateTo.  The procedure also checks if the form's GUID is present in a list of form GUIDs associated with users who are supervisors and have a matching @P_UserID.
    *   **Completed Forms ('C'):** If @P_FormStatus is 'C', the procedure retrieves form data from the `EAS_Form_Master` table, filtering for forms in the 'Closed', 'Rejected', or 'Withdrawn' status. It filters based on the @P_FormTitle using a LIKE operator, allowing for partial matches. The date range is applied to filter forms created within the specified @P_DateFrom and @P_DateTo. The procedure also checks if the form's GUID is present in a list of form GUIDs associated with users who are supervisors and have a matching @P_UserID.
3.  **Data Retrieval:** The procedure retrieves the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, `updatedon` (as SubmitDate), and `FormStatus` from the `EAS_Form_Master` table. It also retrieves the `Applevel` and `userid` from the `EAS_Form_Approve_Lvl` table.
4.  **Grouping and Ordering:** The results are grouped by `FormGuid`, `Applevel`, `userid`, `DocRefNo`, `DocType`, `Company`, `Title`, and `updatedon` to avoid duplicate records. The results are then ordered by `updatedon` in descending order.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_User_Role`, `EAS_User`, `EAS_Form_Approve_Lvl`, `EAS_PA_Supervisor`
*   **Writes:** None