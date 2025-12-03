# Procedure: sp_TAMS_Approval_Add_BufferZone

### Purpose
This stored procedure adds a new buffer zone to a TAMS TAR record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record. |
| @SectorID | BIGINT | The ID of the sector to be added as a buffer zone. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It then checks if a sector with the specified ID already exists in the TAMS_TAR_Sector table for the given TARID. If not, it proceeds to add the sector as a buffer zone.
3. To determine the colour code for the buffer zone, it queries the TAMS_Type_Of_Work table based on the line from the TAMS_TAR record with the matching ID.
4. It then inserts a new row into the TAMS_TAR_Sector table with the specified TARID, sector ID, and colour code.

### Data Interactions
* **Reads:** [dbo].[TAMS_TAR], [dbo].[TAMS_TAR_Sector], [dbo].[TAMS_Type_Of_Work], [dbo].[TAMS_Sector]
* **Writes:** [dbo].[TAMS_TAR_Sector]