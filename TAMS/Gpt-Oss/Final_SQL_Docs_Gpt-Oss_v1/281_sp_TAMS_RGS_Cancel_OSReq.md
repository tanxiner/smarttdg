# Procedure: sp_TAMS_RGS_Cancel_OSReq

### Purpose
Cancels an outstanding surrender request by marking the TOA record as cancelled, updating related OCC authorisation states, and notifying the relevant party via SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record whose surrender is being cancelled |
| @CancelRemarks | NVARCHAR(1000) | Text explaining why the surrender is cancelled |
| @UserID | NVARCHAR(500) | User performing the cancellation |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and flag that this procedure owns the transaction.
2. **Reset Message** – Initialise the output message to an empty string.
3. **Cancel TOA** – Update the TAMS_TOA row for the supplied @TARID: set status to 6 (cancelled), store @CancelRemarks, and record the update timestamp and user.
4. **Gather Context** – Retrieve TAR number, TOA number, line type (DTL or NEL), access date, and operation date from the TAR and TOA tables.
5. **Determine Endorsers** –  
   * For DTL line: fetch endorser IDs at levels 10, 11, and 12 from the workflow tables.  
   * For NEL line: fetch the endorser ID at level 7.
6. **Check Acknowledgement Status** – Scan all TOA records for the same access date that are not in status 0 or 6.  
   * If any such record has a status other than 5, flag that not all acknowledgements are complete.
7. **If All Acknowledgements Complete** –  
   * **DTL Line**  
     * For each OCCAuth record with status 10 and PowerOn = 0, change status to 11, log the update, and insert a workflow record marking it as Pending for Endorser1.  
     * For each OCCAuth record with status 8, change status to 12, log the update, and insert a workflow record marking it as Terminated for Endorser1.  
     * Insert additional workflow records for Endorser2 (Terminated) and Endorser3 (Pending) for the same set of OCCAuth records.  
   * **NEL Line**  
     * For each OCCAuth record with status 7 and PowerOn = 0, change status to 8, log the update, and insert a workflow record marking it as Pending for Endorser1.
8. **Compose SMS** – Build a message indicating that the surrender has been acknowledged by the appropriate OCC (DTL or NEL) with the current time and date.
9. **Send SMS** – (Placeholder for SMS sending logic; actual send not implemented in the code).
10. **Error Check** – If an error occurred during the insert into the workflow table, set @Message to an error string and jump to the error handler.
11. **Commit or Rollback** – If this procedure started the transaction, commit it; otherwise leave it to the caller. Return the @Message.

### Data Interactions
* **Reads:**  
  - TAMS_TOA  
  - TAMS_TAR  
  - TAMS_Endorser  
  - TAMS_Workflow  
  - TAMS_OCC_Auth  
* **Writes:**  
  - TAMS_TOA (status update)  
  - TAMS_OCC_Auth (status updates)  
  - TAMS_OCC_Auth_Workflow (inserted records)