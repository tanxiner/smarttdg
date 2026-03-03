# Procedure: sp_TAMS_Inbox_Master_OnLoad

### Purpose
This stored procedure performs a master load of TAMS inbox data, including sectors and corresponding TARs, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line number to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDate | NVARCHAR(20) | Specifies the access date to filter by. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | Specifies the login user ID for filtering purposes. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user ID.
2. It then creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data and TARs with their corresponding access details.
3. The procedure truncates these temporary tables before populating them with new data.
4. It inserts sector data into the #TmpSector table based on the provided line number and track type.
5. For each sector, it selects TARs from the TAMS_TAR table that match the specified TAR type and access date, as well as the user ID.
6. The procedure then checks if there are any pending workflows for each TAR. If not, it inserts the TAR data into the #TmpInboxList table.
7. If there are pending workflows, it opens a cursor to iterate through the workflow actions and checks if the current action is associated with the same user ID as the login user. If so, it increments an action by counter.
8. Based on the action by counter value, it either inserts or skips the TAR data into the #TmpInboxList table.
9. Finally, the procedure joins the sector data from the #TmpSector table with the TAR data from the #TmpInboxList table and groups the results by sector order.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList