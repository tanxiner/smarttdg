# Procedure: sp_TAMS_GetTarEnquiryResult_Header

### Purpose
Retrieves a filtered list of TAR records for a specified user, applying role‑based visibility rules and optional search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Identifier of the user making the request |
| @Line | nvarchar(50) | Optional line filter |
| @TrackType | nvarchar(50) | Track type to limit the query |
| @TarType | nvarchar(50) | Optional TAR type filter |
| @AccessType | nvarchar(50) | Optional access type filter |
| @TarStatusId | integer | Optional TAR status identifier |
| @AccessDateFrom | nvarchar(50) | Optional start date for access date filter |
| @AccessDateTo | nvarchar(50) | Optional end date for access date filter |
| @Department | nvarchar(50) | Optional department filter |
| @Userid | nvarchar(50) | Optional creator user filter |

### Logic Flow
1. **Role Determination**  
   - Query the user’s roles for the supplied @TrackType.  
   - If the user holds any of the “all‑access” roles (e.g., NEL_OCCScheduler, DTL_OCCScheduler, etc.), set @IsAll = 1.  
   - If the user holds any of the “power‑endorser” roles (e.g., NEL_PowerEndorser, DTL_PFR, etc.), set @IsPower = 1.  
   - If the user holds any of the “department” roles (e.g., NEL_Applicant, DTL_ApplicantHOD, etc.), set @IsDep = 1.  
   - If the user is marked as external, reset all three flags to 0.

2. **Debug Output**  
   - Print the values of @IsDep, @IsPower, and @IsAll for troubleshooting.

3. **Build Filter Conditions**  
   - Initialize an empty string @cond.  
   - Append SQL fragments to @cond for each non‑empty parameter: @Line, @TarType, @AccessType, @TarStatusId, @AccessDateFrom, @AccessDateTo, @Department, @Userid.  
   - Date fragments convert the string dates to datetime using style 103.

4. **Construct Dynamic SELECT**  
   - Start a base SELECT that numbers rows and joins the result set with TAMS_User to get the creator’s name.  
   - Depending on the role flags, append one of four SELECT blocks:  
     * **@IsAll = 1** – user can see all TARs for the track type.  
     * **@IsPower = 1** – user can see TARs where InvolvePower = 1 or the TAR was created by the user.  
     * **@IsDep = 1** – user can see TARs belonging to their department or created by them.  
     * **Default** – user can only see TARs they created.  
   - Each block joins TAMS_TAR with TAMS_WFStatus (and sometimes TAMS_User) and applies the @cond filters.

5. **Execute**  
   - Print the final dynamic SQL for debugging.  
   - Execute the dynamic SQL using EXEC.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_TAR  
  - TAMS_WFStatus  

* **Writes:**  
  - None

---