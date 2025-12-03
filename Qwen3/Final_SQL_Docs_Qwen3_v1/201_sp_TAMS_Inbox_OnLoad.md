# Procedure: sp_TAMS_Inbox_OnLoad

### Purpose
This stored procedure is used to populate a temporary inbox table with TAR (Task Assignment Record) data that meets specific criteria, including access date and type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the sector. |
| @AccessDate | NVARCHAR(20) | The access date for the TAR data. |
| @TARType | NVARCHAR(20) | The type of TAR data to include. |
| @LoginUser | NVARCHAR(50) | The login user ID. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, TAR data, and a list of TARs with specific criteria, respectively.
3. It populates the #TmpSector table with sector data from TAMS_Sector based on the provided line number and date range.
4. It populates the #TmpInbox table with TAR data from TAMS_TAR that meets specific criteria, including access date and type, and is not already in the inbox list.
5. For each TAR in the #TmpInbox table, it checks if there are any workflows associated with it that have a status other than 'Pending'. If so, it retrieves the action by from TAMS_TAR_Workflow.
6. Based on the action by retrieved, it inserts or updates the corresponding TAR in the #TmpInboxList table.
7. Finally, it joins the #TmpSector and #TmpInboxList tables based on sector ID and direction, and groups the results to display the final inbox data.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_User, TAMS_TAM
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList