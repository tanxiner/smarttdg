# Procedure: sp_TAMS_Depot_Inbox_Master_OnLoad

### Purpose
This stored procedure loads depot inbox data into temporary tables for further processing, ensuring that only pending tasks are included and filtered by user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number to filter tasks by. |
| @TrackType | NVARCHAR(50) | Track type to filter tasks by. |
| @AccessDate | NVARCHAR(20) | Access date to filter tasks by. |
| @TARType | NVARCHAR(20) | Task type to filter tasks by. |
| @LoginUser | NVARCHAR(50) | User ID to filter tasks by. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user.
2. It then creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, inbox data, and a list of tasks, respectively.
3. The procedure truncates these temporary tables before populating them with data from the TAMS_Sector and TAMS_TAR tables.
4. It filters the tasks based on the provided parameters (line number, track type, access date, and task type) and only includes pending tasks that match the user ID.
5. For each task, it checks if there are any workflows associated with it. If not, it inserts the task into the #TmpInboxList table.
6. If there are workflows, it fetches the action by from the TAMS_TAR_Workflow table and checks if the user ID matches. If it does, it increments a counter to track the number of actions by the user.
7. After processing all tasks, it groups the sector data by line, sector ID, sector name, and sector order and returns this data.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_USER
* Writes: #TmpSector, #TmpInbox, #TmpInboxList