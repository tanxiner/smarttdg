# Procedure: EAS_Form_Get_All_Froms

### Purpose
This stored procedure retrieves all form records from the EAS_Form_Master table, filtering based on form status, title, date range, and user permissions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormStatus | varchar(1) | Specifies the form status to filter by ('P' for Progress, 'C' for Completed). |
| @P_FormTitle | varchar(100) | Specifies the form title to filter by. |
| @P_DateFrom | varchar(10) | Specifies the start date for the date range filter. |
| @P_DateTo | varchar(10) | Specifies the end date for the date range filter. |
| @P_UserID | varchar(10) | Specifies the user ID to determine user permissions. |

### Logic Flow
The stored procedure first determines the user's role and permissions. It checks if the user is a super administrator or IT administrator.

1.  **Role Determination:** The procedure checks if the user has a role of 'SUPER_ADMIN' or 'IT_ADMIN' from the `EAS_User_Role` table, using the provided `@P_UserID`. If the user has one of these roles, they are granted full access to all forms.

2.  **Form Status Filtering:**
    *   **'P' (Progress Forms):** If the `@P_FormStatus` is 'P', the procedure retrieves form records where the `FormStatus` is not 'Closed', 'Rejected', or 'Withdrawn'. It then further filters based on the approval status of the form.
        *   If the user is a super administrator, it retrieves all records matching the criteria.
        *   If the user is not a super administrator, it retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.

    *   **'C' (Completed Forms):** If the `@P_FormStatus` is 'C', the procedure retrieves form records where the `FormStatus` is 'Closed', 'Rejected', or 'Withdrawn'. It then retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.
        *   If the user is a super administrator, it retrieves all records matching the criteria.
        *   If the user is not a super administrator, it retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.

3.  **Date Filtering:** The procedure filters the form records based on the provided `@P_DateFrom` and `@P_DateTo` values, ensuring that the form creation date falls within the specified date range.

4.  **Title Filtering:** The procedure filters the form records based on the provided `@P_FormTitle` value, using a wildcard search to find forms with titles that contain the specified text.

5.  **Data Retrieval:** Finally, the procedure retrieves the form data, including the form GUID, document reference number, document type, company, title, submit date (calculated from the `updatedon` field), and the form status (calculated based on the approval status).

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_User_Role`, `EAS_User`, `EAS_Form_Pending_NODays`
*   **Writes:** None