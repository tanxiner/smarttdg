# Procedure: sp_TAMS_GetTarEnquiryResult_Department

### Purpose
Return a list of distinct company names for TAR records that a user is authorized to view, filtered by optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Identifier of the user making the request |
| @Line | nvarchar(50) | Optional filter for the TAR line |
| @TrackType | nvarchar(50) | Required filter for the TAR track type |
| @TarType | nvarchar(50) | Optional filter for the TAR type |
| @AccessType | nvarchar(50) | Optional filter for the access type |
| @TarStatusId | integer | Optional filter for the TAR status identifier |
| @AccessDateFrom | nvarchar(50) | Optional start date for the access date range |
| @AccessDateTo | nvarchar(50) | Optional end date for the access date range |

### Logic Flow
1. **Role Determination**  
   - Query the user’s roles for the supplied @TrackType.  
   - If the user holds any role in the *All* list (`NEL_OCCScheduler`, `DTL_OCCScheduler`, `NEL_TrafficController`, `DTL_TrafficController`, `NEL_DCC`, `NEL_ChiefController`, `NEL_SDS`, `NEL_TAPApprover`, `NEL_TAPHOD`, `NEL_TAPVerifier`, `DTL_TAPApprover`, `DTL_TAPHOD`, `DTL_TAPVerifier`, `DTL_ChiefController`), set `@IsAll = 1`.  
   - If the user holds any role in the *Power* list (`NEL_PowerEndorser`, `NEL_PowerHOD`, `NEL_PFR`, `DTL_PowerEndorser`, `DTL_PFR`), set `@IsPower = 1`.  
   - If the user holds any role in the *Department* list (`NEL_ApplicantHOD`, `NEL_Applicant`, `DTL_Applicant`, `DTL_ApplicantHOD`), set `@IsDep = 1`.

2. **Build Filter Conditions**  
   - Initialize an empty condition string `@cond`.  
   - Append `AND t.Line='...'` if @Line is provided and not a sentinel value.  
   - Append `AND t.TarType='...'` if @TarType is provided.  
   - Append `AND AccessType='...'` if @AccessType is provided.  
   - Append `AND TarStatusId='...'` if @TarStatusId is provided.  
   - Append date range conditions using `AccessDate >=` and `AccessDate <=` when @AccessDateFrom or @AccessDateTo are supplied.

3. **Construct Dynamic Query**  
   - Start a SELECT that numbers rows (`ROW_NUMBER() OVER(ORDER BY t.company)`) and returns the company column.  
   - Depending on the role flags, choose one of four query templates:  
     * **All** – select distinct companies from `TAMS_TAR` joined with `TAMS_WFStatus` where the status and line match, the track type matches, and the workflow type is `TARWFStatus`.  
     * **Power** – same join, but add a condition that either `t.InvolvePower = 1` or the record was created by the user.  
     * **Department** – same join, but restrict to companies that are either the user’s department (from `TAMS_User`) or the record’s creator.  
     * **Default** – restrict to records created by the user.  
   - Append the previously built `@cond` string to each query to apply the optional filters.

4. **Execute**  
   - Print the final dynamic SQL for debugging.  
   - Execute the dynamic SQL to return the result set.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_TAR  
  - TAMS_WFStatus  

* **Writes:**  
  - None