# Procedure: sp_TAMS_SectorBooking_SubSet_Chk

### Purpose
This stored procedure checks if two sets of sector IDs are subsets of each other.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @D1SelSec	| NVARCHAR(2000) | The first set of sector IDs separated by semicolons. |
| @D2SelSec	| NVARCHAR(2000) | The second set of sector IDs separated by semicolons. |

### Logic Flow
The procedure works as follows:
1. It creates temporary tables to store the sector IDs from both input sets.
2. It truncates these temporary tables, effectively removing any existing data.
3. It inserts the sector IDs from both input sets into their respective temporary tables.
4. It counts the number of unique sector IDs in each table.
5. If the first set has more unique sector IDs than the second set, it checks if all sector IDs in the first set are present in the second set.
6. If the second set has more unique sector IDs than the first set, it performs a similar check in reverse.
7. Based on these comparisons, the procedure sets an error code indicating whether the two sets are subsets of each other.

### Data Interactions
* **Reads:** [dbo].[SPLIT], [dbo].[SPLIT]
* **Writes:** None