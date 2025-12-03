# sp_TAMS_GetTarEnquiryResult_Header_20220529_M

## Purpose  
Retrieves a filtered list of TAR header records for one or two operational lines (e.g., NEL, DTL) by constructing and executing dynamic SQL. The query is tailored to the caller’s role flags and optional filter criteria such as TAR type, access type, status, and access dates.

## Parameters  

| Name | Type | Inferred Usage |
|------|------|----------------|
| @uid | int | User identifier used for role‑specific filtering (createdby, department lookup). |
| @Line | varchar | Comma‑separated list of line codes; first three characters form @Line1, characters 5‑7 form @Line2. |
| @TarType | varchar | TAR type filter; “-1” indicates no filter. |
| @AccessType | varchar | Access type filter; “-1” indicates no filter. |
| @TarStatus | varchar | TAR status filter; “-1” indicates no filter. |
| @AccessDateFrom | varchar | Start of access date range; empty or “-1” means no lower bound. |
| @AccessDateTo | varchar | End of access date range; empty or “-1” means no upper bound. |
| @isApplicant | bit | Flag indicating the caller is an applicant. |
| @isApplicantHOD | bit | Flag indicating the caller is a Head‑of‑Department. |
| @isPowerEndorser | bit | Flag indicating the caller is a power endorser. |
| @isPFR | bit | Flag indicating the caller is a PFR. |
| @isTAPVerifier | bit | Flag indicating the caller is a TAP verifier. |
| @isTAPApprover | bit | Flag indicating the caller is a TAP approver. |
| @isTAPHOD | bit | Flag indicating the caller is a TAP HOD. |
| @isChiefController | bit | Flag indicating the caller is a chief controller. |
| @isTrafficController | bit | Flag indicating the caller is a traffic controller. |
| @isOCCScheduler | bit | Flag indicating the caller is an OCC scheduler. |
| @isTarSysAdmin | bit | Flag indicating the caller is a TAR system administrator. |
| @isPowerEndorser | bit | (duplicate flag for power endorser role). |
| @isPFR | bit | (duplicate flag for PFR role). |
| @isTAPVerifier | bit | (duplicate flag for TAP verifier role). |
| @isTAPApprover | bit | (duplicate flag for TAP approver role). |
| @isTAPHOD | bit | (duplicate flag for TAP HOD role). |
| @isChiefController | bit | (duplicate flag for chief controller role). |
| @isTrafficController | bit | (duplicate flag for traffic controller role). |
| @isOCCScheduler | bit | (duplicate flag for OCC scheduler role). |
| @isTarSysAdmin | bit | (duplicate flag for TAR system administrator role). |

## Logic Flow  

1. **Line Extraction**  
   - `@Line1` is set to the first three characters of `@Line`.  
   - `@Line2` is set to characters 5‑7 of `@Line`.  
   - The procedure prints `@Line1` for debugging.

2. **Condition Building (`@cond`)**  
   - If `@TarType` is not “-1”, append a `t.tartype = @TarType` clause.  
   - If `@AccessType` is not “-1”, append a `t.accesstype = @AccessType` clause.  
   - If `@TarStatus` is not “-1”, append a `t.TarStatusId = @TarStatus` clause.  
   - If `@AccessDateFrom` is provided, append `t.AccessDate >= @AccessDateFrom`.  
   - If `@AccessDateTo` is provided, append `t.AccessDate <= @AccessDateTo`.  
   - All clauses are concatenated into `@cond`.

3. **Dynamic SQL Construction (`@sql`)**  
   - Begins with a `SELECT` that assigns a row number (`ROW_NUMBER() OVER (ORDER BY t.tarno)`) as `id` and selects header fields from `TAMS_TAR` joined to `TAMS_WFStatus` on status ID.  
   - The query is wrapped in a sub‑select `as t` at the end.

4. **Line‑Specific Query Building**  
   - For `@Line1` equal to “NEL” or “DTL”, a series of nested `IF` statements evaluate the role flags.  
   - Depending on the combination of applicant, HOD, power endorser, PFR, TAP verifier/approver/HOD, chief controller, traffic controller, OCC scheduler, and system admin flags, the SELECT is modified to include:  
     - `createdby = @uid` for applicant role.  
     - `t.InvolvePower = 1` to include records where power is involved.  
     - `t.company IN (SELECT TARQueryDept …)` to restrict to departments the user can query.  
     - `t.Line = @Line1` to restrict to the current line.  
   - The same logic is repeated for `@Line2` if it is not empty, appending the corresponding SELECT to `@sql` (no explicit UNION is used; the code comments suggest a union could be added).

5. **Finalization**  
   - After all conditional SELECT fragments are concatenated, the procedure appends `) as t` to close the sub‑query.  
   - The complete dynamic SQL string is printed for debugging.  
   - The procedure executes the dynamic SQL with `EXEC (@sql)`.

6. **Result**  
   - The executed query returns a result set of TAR header records, including fields such as `id`, `line`, `tarno`, `tartype`, `accesstype`, `accessdate`, `tarstatus`, and `company`, ordered by `tarno` with a row number.

## Data Interactions  

- **Reads**  
  - `TAMS_TAR` – source of TAR header data.  
  - `TAMS_WFStatus` – provides human‑readable status text for each TAR.  
  - `TAMS_User_QueryDept` – supplies department codes that a user is allowed to query for certain roles.

- **Writes**  
  - None. The procedure only selects data; it does not insert, update, or delete records.