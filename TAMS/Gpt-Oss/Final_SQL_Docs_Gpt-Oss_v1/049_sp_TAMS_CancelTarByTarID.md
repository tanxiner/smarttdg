# Procedure: sp_TAMS_CancelTarByTarID

### Purpose
Cancels a TAR record identified by @TarId, updates its status, and logs the cancellation action.

### Parameters
| Name   | Type    | Purpose |
| :----- | :------ | :------ |
| @TarId | integer | Identifier of the TAR to cancel |
| @UID   | integer | Identifier of the user performing the cancellation |

### Logic Flow
1. Begin a database transaction.  
2. Retrieve the `line` value from `TAMS_TAR` where `Id` equals @TarId.  
3. Look up the workflow status ID for a cancellation in `TAMS_WFStatus` where `Line` matches the retrieved line, `WFType` is 'TARWFStatus', and `WFStatus` is 'Cancel'.  
4. Fetch the user’s name from `TAMS_User` using @UID.  
5. Update `TAMS_TAR` setting `TARStatusId` to the retrieved status ID for the record with `Id` = @TarId.  
6. Insert a new record into `TAMS_Action_Log` recording the line, object type 'TAR', action 'Enquiry-Cancel', the TAR ID, a descriptive message that includes the user’s name and the current date, the current timestamp, and the user ID.  
7. Commit the transaction.  
8. If any error occurs during the transaction, roll back all changes.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User  
* **Writes:** TAMS_TAR, TAMS_Action_Log