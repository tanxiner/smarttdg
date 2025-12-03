# Procedure: sp_TAMS_Get_Depot_TarEnquiryResult_Header

### Purpose
Retrieves a filtered list of TAR records for a user, applying role‑based visibility rules and optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Current user’s identifier |
| @Line | nvarchar(50) | Optional line filter |
| @TrackType | nvarchar(50) | Type of track to limit results |
| @TarType | nvarchar(50) | Optional TAR type filter |
| @AccessType | nvarchar(50) | Optional access type filter |
| @TarStatusId | integer | Optional TAR status identifier |
| @AccessDateFrom | nvarchar(50) | Optional start date for access date range |
| @AccessDateTo | nvarchar(50) | Optional end date for access date range |
| @Department | nvarchar(50) | Optional company/department filter |

### Logic Flow
1. **Role Determination**  
   - Query the user’s roles for the supplied @TrackType.  
   - If the user holds any of the roles `NEL_ApplicantHOD`, `NEL_SDS`, `NEL_TAPApprover`, `NEL_TAPHOD`, or `NEL_TAPVerifier`, set `@IsAll = 1`.  
   - If the user holds any of the roles `NEL_PowerEndorser`, `NEL_PowerHOD`, or `NEL_PFR`, set `@IsPower = 1`.  
   - If the user holds the role `NEL_ApplicantHOD`, set `@IsDep = 1`.

2. **Build Search Conditions**  
   - Initialize an empty condition string `@cond`.  
   - Append SQL fragments for each non‑empty parameter:  
     - `@Line` → `AND t.Line = 'value'`  
     - `@TarType` → `AND t.TarType = 'value'`  
     - `@AccessType` → `AND AccessType = 'value'`  
     - `@TarStatusId` → `AND TarStatusId = 'value'`  
     - `@AccessDateFrom` → `AND AccessDate >= convert(datetime,'value',103)`  
     - `@AccessDateTo` → `AND AccessDate <= convert(datetime,'value',103)`  
     - `@Department` → `AND Company = 'value'`

3. **Construct Main Query**  
   - Start a dynamic SQL string that selects a row‑numbered list of TAR fields from a subquery alias `t`.  
   - Depending on the role flags set earlier, append one of four subquery templates:  
     - **@IsAll**: Select all TARs matching the track type and status, joined to `TAMS_WFStatus`.  
     - **@IsPower**: Select TARs where `InvolvePower = 1` or created by the user, plus track type and status.  
     - **@IsDep**: Select TARs whose company is in the user’s query department list or created by the user, plus track type and status.  
     - **Default**: Select TARs created by the user only, plus track type and status.  
   - Each template includes the previously built `@cond` string to apply the optional filters.

4. **Execute**  
   - Print the final SQL for debugging.  
   - Execute the dynamic SQL to return the result set.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_TAR`  
  - `TAMS_WFStatus`  
  - `TAMS_User_QueryDept`

* **Writes:** None.