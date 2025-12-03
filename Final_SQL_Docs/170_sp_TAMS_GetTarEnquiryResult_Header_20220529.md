# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529

### Purpose
Retrieves a filtered list of TAR records for a user, supporting multiple lines (NEL, DTL) and role‑based visibility.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Current user identifier |
| @Line | nvarchar(10) | Line code(s) to query, e.g. “NEL‑DTL” |
| @TarType | nvarchar(50) | TAR type filter |
| @AccessType | nvarchar(50) | Access type filter |
| @TarStatusId | integer | TAR status identifier filter |
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
| @isNEL_TAPHOD | bit | Flag indicating NEL TAP HOD role |
| @isDTL_TAPHOD | bit | Flag indicating DTL TAP HOD role |
| @isNEL_TAR_SysAdmin | bit | Flag indicating NEL TAR system admin role |
| @isDTL_TAR_SysAdmin | bit | Flag indicating DTL TAR system admin role |
| @isNEL_PFR | bit | Flag indicating NEL PFR role |
| @isDTL_PFR | bit | Flag indicating DTL PFR role |
| @isNEL_ChiefController | bit | Flag indicating NEL chief controller role |
| @isDTL_ChiefController | bit | Flag indicating DTL chief controller role |
| @isNEL_TrafficController | bit | Flag indicating NEL traffic controller role |
| @isDTL_TrafficController | bit | Flag indicating DTL traffic controller role |
| @isNEL_OCCScheduler | bit | Flag indicating NEL OCS scheduler role |
| @isDTL_OCCScheduler | bit | Flag indicating DTL OCS scheduler role |

### Logic Flow
1. **Line Extraction** – The @Line parameter is split into two parts: @Line1 (first segment) and @Line2 (second segment). Each part is expected to be a line code such as NEL or DTL.  
2. **Base Condition Building** – A string @cond is assembled by appending filters for TAR type, access type, status, and access date range when the corresponding parameters are supplied.  
3. **Dynamic Query Construction** –  
   * For each non‑empty line code, the procedure appends a SELECT block that pulls columns from TAMS_TAR and joins TAMS_WFStatus to resolve the current TAR status.  
   * The SELECT includes a ROW_NUMBER over the TAR number to provide a sequential identifier.  
   * Role flags determine which records are visible:  
     * Applicant roles may see records they created or that involve power endorser involvement.  
     * HOD roles may see records belonging to departments the user is authorized to query, retrieved from TAMS_User_QueryDept.  
     * Power endorser and power HOD roles influence visibility based on the InvolvePower flag.  
     * TAP verifier, TAP approver, TAP HOD, and system admin flags adjust the same logic for the corresponding line.  
   * If both line codes are present, a UNION is added between the two SELECT blocks.  
4. **Finalization** – The constructed SQL string is closed with a parenthesis alias, printed for debugging, and executed via dynamic SQL. No data modification occurs; the procedure only returns a result set.

### Data Interactions
**Read**  
- TAMS_TAR – source of TAR records.  
- TAMS_WFStatus – provides status information for each TAR.  
- TAMS_User_QueryDept – supplies department filters for chief controller and PFR roles.  

**Write**  
- None. The procedure performs only SELECT operations.