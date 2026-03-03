# Procedure: sp_TAMS_Form_Save_Access_Reqs

### Purpose
Saves or updates the selected access requirements for a TAR record, inserting the full set of active requirements when none exist, and records any remarks.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Identifier for the line of work to filter requirements. |
| @TrackType | NVARCHAR(50) | Category of the track to filter requirements. |
| @SelAccessReqs | NVARCHAR(200) | Semicolon‑separated list of requirement IDs to mark as selected (non‑power). |
| @PowerSelVal | NVARCHAR(10) | ID of the power requirement to mark as selected. |
| @PowerSelTxt | NVARCHAR(100) | Text description of the selected power requirement (unused in logic). |
| @ARRemarks | NVARCHAR(1000) | Remark text to store on the TAR record. |
| @TARID | BIGINT | Primary key of the TAR record being updated. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and flag that this procedure owns the transaction.  
2. **Initial Insert Check** – Query `TAMS_TAR_AccessReq` for rows with the current `@TARID`.  
   * If none are found, insert a full set of active requirements for the specified `@Line` and `@TrackType` into `TAMS_TAR_AccessReq`. Each inserted row receives the `@TARID`, the requirement `ID`, flags for attachment and power, a default `IsSelected` of 0, and the original order.  
3. **Reset Selections** – Set `IsSelected` to 0 for all rows in `TAMS_TAR_AccessReq` that belong to the current `@TARID`.  
4. **Select Non‑Power Requirements** – Update `TAMS_TAR_AccessReq` rows where `OperationRequirement` matches any ID from the split list `@SelAccessReqs` (filtered to active, non‑power requirements for the same line and track). Set `IsSelected` to 1 for those rows.  
5. **Select Power Requirement** – Update the row whose `OperationRequirement` equals `@PowerSelVal` to set `IsSelected` to 1.  
6. **Update Remarks** – Set the `ARRemark` field of the `TAMS_TAR` record identified by `@TARID` to the supplied `@ARRemarks`.  
7. **Error Handling** – If any error occurs during the above steps, set `@Message` to an error string, roll back the transaction if it was started here, and exit.  
8. **Commit** – If no error, commit the transaction if it was started by this procedure and return the (possibly empty) `@Message`.

### Data Interactions
* **Reads:**  
  - `TAMS_TAR_AccessReq` (to check existence of rows for the TAR)  
  - `TAMS_Access_Requirement` (to retrieve active requirements for insertion and selection)  
  - `SPLIT` function (to split the `@SelAccessReqs` string)  

* **Writes:**  
  - `TAMS_TAR_AccessReq` (insert new rows, update `IsSelected` flags)  
  - `TAMS_TAR` (update `ARRemark` field)