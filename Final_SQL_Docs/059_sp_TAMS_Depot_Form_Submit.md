# Procedure: sp_TAMS_Depot_Form_Submit

### Purpose
Creates or updates a Depot TAR record, associates sectors, stations, power sectors, SPKS zones, attachments, and initiates the appropriate workflow and notification for the request.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Railway line identifier |
| @TrackType | NVARCHAR(50) | Track type (e.g., NEL, TAMS) |
| @AccessDate | NVARCHAR(20) | Requested access date |
| @AccessType | NVARCHAR(20) | Type of access (Protection, Possession, etc.) |
| @TARType | NVARCHAR(10) | Request urgency (Urgent, Normal, etc.) |
| @Sectors | NVARCHAR(2000) | Semicolon‑separated list of sector IDs |
| @PowerSelVal | NVARCHAR(10) | Power selection value |
| @PowerSelTxt | NVARCHAR(100) | Power selection text |
| @IsExclusive | INT | Flag indicating exclusive protection |
| @HODForApp | NVARCHAR(20) | Login ID of HOD for approval |
| @UserID | NVARCHAR(100) | Login ID of submitting user |
| @TARID | BIGINT | Identifier of the TAR record |
| @Message | NVARCHAR(500) OUTPUT | Result message or error text |

### Logic Flow
1. **Transaction Setup** – Starts a transaction if none exists and sets a flag for internal control.  
2. **User Identification** – Retrieves numeric user ID for the submitting user.  
3. **Sector Colour Determination** – If the request is an exclusive protection, fetches the colour code for the sector.  
4. **Sector Association** – Inserts each selected sector into `TAMS_TAR_Sector` with buffer flag 0 and the determined colour.  
5. **Station Association** – Inserts active stations linked to the selected sectors into `TAMS_TAR_Station`.  
6. **Power Sector Handling**  
   * Determines if traction power is ON.  
   * Inserts non‑buffer power sectors that are either not powered or powered based on the selection, ensuring no duplicates.  
7. **SPKS Zone Association** – Inserts SPKS zones linked to the selected sectors into `TAMS_TAR_SPKSZone`.  
8. **Attachment Transfer** – Moves attachments from the temporary table to `TAMS_TAR_Attachment` for the current TAR.  
9. **Buffer Zone Processing (Possession)** –  
   * Retrieves cross‑over flag from `TAMS_TAR`.  
   * Inserts buffer sectors that match line, track type, power state, and are not already linked.  
   * Updates colour codes for non‑buffer sectors based on the possession type.  
10. **Workflow Determination** –  
    * Checks if the request involves power.  
    * Determines the appropriate workflow ID based on TAR type, day of week, public holiday status, and cut‑off time.  
11. **Workflow Status and Endorser** – Retrieves the initial workflow status and endorser for the selected workflow.  
12. **Reference Number Generation** – Calls `sp_Generate_Ref_Num` to create a TAR reference number.  
13. **TAR Record Update** – Updates the main TAR record with reference number, type, status, power involvement, and power state.  
14. **Workflow Record Insertion** – Inserts a new workflow entry if one does not already exist for the TAR, workflow, and endorser.  
15. **Email Notification (Urgent)** – If the TAR is urgent, composes an email to the HOD with a link to the TAR form and queues it via `EAlertQ_EnQueue`.  
16. **Error Handling** – If any error occurs, sets an error message and rolls back the transaction.  
17. **Commit/Rollback** – Commits the transaction if it was started internally; otherwise leaves it open. Returns the message.

### Data Interactions
* **Reads**  
  * `TAMS_User` – to resolve user IDs.  
  * `TAMS_Type_Of_Work` – to obtain colour codes.  
  * `TAMS_Sector`, `TAMS_Track_Power_Sector`, `TAMS_Power_Sector` – to determine power sectors.  
  * `TAMS_Track_SPKSZone`, `TAMS_SPKSZone` – to determine SPKS zones.  
  * `TAMS_Station`, `TAMS_Entry_Station` – to determine stations.  
  * `TAMS_Buffer_Zone` – to determine buffer sectors.  
  * `TAMS_TAR` – to read cross‑over flag and applicant name.  
  * `TAMS_TAR_AccessReq`, `TAMS_Access_Requirement` – to check power workflow involvement.  
  * `TAMS_Workflow`, `TAMS_Parameters` – to select workflow ID.  
  * `TAMS_Endorser` – to get workflow status and endorser.  
  * `TAMS_Calendar` – to detect public holidays.  
  * `TAMS_Parameters` – to fetch URLs and cut‑off times.  
  * `TAMS_User` – to fetch HOD email.  
* **Writes**  
  * `TAMS_TAR_Sector` – inserts sector links.  
  * `TAMS_TAR_Station` – inserts station links.  
  * `TAMS_TAR_Power_Sector` – inserts power sector links.  
  * `TAMS_TAR_SPKSZone` – inserts SPKS zone links.  
  * `TAMS_TAR_Attachment` – inserts attachments.  
  * `TAMS_TAR` – updates reference number, type, status, power flags.  
  * `TAMS_TAR_Workflow` – inserts workflow entry.  
  * `EAlertQ_EnQueue` – queues email notification.