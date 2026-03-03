# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406_M

### Purpose
This stored procedure performs a daily load of TAR (Trade Agreement Record) inbox data, removing any cancelled records and populating the #TmpInboxList table with the remaining records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(10) | The line number to process. |
| @AccessDate	| NVARCHAR(20) | The access date for the TARs. |
| @TARType	| NVARCHAR(20) | The type of TAR to load. |
| @LoginUser	| NVARCHAR(50) | The login user ID. |
| @SectorID	| INT | The sector ID. |

### Logic Flow
1. The procedure starts by selecting the current user ID from the TAMS_USER table based on the provided login user ID.
2. It then sets the current date and time to the GETDATE() function, which returns the current date and time in the format specified.
3. The procedure creates temporary tables #TmpSector and #TmpInbox to store the sector data and TAR inbox records, respectively.
4. It truncates these temporary tables to ensure they are empty before populating them with new data.
5. The procedure then selects the sector data from the TAMS_Sector table based on the provided line number and filters out any inactive or expired sectors.
6. Next, it selects the TAR inbox records from the TAMS_TAR table, filtering out any cancelled records (based on the WFStatus column) and records with a user ID other than the current user ID.
7. The procedure then creates a cursor (@Cur01) to iterate through the #TmpInbox table, selecting each record in turn.
8. For each record, it checks if there are any workflow actions associated with that TAR (based on the TAMS_TAR_Workflow table). If not, it inserts the record into the #TmpInboxList table.
9. If there are workflow actions associated with the TAR, it creates another cursor (@Cur02) to iterate through these actions and checks if the current user ID is the action owner. If so, it increments a counter variable (@ActionByChk).
10. After iterating through all the workflow actions, if the counter variable (@ActionByChk) is still 0, it means that the TAR has no associated workflow actions and inserts the record into the #TmpInboxList table.
11. Finally, the procedure selects the records from the #TmpInboxList table and groups them by TAR ID, line number, sector ID, access date, and type.

### Data Interactions
* **Reads:**
	+ TAMS_USER
	+ TAMS_Sector
	+ TAMS_TAR
	+ TAMS_TAR_Workflow
	+ TAMS_Endorser
* **Writes:** None