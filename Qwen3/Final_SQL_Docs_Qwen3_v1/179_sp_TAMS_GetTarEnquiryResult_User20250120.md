# Procedure: sp_TAMS_GetTarEnquiryResult_User20250120

### Purpose
This stored procedure retrieves TAR (Tracking and Analysis Report) data for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR data. |

### Logic Flow
1. The procedure first checks if the user has a specific role (e.g., NEL_DCC, NEL_ChiefController) and if they have access to the desired track type.
2. If the user has multiple roles with different levels of access, it determines which level applies based on the provided parameters.
3. It then constructs a SQL query using the `ROW_NUMBER()` function to assign a unique number to each TAR record, ordered by the user's name.
4. The query joins the TAMS_TAR table with the TAMS_User table to retrieve the user's name and ID.
5. Depending on the user's role and access level, it filters the TAR data based on specific conditions (e.g., involvePower = 1 for PFR/PowerHOD roles).
6. Finally, it executes the constructed SQL query to retrieve the filtered TAR data.

### Data Interactions
* Reads: TAMS_TAR, TAMS_User, TAMS_WFStatus tables.
* Writes: None