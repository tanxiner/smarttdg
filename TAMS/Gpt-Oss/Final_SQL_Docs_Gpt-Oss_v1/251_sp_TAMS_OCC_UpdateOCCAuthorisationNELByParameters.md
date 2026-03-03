**Procedure Overview**

`TAMS_TMS_OCC_Auth_Update` is a T‑SQL stored procedure that updates an OCC (On‑Site Control) authorization record and its associated workflow.  
It also records every change in audit tables so that the history of the authorization and its workflow can be traced.

---

### 1. Parameters

| Parameter | Purpose |
|-----------|---------|
| `@OCCAuthID` | The primary key of the OCC authorization record to be updated. |
| `@OCCLevel` | The current workflow level (step) that is being processed. |
| `@SelectionValue` | The new status value chosen by the user (e.g., “Approved”, “Rejected”). |
| `@Remarks` | A comment or note entered by the user. |
| `@PFRRemark` | A remark related to the Power‑On/Power‑Off request. |
| `@UserID` | The ID of the user performing the update. |

---

### 2. Transaction Handling

The procedure runs inside a `TRY…CATCH` block.  
A transaction is started at the beginning; if everything succeeds, the transaction is committed.  
If any error occurs, the transaction is rolled back to keep the database consistent.

---

### 3. Validation

1. **Existence Check** – The procedure first verifies that a record with the supplied `@OCCAuthID` exists in the `TAMS_OCC_Auth` table.  
   If it does not exist, the procedure exits immediately.

2. **Retrieve Current Details** – If the record exists, the procedure pulls the following fields into local variables:  
   * `Line`, `OperationDate`, `AccessDate`, `TractionPowerId`, `PowerOn`, `PowerOffTime`, `RackedOutTime`, `IsBuffer`, `PowerOn`, `PFRRemark`, `PFRRemark`, `OCCAuthStatusId`, `IsBuffer`, `PowerOn`, `PowerOffTime`, `RackedOutTime`, `CreatedOn`, `CreatedBy`, `UpdatedOn`, `UpdatedBy`.  
   These values are used later for status updates and audit logging.

---

### 4. Workflow Update Logic

The core of the procedure is a series of `IF @OCCLevel = X` blocks.  
Each block represents a specific step in the OCC authorization workflow.  
The logic inside each block follows a common pattern:

1. **Determine the Current Workflow**  
   * Find the workflow definition that matches the current `Line`, `TrackType`, and is active.  
   * Retrieve the `WorkflowId` and the `OCCEndorserID` (the user or role responsible for the current level).

2. **Update the Current Workflow Record**  
   * Set the workflow status (`WFStatus`) to either the supplied `@SelectionValue` or a fixed value such as “Completed”.  
   * Record the action time (`ActionOn`) and the acting user (`ActionBy`).

3. **Advance to the Next Level**  
   * Identify the next workflow record (`@OCCEndorserID_Next`) that will be pending.  
   * Insert a new pending record into `TAMS_OCC_Auth_Workflow` for the next level.  
   * Update the main `TAMS_OCC_Auth` record’s status (`OCCAuthStatusId`) to reflect the new workflow level.

4. **Special Cases**  
   * Some levels perform additional actions, such as setting `PowerOn`, `PowerOffTime`, or `RackedOutTime`.  
   * Certain levels simply mark the workflow as “Completed” and do not create a new pending record.

5. **Audit Logging**  
   * After each update, the procedure inserts corresponding records into the audit tables:  
     * `TAMS_OCC_Auth_Workflow_Audit` – logs updates (`U`) and inserts (`I`) for workflow records.  
     * `TAMS_OCC_Auth_Audit` – logs updates to the main authorization record.

---

### 5. Detailed Level‑by‑Level Behavior

| Level | Typical Action |
|-------|----------------|
| **1** | Marks the first workflow step as “Completed” and creates a pending record for the next step. |
| **2** | Similar to level 1 but also updates the main authorization status. |
| **3** | Sets the status to the supplied `@SelectionValue` and advances to the next step. |
| **4** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **5** | Updates the status to the supplied value and advances. |
| **6** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **7** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **8** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **9** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **10** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **11** | Updates the status to the supplied value and advances. |
| **12** | Updates the status to the supplied value and advances. |
| **13** | Updates the status to the supplied value and advances. |
| **14** | Marks the current step as “Completed” and creates a pending record for the next step. |
| **15** | Marks the current step as “Completed” and sets the final status to 15. |

*Note:* The exact meaning of each level depends on the business process (e.g., power‑on, buffer, power‑off, rack‑out). The procedure ensures that the workflow moves sequentially through these levels, updating the main authorization record and logging every change.

---

### 6. Audit Logging

After the workflow update, the procedure writes audit entries to three tables:

1. **`TAMS_OCC_Auth_Workflow_Audit`** – Records both the update (`U`) of the current workflow record and the insert (`I`) of the new pending record.
2. **`TAMS_OCC_Auth_Audit`** – Records the update (`U`) of the main authorization record, capturing all relevant fields and the user who performed the action.

These audit tables provide a complete history of every change made to the OCC authorization and its workflow.

---

### 7. Completion

If all operations succeed, the transaction is committed, making the changes permanent.  
If any error occurs during the process, the transaction is rolled back, leaving the database unchanged.

---

**In Summary**

`TAMS_TMS_OCC_Auth_Update` is a robust, level‑driven workflow updater for OCC authorizations.  
It validates the target record, updates the workflow step based on the current level and user selection, advances to the next step, updates the main authorization status, and logs every change for auditability—all within a single, atomic transaction.