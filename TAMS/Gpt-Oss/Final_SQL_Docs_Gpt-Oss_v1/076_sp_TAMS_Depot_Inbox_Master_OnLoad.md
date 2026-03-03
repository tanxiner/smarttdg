# Procedure: sp_TAMS_Depot_Inbox_Master_OnLoad

### Purpose
Retrieves the list of active sectors for a specified line and track type, filtering pending TAR records relevant to the logged‑in user, and returns the sector metadata.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., “DTL”, “NEL”). |
| @TrackType | NVARCHAR(50) | Track type filter for sectors and TARs. |
| @AccessDate | NVARCHAR(20) | Optional access date to narrow TAR selection. |
| @TARType | NVARCHAR(20) | Optional TAR type filter. |
| @LoginUser | NVARCHAR(50) | Login ID of the user invoking the procedure. |

### Logic Flow
1. **User Identification** – The procedure looks up the numeric `Userid` that corresponds to the supplied `@LoginUser` from the `TAMS_USER` table.  
2. **Current Date Setup** – `@CurrDate` is set to today’s date (time truncated).  
3. **Temp Table Preparation** – Three temporary tables are created and cleared:  
   * `#TmpSector` holds sector details for the requested line and track type.  
   * `#TmpInbox` will store candidate TAR records that are pending approval.  
   * `#TmpInboxList` will accumulate the final set of TAR records that the user is allowed to see.  
4. **Sector Selection** – `#TmpSector` is populated with sectors that:  
   * belong to the specified `@Line` and `@TrackType`,  
   * are active (`IsActive = 1`), and  
   * are within their effective date range (`@CurrDate` between `EffectiveDate` and `ExpiryDate`).  
   The rows are ordered by the sector’s defined order.  
5. **Candidate TAR Retrieval** – `#TmpInbox` is filled with TAR records that satisfy:  
   * a pending workflow status (`WFStatus` contains “Pending”),  
   * no assigned user (`UserId = 0`) **or** the assigned user equals the current user,  
   * the endorser’s role matches one of the current user’s roles,  
   * optional filters on `AccessDate` and `TARType` if supplied,  
   * the TAR is not a buffer (`IsBuffer = 0`) and matches the requested `@TrackType`.  
   The query joins `TAMS_TAR`, `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR_Workflow`, and `TAMS_Endorser`.  
6. **Filtering by Workflow History** – A cursor iterates over each row in `#TmpInbox`. For each TAR:  
   * If the TAR has **no** workflow records with a status other than “Pending”, the TAR is added to `#TmpInboxList`.  
   * If there are non‑pending workflow records, a second cursor checks the `ActionBy` field of those records.  
   * If the current user is **not** listed as `ActionBy` in any of those records, the TAR is added to `#TmpInboxList`.  
   This logic ensures that a user only sees a TAR if they are the next approver or if the TAR has never progressed beyond the pending state.  
7. **Result Set** – The procedure finally selects the distinct sector rows from `#TmpSector`, grouped by line, sector ID, sector string, and sector order, and orders them by the sector order.  
   (The `#TmpInboxList` table is not returned; it is used only for internal filtering.)  
8. **Cleanup** – All temporary tables are dropped before the procedure ends.

### Data Interactions
* **Reads:**  
  * `TAMS_USER` – to resolve the numeric user ID.  
  * `TAMS_Sector` – to fetch active sectors for the line and track type.  
  * `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_TAR_Workflow`, `TAMS_Endorser` – to gather pending TARs and their workflow status.  
  * `TAMS_User_Role` – to determine which endorser roles belong to the current user.  

* **Writes:**  
  * Temporary tables `#TmpSector`, `#TmpInbox`, and `#TmpInboxList` are created, populated, and dropped within the session. No permanent tables are modified.