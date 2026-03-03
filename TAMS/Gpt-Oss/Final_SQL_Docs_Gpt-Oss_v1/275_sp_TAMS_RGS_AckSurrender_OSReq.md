# Procedure: sp_TAMS_RGS_AckSurrender_OSReq

### Purpose
Acknowledges a surrender request for a TAR, updates related status records, triggers OCC authorization workflow updates, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to acknowledge |
| @UserID | NVARCHAR(500) | User performing the acknowledgment |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns it.
2. **Reset Message** – Clear the output message variable.
3. **Update TOA Status** – Set `TOAStatus` to 5 (acknowledged), record the acknowledgment time, and update audit fields for the specified `TARId`.
4. **Initialize Variables** – Prepare variables for SMS content, status checks, and date/time formatting.
5. **Retrieve TAR and TOA Details** – Join `TAMS_TAR` and `TAMS_TOA` to fetch TAR number, TOA number, line type, acknowledgment time, access date, and operation date for the given `TARId`.
6. **Determine Endorsers** –  
   * If line is `DTL`, select three endorsers at levels 10, 11, and 12 from `TAMS_Endorser` linked to the `OCCAuth` workflow.  
   * If line is not `DTL`, select one endorser at level 7 for `NEL`.
7. **Check All TOAs Acknowledged** –  
   * Open a cursor over all TOAs for the TAR that match the access date and line, excluding statuses 0 and 6.  
   * If any TOA status is not 5, flag that not all are acknowledged.
8. **If All Acknowledged** –  
   * For `DTL` line:  
     - Open a cursor on `TAMS_OCC_Auth` records with status 10 and `PowerOn` 0; for each, update status to 11, log the change, and insert a pending workflow record for `Endorser1`.  
     - Open a cursor on records with status 8; for each, update status to 12, log the change, and insert a terminated workflow record for `Endorser1`.  
     - Repeat similar inserts for `Endorser2` (terminated) and `Endorser3` (pending) on the same set of status‑8 records.  
   * For non‑`DTL` line (`NEL`):  
     - Open a cursor on records with status 7 and `PowerOn` 0; for each, update status to 8, log the change, and insert a pending workflow record for `Endorser1`.
9. **Compose SMS Message** – Build a text string indicating the TOA number, that the surrender was acknowledged by the appropriate OCC (DTL or NEL), the current time and date, and a thank‑you note.
10. **Send SMS** – (Placeholder for SMS sending logic; actual send not shown in code).
11. **Error Handling** – If an error occurs during the SMS send step, set an error message and jump to the error trap.
12. **Commit or Rollback** – If the procedure started its own transaction, commit on success; otherwise rollback on error.
13. **Return** – Output the message string.

### Data Interactions
* **Reads:**  
  - `TAMS_TOA`  
  - `TAMS_TAR`  
  - `TAMS_Endorser`  
  - `TAMS_Workflow`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Auth_Workflow` (for inserts)
* **Writes:**  
  - `TAMS_TOA` (status, timestamps, audit fields)  
  - `TAMS_OCC_Auth` (status updates, audit fields)  
  - `TAMS_OCC_Auth_Workflow` (inserted workflow records)  

---