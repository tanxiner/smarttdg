# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018_M

### Purpose
Retrieve a filtered list of TAR header records for a user, applying role‑based access and optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Current user identifier |
| @Line | nvarchar(10) | Comma‑separated line codes (e.g., “DTL,NEL”) |
| @TarType | nvarchar(50) | TAR type filter |
| @AccessType | nvarchar(50) | Access type filter |
| @TarStatusId | integer | TAR status identifier filter |
| @AccessDateFrom | nvarchar | Start of access date range (dd‑mm‑yyyy) |
| @AccessDateTo | nvarchar | End of access date range (dd‑mm‑yyyy) |
| @isDTL_Applicant | integer | Flag indicating applicant role for DTL |
| @isDTL_ApplicantHOD | integer | Flag indicating HOD role for DTL |
| @isDTL_PFR | integer | Flag indicating PFR role for DTL |
| @isDTL_PowerEndorser | integer | Flag indicating Power Endorser role for DTL |
| @isDTL_TAPVerifier | integer | Flag indicating TAP Verifier role for DTL |
| @isDTL_TAPApprover | integer | Flag indicating TAP Approver role for DTL |
| @isDTL_TAPHOD | integer | Flag indicating TAPHOD role for DTL |
| @isDTL_ChiefController | integer | Flag indicating Chief Controller role for DTL |
| @isDTL_TrafficController | integer | Flag indicating Traffic Controller role for DTL |
| @isDTL_OCCScheduler | integer | Flag indicating OCC Scheduler role for DTL |
| @isDTL_TAR_SysAdmin | integer | Flag indicating TAR System Administrator role for DTL |
| @isNEL_Applicant | integer | Flag indicating applicant role for NEL |
| @isNEL_ApplicantHOD | integer | Flag indicating HOD role for NEL |
| @isNEL_PFR | integer | Flag indicating PFR role for NEL |
| @isNEL_PowerEndorser | integer | Flag indicating Power Endorser role for NEL |
| @isNEL_TAPVerifier | integer | Flag indicating TAP Verifier role for NEL |
| @isNEL_TAPApprover | integer | Flag indicating TAP Approver role for NEL |
| @isNEL_TAPHOD | integer | Flag indicating TAPHOD role for NEL |
| @isNEL_ChiefController | integer | Flag indicating Chief Controller role for NEL |
| @isNEL_TrafficController | integer | Flag indicating Traffic Controller role for NEL |
| @isNEL_OCCScheduler | integer | Flag indicating OCC Scheduler role for NEL |
| @isNEL_TAR_SysAdmin | integer | Flag indicating TAR System Administrator role for NEL |

### Logic Flow
1. **Line Parsing**  
   - Split the @Line value into two parts: @Line1 (first code) and @Line2 (second code).  
   - @Line1 is used for the primary query; @Line2 is appended later if present.

2. **Condition Construction**  
   - Initialize an empty condition string @cond.  
   - Append filters to @cond when corresponding parameters are supplied: TAR type, access type, status ID, and access date range.  
   - Date filters are converted to the format required by the database.

3. **Dynamic SQL Assembly – Primary Line**  
   - If @Line1 is not empty, evaluate its value.  
   - For “NEL” or “DTL” the procedure builds a SELECT statement that joins the TAR table with the workflow status table to translate status IDs into status names.  
   - The SELECT is wrapped in a sub‑query alias “t” and will later be concatenated with any secondary line query.

4. **Role‑Based Query Selection**  
   - The procedure contains a large series of conditional blocks that choose the exact SELECT clause based on the combination of role flags for the primary line.  
   - Each block corresponds to a specific role scenario (e.g., applicant only, HOD only, or a combination of roles).  
   - For applicant roles, the query filters records where the creator matches @uid.  
   - For HOD roles, the query may restrict records to departments that the user is allowed to view, determined by a lookup in the user‑query‑department table.  
   - When a user has all role flags set to zero, the query defaults to a broad selection that respects only the search filters.

5. **Secondary Line Handling**  
   - If @Line2 is supplied, the procedure repeats the same role‑based logic for that line, appending the resulting SELECT clause to the existing dynamic SQL string.  
   - No UNION is added between the two queries; the results are simply concatenated.

6. **Finalization and Execution**  
   - Close the sub‑query with “as t”.  
   - Print the fully constructed SQL string for debugging purposes.  
   - Execute the dynamic SQL using the EXEC statement.

### Data Interactions
- **Reads**  
  - TAMS_TAR – source of TAR header records.  
  - TAMS_WFStatus – provides status names and status IDs for filtering.  
  - TAMS_User_QueryDept – supplies department lists that a user is permitted to view when acting as a HOD.  
- **Writes**  
  - None. The procedure only performs SELECT operations and executes dynamic SQL; it does not modify any tables.