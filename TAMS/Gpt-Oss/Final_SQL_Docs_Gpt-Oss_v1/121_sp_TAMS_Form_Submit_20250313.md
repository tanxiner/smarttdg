# Procedure: sp_TAMS_Form_Submit_20250313

### Purpose
Creates or updates a TAR record, associates sectors, stations, power sectors, attachments, and initiates workflow and notification based on TAR type and conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier for the TAR |
| @TrackType | NVARCHAR(50) | Track type for the TAR |
| @AccessDate | NVARCHAR(20) | Date of access request |
| @AccessType | NVARCHAR(20) | Type of access (e.g., Protection, Possession) |
| @TARType | NVARCHAR(10) | Classification of TAR (Urgent, etc.) |
| @Sectors | NVARCHAR(2000) | Semicolon‑delimited list of sector IDs |
| @PowerSelVal | NVARCHAR(10) | Power selection value |
| @PowerSelTxt | NVARCHAR(100) | Power selection text |
| @IsExclusive | INT | Flag indicating exclusive protection |
| @HODForApp | NVARCHAR(20) | Login ID of HOD for approval |
| @UserID | NVARCHAR(100) | Login ID of submitting user |
| @TARID | BIGINT | Identifier of the TAR record |
| @Message | NVARCHAR(500) OUTPUT | Result message or error description |

### Logic Flow
1. **Transaction Setup** – Starts a transaction if none exists and flags internal transaction control.  
2. **User Identification** – Retrieves numeric user ID for the submitting user.  
3. **Sector Colour Determination** – If access type is Protection and exclusive, fetches colour code for exclusive protection.  
4. **Sector Association** – Inserts selected sectors into TAMS_TAR_Sector with colour code and buffer flags.  
5. **Station Association** – Inserts active stations linked to the selected sectors into TAMS_TAR_Station.  
6. **Power Sector Association**  
   - Determines if traction power is ON.  
   - Inserts non‑buffer power sectors first.  
   - Inserts buffer power sectors that are not already present.  
7. **Attachment Transfer** – Moves attachments from temporary table to TAMS_TAR_Attachment.  
8. **Buffer Zone Handling (Possession)** –  
   - Retrieves buffer zone colour code.  
   - Inserts buffer sectors that match line, track, power, and existing sectors.  
   - Adds additional buffer sectors if a crossover flag is set.  
   - Updates colour code for non‑buffer sectors based on possession type.  
9. **Workflow Determination** –  
   - Checks if the TAR involves power.  
   - For urgent TARs, selects workflow based on day of week, public holiday, and cutoff time.  
   - For other types, selects workflow matching TAR type.  
10. **Workflow Status Retrieval** – Gets initial workflow status and endorser for the selected workflow.  
11. **Reference Number Generation** – Calls sp_Generate_Ref_Num to obtain TAR number and message.  
12. **TAR Record Update** – Sets TAR number, type, status, power flags, and creator.  
13. **HOD User Identification** – Retrieves numeric ID for the HOD login.  
14. **Workflow Record Insertion** – Adds a record to TAMS_TAR_Workflow marking status as Pending.  
15. **Email Notification (Urgent)** –  
    - Builds email content with applicant name and link to TAR form.  
    - Enqueues email via EAlertQ_EnQueue for the HOD.  
16. **Error Handling** – If any error occurs, rolls back transaction and returns error message.  
17. **Commit** – Commits transaction if internal transaction was started and returns success message.

### Data Interactions
* **Reads**  
  - TAMS_User (for user and HOD IDs)  
  - TAMS_Type_Of_Work (for colour codes)  
  - TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector (for power sector data)  
  - TAMS_Station, TAMS_Entry_Station (for station data)  
  - TAMS_Buffer_Zone (for buffer zone data)  
  - TAMS_Possession (for possession type)  
  - TAMS_TAR (for existing TAR data)  
  - TAMS_Workflow, TAMS_Parameters, TAMS_Calendar (for workflow selection)  
  - TAMS_Endorser (for workflow status and endorser)  
  - TAMS_Parameters (for approval cutoff time)  
  - TAMS_TAR_Attachment_Temp (for attachments)  
  - TAMS_Parameters (for public holiday check)  

* **Writes**  
  - TAMS_TAR_Sector  
  - TAMS_TAR_Station  
  - TAMS_TAR_Power_Sector  
  - TAMS_TAR_Attachment  
  - TAMS_TAR (update)  
  - TAMS_TAR_Workflow  
  - EAlertQ_EnQueue (via stored procedure call)