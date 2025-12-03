# Procedure: sp_TAMS_Get_SignUpStatusByLoginID

### Purpose
This stored procedure retrieves and displays the access status for a given login ID, including the workflow status, pending role, and notified date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve access status for. |

### Logic Flow
1. The procedure first checks if a registration exists for the given login ID.
2. If a registration is found, it retrieves the ID of the registration and creates a temporary table to store the access status.
3. It then opens a cursor to iterate through each line and module associated with the registration.
4. For each line and module, it retrieves the workflow status, pending role, and notified date from the TAMS_WFStatus and TAMS_Registration tables.
5. Based on the workflow status, it determines whether the user is external or internal and updates the pending role accordingly.
6. It then inserts a new row into the temporary table with the line, module, workflow status, pending role, and notified date.
7. Finally, it closes the cursor, deallocates the cursor handle, and returns the access status from the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus