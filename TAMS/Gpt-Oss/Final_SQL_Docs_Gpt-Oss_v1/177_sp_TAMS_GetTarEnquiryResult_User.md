# Procedure: sp_TAMS_GetTarEnquiryResult_User

### Purpose
Return a list of TAR records that a user is authorized to view, filtered by optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Current user’s identifier |
| @Line | nvarchar(50) | Optional line filter |
| @TrackType | nvarchar(50) | Required track type for the query |
| @TarType | nvarchar(50) | Optional TAR type filter |
| @AccessType | nvarchar(50) | Optional access type filter |
| @TarStatusId | integer | Optional TAR status identifier |
| @AccessDateFrom | nvarchar(50) | Optional start date for access date range |
| @AccessDateTo | nvarchar(50) | Optional end date for access date range |

### Logic Flow
1. **Role Determination**  
   - Query the user’s roles for the supplied @TrackType.  
   - If the user holds any of the “all‑view” roles (`NEL_DCC`, `NEL_ChiefController`, `NEL_SDS`, `NEL_TAPApprover`, `NEL_TAPHOD`, `NEL_TAPVerifier`, `DTL_TAPApprover`, `DTL_TAPHOD`, `DTL_TAPVerifier`, `DTL_ChiefController`) set `@IsAll = 1`.  
   - If the user holds any of the “power‑endorser” roles (`NEL_PowerEndorser`, `NEL_PowerHOD`, `NEL_PFR`, `DTL_PowerEndorser`, `DTL_PFR`) set `@IsPower = 1`.  
   - If the user holds any of the “department” roles (`NEL_ApplicantHOD`, `NEL_Applicant`, `DTL_Applicant`, `DTL_ApplicantHOD`) set `@IsDep = 1`.

2. **Build Search Conditions**  
   - Initialize an empty condition string `@cond`.  
   - Append SQL fragments for each non‑empty parameter: `@Line`, `@TarType`, `@AccessType`, `@TarStatusId`.  
   - Append date range fragments for `@AccessDateFrom` and `@AccessDateTo` after converting the string to datetime.

3. **Construct Dynamic SELECT**  
   - Start a base SELECT that numbers rows and returns `createdBy` and user name.  
   - Depending on the role flags:
     - **@IsAll**: select all TARs where the TAR status and line match a workflow status of type `TARWFStatus` and the track type matches @TrackType.  
     - **@IsPower**: select TARs where the workflow status matches, the line matches, the workflow type is `TARWFStatus`, and either `InvolvePower = 1` or the TAR was created by the current user.  
     - **@IsDep**: select TARs where the workflow status matches, the line matches, the workflow type is `TARWFStatus`, the track type matches, and the creator’s company matches the user’s department or the creator is the current user.  
     - **Default**: select TARs where the workflow status matches, the line matches, the track type matches, the workflow type is `TARWFStatus`, and the creator is the current user.  
   - Append the previously built `@cond` to each query.

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
  - None (procedure is read‑only).