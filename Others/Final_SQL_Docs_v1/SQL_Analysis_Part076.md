# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406_M
**Type:** Stored Procedure

### Purpose
This stored procedure loads master data for TAMS Inbox, including sectors and TARs, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Sector line number to load |
| @AccessDate | NVARCHAR(20) | Access date for TARs (optional) |
| @TARType | NVARCHAR(20) | TAR type to load (optional) |
| @LoginUser | NVARCHAR(50) | User ID of the current user |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Loads sectors from the TAMS_Sector table that match the specified line number and are active, with an effective date within the current month.
3. For each sector, loads TARs from the TAMS_TAR table that have a pending workflow status and do not have a gap in the sector order.
4. If no TARs are found for a sector, it is added to the #TmpInboxList table.
5. If one or more TARs are found for a sector, their details are inserted into the #TmpInboxList table.
6. The procedure then iterates through the TARs in the #TmpInbox table and checks if they have an associated workflow status update.
7. If no updates are found, each TAR is added to the #TmpInboxList table.
8. Finally, the procedure returns the loaded data.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList