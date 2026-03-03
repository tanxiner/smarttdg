# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20240905

### Purpose
Retrieves a list of TAR header records that a user is authorized to view, applying optional filters such as line, TAR type, access type, status, date range, department, and user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | Identifier of the user making the request |
| @Line | nvarchar(50) | Optional line filter; if supplied, only TARs on this line are returned |
| @TrackType | nvarchar(50) | Required track type; used to scope role checks and query joins |
| @TarType | nvarchar(50) | Optional TAR type filter |
| @AccessType | nvarchar(50) | Optional access type filter |
| @TarStatusId | integer | Optional TAR status filter |
| @AccessDateFrom | nvarchar(50) | Optional start of access date range (string in dd/mm/yyyy format) |
| @AccessDateTo | nvarchar(50) | Optional end of access date range (string in dd/mm/yyyy format) |
| @Department | nvarchar(50) | Optional department filter; limits results to TARs created by that department |
| @Userid | nvarchar(50) | Optional user ID filter; limits results to TARs created by that user |

### Logic Flow
1. **Role Determination**  
   - Query the role tables to set three flags:  
     * `@IsAll` – user has any of the broad roles (scheduler, controller, approver, etc.).  
     * `@IsPower` – user has a power‑endorser or PFR role.  
     * `@IsDep` – user is an applicant or applicant HOD.  
   - If the user is marked as external, all three flags are cleared.

2. **Filter Construction**  
   - Initialize an empty condition string `@cond`.  
   - For each optional parameter that is not null, empty, or “-1”, append a corresponding SQL predicate to `@cond`.  
   - Date parameters are converted to datetime using style 103.  
   - Department and Userid parameters add equality checks on `Company` and `Userid`.

3. **Dynamic Query Assembly**  
   - Start a SELECT that numbers rows (`ROW_NUMBER()`) over descending `tarno`.  
   - Depending on the role flags, choose one of four SELECT blocks:  
     * **All‑access** (`@IsAll`): return all TARs matching the track type and conditions.  
     * **Power‑access** (`@IsPower`): return TARs where `InvolvePower = 1` or created by the user.  
     * **Department‑access** (`@IsDep`): return TARs created by the user or whose company matches the user’s department.  
     * **Default**: return only TARs created by the user.  
   - Each block joins `TAMS_TAR` with `TAMS_WFStatus` (to get status text) and `TAMS_User` (to get creator name), applies the track‑type match, and appends the previously built `@cond`.

4. **Execution**  
   - The fully constructed SQL string is printed for debugging and then executed with `EXEC`.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_TAR`  
  - `TAMS_WFStatus`  

* **Writes:** None.