# Procedure: sp_TAMS_GetTarEnquiryResult_User20240905

### Purpose
Return a list of TAR records that the specified user is permitted to view, filtered by optional criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Identifier of the user making the request |
| @Line | nvarchar(50) | Optional filter for TAR line |
| @TrackType | nvarchar(50) | Required filter for TAR track type |
| @TarType | nvarchar(50) | Optional filter for TAR type |
| @AccessType | nvarchar(50) | Optional filter for access type |
| @TarStatusId | integer | Optional filter for TAR status identifier |
| @AccessDateFrom | nvarchar(50) | Optional start date for access date range |
| @AccessDateTo | nvarchar(50) | Optional end date for access date range |

### Logic Flow
1. **Role Determination**  
   - Query the user’s roles for the given @TrackType.  
   - If the user holds any of the “all‑view” roles (NEL_DCC, NEL_ChiefController, NEL_SDS, NEL_TAPApprover, NEL_TAPHOD, NEL_TAPVerifier, DTL_TAPApprover, DTL_TAPHOD, DTL_TAPVerifier, DTL_ChiefController) set @IsAll = 1.  
   - If the user holds any of the “power‑endorser” roles (NEL_PowerEndorser, NEL_PowerHOD, NEL_PFR, DTL_PowerEndorser, DTL_PFR) set @IsPower = 1.  
   - If the user holds any of the “department” roles (NEL_ApplicantHOD, NEL_Applicant, DTL_Applicant, DTL_ApplicantHOD) set @IsDep = 1.

2. **Build Filter String**  
   - Initialize @cond as empty.  
   - Append conditions for @Line, @TarType, @AccessType, @TarStatusId, @AccessDateFrom, and @AccessDateTo when they are supplied and not equal to “-1”.  
   - Date filters convert the supplied string to datetime using style 103.

3. **Construct Dynamic SELECT**  
   - Start a SELECT that numbers rows by TAR name.  
   - Depending on the role flags, build a sub‑query that selects distinct `t.createdBy` and the corresponding user name from `TAMS_TAR`, `TAMS_WFStatus`, and `TAMS_User`.  
   - The sub‑query always joins on status, line, and track type, and applies the dynamic @cond filters.  
   - Role‑specific logic:  
     * **@IsAll** – no additional restrictions.  
     * **@IsPower** – include records where `t.InvolvePower = 1` or the record was created by the user.  
     * **@IsDep** – include records where the TAR company matches the user’s department or the record was created by the user.  
     * **Default** – include only records created by the user.

4. **Execute**  
   - Print the constructed SQL for debugging.  
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