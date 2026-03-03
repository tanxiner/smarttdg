# Procedure: sp_TAMS_Depot_GetTarEnquiryResult_Department

### Purpose
Return a list of company names for TAR records that a user is authorized to view, filtered by optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User identifier used to determine role membership and ownership |
| @Line | nvarchar(50) | Optional line filter; if provided and not '-1', restricts results to that line |
| @TrackType | nvarchar(50) | Required track type; used in role checks and query filtering |
| @TarType | nvarchar(50) | Optional TAR type filter; applied when not null, empty, or '-1' |
| @AccessType | nvarchar(50) | Optional access type filter; applied when not null, empty, or '-1' |
| @TarStatusId | integer | Optional TAR status filter; applied when not null, empty, or '-1' |
| @AccessDateFrom | nvarchar(50) | Optional start date for AccessDate filter; converted to datetime |
| @AccessDateTo | nvarchar(50) | Optional end date for AccessDate filter; converted to datetime |

### Logic Flow
1. **Role Determination**  
   - Query `TAMS_User`, `TAMS_User_Role`, and `TAMS_Role` to see if the user has any of the following roles for the supplied `@TrackType`:  
     * `NEL_ChiefController`, `NEL_DCC`, `NEL_ApplicantHOD`, `NEL_SDS`, `NEL_TAPApprover`, `NEL_TAPHOD`, `NEL_TAPVerifier`.  
     If found, set `@IsAll = 1`.  
   - Repeat the query for roles `NEL_PowerEndorser`, `NEL_PowerHOD`, `NEL_PFR`; if found, set `@IsPower = 1`.  
   - Repeat the query for role `NEL_ApplicantHOD`; if found, set `@IsDep = 1`.

2. **Build Search Condition (`@cond`)**  
   - Initialize `@cond` as an empty string.  
   - Append `AND t.Line='value'` if `@Line` is supplied and not '-1'.  
   - Append `AND t.TarType='value'` if `@TarType` is supplied and not '-1'.  
   - Append `AND AccessType='value'` if `@AccessType` is supplied and not '-1'.  
   - Append `AND TarStatusId='value'` if `@TarStatusId` is supplied and not '-1'.  
   - Append `AND AccessDate >= convert(datetime,'value',103)` if `@AccessDateFrom` is supplied.  
   - Append `AND AccessDate <= convert(datetime,'value',103)` if `@AccessDateTo` is supplied.

3. **Construct Dynamic SQL (`@sql`)**  
   - Start with a SELECT that numbers rows and selects `t.company` from a subquery.  
   - Depending on role flags:  
     * If `@IsAll = 1`: select distinct `t.company` from `TAMS_TAR` joined to `TAMS_WFStatus` where status and line match, `TrackType` equals `@TrackType`, `WFType` is `TARWFStatus`, and apply `@cond`.  
     * Else if `@IsPower = 1`: same join, but add condition that either `t.InvolvePower = 1` or `t.createdby = @uid`, and `TrackType` equals `@TrackType`.  
     * Else if `@IsDep = 1`: same join, add condition that `t.TrackType = @TrackType` and either `t.company` is in the set of departments returned by `TAMS_User_QueryDept` for the user (where `TARQueryDept` starts with `NEL`) or `t.createdby = @uid`.  
     * Else (no special role): same join, add condition that `t.createdby = @uid`.  
   - Close the subquery and finish the statement.

4. **Execute**  
   - Print the constructed SQL for debugging.  
   - Execute the dynamic SQL to return the result set.

### Data Interactions
* **Reads:**  
  - `TAMS_User`, `TAMS_User_Role`, `TAMS_Role` (role checks)  
  - `TAMS_TAR`, `TAMS_WFStatus` (main query)  
  - `TAMS_User_QueryDept` (department list for dependent role)  

* **Writes:** None.