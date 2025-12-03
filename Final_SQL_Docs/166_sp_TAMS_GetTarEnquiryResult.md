# Procedure: sp_TAMS_GetTarEnquiryResult

### Purpose
Retrieves a list of TAR records that a user is authorized to view, filtered by line, role, status, and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User identifier used for ownership and permission checks |
| @Line | nvarchar(10) | Line code (e.g., “NEL‑001”) split into primary and secondary parts |
| @AccessType | nvarchar(50) | Optional filter on the type of access |
| @TarStatusId | integer | Optional filter on the TAR status |
| @AccessDateFrom | nvarchar(50) | Optional start date for the access date filter |
| @AccessDateTo | nvarchar(50) | Optional end date for the access date filter |
| @isNEL_Applicant | bit | Flag indicating the user is a NEL applicant |
| @isDTL_Applicant | bit | Flag indicating the user is a DTL applicant |
| @isNEL_ApplicantHOD | bit | Flag indicating the user is a NEL HOD |
| @isDTL_ApplicantHOD | bit | Flag indicating the user is a DTL HOD |
| @isNEL_PowerApprover | bit | Flag indicating the user is a NEL power approver |
| @isDTL_PowerApprover | bit | Flag indicating the user is a DTL power approver |
| @isNEL_PowerVerifier | bit | Flag indicating the user is a NEL power verifier |

### Logic Flow
1. **Initialisation**  
   - Extract the first three characters of @Line into @Line1 (primary line).  
   - Extract characters 5‑7 of @Line into @Line2 (secondary line).  
   - Initialise an empty condition string @cond.

2. **Build Base Conditions**  
   - If @AccessType is supplied and not a placeholder, append a condition on AccessType.  
   - If @TarStatusId is supplied and not a placeholder, append a condition on TarStatusId.  
   - If @AccessDateFrom is supplied, append a condition that AccessDate is on or after that date.  
   - If @AccessDateTo is supplied, append a condition that AccessDate is on or before that date.

3. **Determine Query for Primary Line**  
   - If @Line1 is “NEL” or “DTL”, evaluate the role flags to decide which query fragment to build.  
   - For each role combination, construct a SELECT that pulls tarno, tartype, accesstype, accessdate, and wfstatus from TAMS_TAR_Test joined with TAMS_WFStatus on TARStatusId and Line.  
   - Additional filters applied:  
     * `createdby = @uid` for applicant‑only views.  
     * `InvolvePower = 1` for power‑related views.  
     * `company IN (subquery)` where the subquery selects departments the user can query from TAMS_User_QueryDept.  
   - The constructed fragment is stored in @sql.

4. **Handle Secondary Line (if present)**  
   - If @Line2 is not empty, repeat the same role‑based logic for the secondary line, building a new SELECT fragment.  
   - If both primary and secondary lines are present, prepend a “union” to @sql before adding the secondary fragment.

5. **Execute Dynamic SQL**  
   - The fully assembled @sql string is executed with `EXEC (@sql)`.  
   - No result set is returned directly by the procedure; the dynamic query produces the final result set.

### Data Interactions
* **Reads:**  
  - TAMS_TAR_Test  
  - TAMS_WFStatus  
  - TAMS_User_QueryDept  

* **Writes:**  
  - None

---