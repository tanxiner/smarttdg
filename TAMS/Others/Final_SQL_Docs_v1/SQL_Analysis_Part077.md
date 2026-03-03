# Procedure: sp_TAMS_Inbox_OnLoad
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process TAR (Trade Agreement) inbox data for a given user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID. |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Inserts into the Audit table (not shown).
3. Returns the processed TAR inbox data.

### Data Interactions
* Reads: TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList