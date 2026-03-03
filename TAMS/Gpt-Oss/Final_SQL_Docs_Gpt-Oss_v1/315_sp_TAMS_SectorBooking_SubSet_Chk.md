# Procedure: sp_TAMS_SectorBooking_SubSet_Chk

### Purpose
Determines whether one semicolon‑delimited list of sector IDs is a subset of the other and returns a status indicator.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @D1SelSec | NVARCHAR(2000) | Semicolon‑separated list of sector IDs for the first set. |
| @D2SelSec | NVARCHAR(2000) | Semicolon‑separated list of sector IDs for the second set. |

### Logic Flow
1. Initialise a return message variable `@RetMsg` to 0 (no error).  
2. Create two temporary tables `#TmpD1Sel` and `#TmpD2Sel` each with a single `SecID` column.  
3. Populate `#TmpD1Sel` by splitting `@D1SelSec` on ';' using the `[dbo].[SPLIT]` function; do the same for `#TmpD2Sel` with `@D2SelSec`.  
4. Count the number of rows in each temporary table and store them in `@D1MaxCtr` and `@D2MaxCtr`.  
5. Compare the string lengths of the input parameters:  
   * If `@D1SelSec` is longer than `@D2SelSec`:  
     - Count how many `SecID`s from `#TmpD1Sel` also appear in `#TmpD2Sel` and store in `@D1Chk`.  
     - If `@D1Chk` equals `@D2MaxCtr`, set `@RetMsg` to 0 (subset).  
     - Otherwise set `@RetMsg` to 1 (first list longer but not a subset).  
   * Otherwise (the second list is longer or equal):  
     - Count how many `SecID`s from `#TmpD2Sel` also appear in `#TmpD1Sel` and store in `@D2Chk`.  
     - If `@D2Chk` equals `@D1MaxCtr`, set `@RetMsg` to 0 (subset).  
     - Otherwise set `@RetMsg` to 2 (second list longer but not a subset).  
6. Return the value of `@RetMsg` as `RetMsgInd`.  
7. Drop the temporary tables.

### Data Interactions
* **Reads:** `[dbo].[SPLIT]` function (used to split the input strings).  
* **Writes:** Temporary tables `#TmpD1Sel` and `#TmpD2Sel` (created and dropped within the procedure).