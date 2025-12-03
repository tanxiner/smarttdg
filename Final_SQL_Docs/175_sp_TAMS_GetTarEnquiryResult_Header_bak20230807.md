# Procedure: sp_TAMS_GetTarEnquiryResult_Header_bak20230807

### Purpose
Retrieves a filtered list of TAR records for a user, applying role‑based access rules and optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Current user ID |
| @Line | nvarchar(10) | Line identifier (e.g., “NEL‑DTL”) |
| @TrackType | nvarchar(50) | TAR track type filter |
| @TarType | nvarchar(50) | TAR type filter |
| @AccessType | nvarchar(50) | Access type filter |
| @TarStatusId | integer | TAR status ID filter |
| @AccessDateFrom | nvarchar(50) | Start of access date range |
| @AccessDateTo | nvarchar(50) | End of access date range |
| @isNEL_Applicant | bit | Flag indicating NEL applicant role |
| @isDTL_Applicant | bit | Flag indicating DTL applicant role |
| @isNEL_ApplicantHOD | bit | Flag indicating NEL applicant HOD role |
| @isDTL_ApplicantHOD | bit | Flag indicating DTL applicant HOD role |
| @isNEL_PowerEndorser | bit | Flag indicating NEL power endorser role |
| @isDTL_PowerEndorser | bit | Flag indicating DTL power endorser role |
| @isNEL_PowerHOD | bit | Flag indicating NEL power HOD role |
| @isDTL_PowerHOD | bit | Flag indicating DTL power HOD role |
| @isNEL_TAPVerifier | bit | Flag indicating NEL TAP verifier role |
| @isDTL_TAPVerifier | bit | Flag indicating DTL TAP verifier role |
| @isNEL_TAPApprover | bit | Flag indicating NEL TAP approver role |
| @isDTL_TAPApprover | bit | Flag indicating DTL TAP approver role |
| @isNEL_TAPApprover | bit | Flag indicating NEL TAP approver role |
| @isDTL_TAPApprover | bit | Flag indicating DTL TAP approver role |
| @isNEL_TAPApprover | bit | Flag indicating NEL TAP approver role |
| @isDTL_TAPApprover | bit | Flag indicating DTL TAP approver role |
| @isNEL_TAPHOD | bit | Flag indicating NEL TAP HOD role |
| @isDTL_TAPHOD | bit | Flag indicating DTL TAP HOD role |
| @isNEL_ChiefController | bit | Flag indicating NEL chief controller role |
| @isDTL_ChiefController | bit | Flag indicating DTL chief controller role |
| @isNEL_TrafficController | bit | Flag indicating NEL traffic controller role |
| @isDTL_TrafficController | bit | Flag indicating DTL traffic controller role |
| @isNEL_OCCScheduler | bit | Flag indicating NEL OCS scheduler role |
| @isDTL_OCCScheduler | bit | Flag indicating DTL OCS scheduler role |
| @isNEL_TAR_SysAdmin | bit | Flag indicating NEL TAR system admin role |
| @isDTL_TAR_SysAdmin | bit | Flag indicating DTL TAR system admin role |

### Logic Flow
1. **Initialisation** – Variables for line parts, search conditions, and dynamic SQL string are declared.  
2. **Search Condition Construction** – If @TarType, @AccessType, @TarStatusId, @AccessDateFrom, or @AccessDateTo are supplied, corresponding SQL fragments are appended to a condition string (`@cond`).  
3. **Line Parsing** – @Line is split into two parts: the first segment (`@Line1`) and the second segment (`@Line2`).  
4. **Dynamic SQL Building for @Line1**  
   * If @Line1 is “NEL”, a block of nested IFs evaluates the NEL role flags to decide which subset of TAR records the user may see.  
   * If @Line1 is “DTL”, a similar block evaluates DTL role flags.  
   * Each branch constructs a SELECT that joins TAMS_TAR with TAMS_WFStatus, applies the common search conditions, and adds role‑specific predicates such as:  
     * Ownership (`createdby = @uid`)  
     * Power endorser involvement (`InvolvePower = 1`)  
     * Department visibility via TAMS_User_QueryDept  
     * Company‑level visibility for HODs.  
   * The SELECT is wrapped with `row_number() over (order by AccessDate desc)` to provide a sequential index.  
5. **Union for Dual Lines** – If both @Line1 and @Line2 are present, a `union` clause is appended to the dynamic SQL, and the same role‑based logic is repeated for @Line2.  
6. **Finalisation** – The constructed SQL string is closed, printed for debugging, and executed with `EXEC (@sql)`.  
7. **Result** – The procedure returns the result set of the executed dynamic query; no data is modified.

### Data Interactions
- **Reads**  
  * `TAMS_TAR` – main TAR record table.  
  * `TAMS_WFStatus` – workflow status lookup for TAR records.  
  * `TAMS_User_QueryDept` – department visibility mapping for users.  

- **Writes** – None. The procedure only performs SELECT operations.