# Procedure: sp_TAMS_Update_External_User_Details_By_ID

### Purpose
This stored procedure updates external user details for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user to update. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_User table with the specified UserID.
2. If a record is found, it updates all relevant fields (Name, Department, OfficeNo, MobileNo, Email, SBSTContactPersonName, SBSTContactPersonDept, SBSTContactPersonOfficeNo, ValidTo, IsActive, UpdatedBy, and UpdatedOn) for that user ID.
3. The changes are committed to the database if the update is successful.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table