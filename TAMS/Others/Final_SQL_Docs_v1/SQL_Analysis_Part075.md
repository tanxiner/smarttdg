### Procedure: sp_TAMS_Inbox_Master_OnLoad

**Type:** Stored Procedure

### Purpose
This stored procedure loads master data for TAMS Inbox, including sectors and TARs, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(10) | Line number to filter sectors |
| @AccessDate	| NVARCHAR(20) | Access date to filter TARs |
| @TARType	| NVARCHAR(20) | TAR type to filter TARs |
| @LoginUser	| NVARCHAR(50) | Login user ID |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Retrieves the sector IDs and corresponding sector information from the TAMS_Sector table based on the line number and track type.
3. Creates temporary tables to store the sector and TAR data.
4. Truncates the existing data from the temporary tables.
5. Inserts new data into the temporary tables based on the user input parameters.
6. Retrieves the TAR IDs, corresponding TAR information, and sector IDs from the TAMS_TAR table.
7. Filters the TARs to only include those with a pending workflow status and matching access date and TAR type.
8. Iterates through the filtered TARs and checks if the user has an action assigned to them.
9. If no action is assigned, inserts the TAR into the temporary tables.
10. Finally, groups the sector data by line number, sector ID, and direction, and orders the results by sector order.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList