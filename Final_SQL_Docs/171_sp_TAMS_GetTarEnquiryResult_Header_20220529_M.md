# sp_TAMS_GetTarEnquiryResult_Header_20220529_M

## Parameters
| Parameter | Description |
|-----------|-------------|
| @UserId | Identifier of the user executing the enquiry. |
| @Line | Comma‑separated list of line codes (e.g., `'DTL,NEL,SPLRT'`). |
| @TarType | Filter for tariff type; `-1` means no filter. |
| @Access | Filter for access type; `-1` means no filter. |
| @TarStatus | Filter for tariff status; `-1` means no filter. |
| @FromDate | Start of the date range (format `dd-mm-yyyy`). |
| @ToDate | End of the date range (format `dd-mm-yyyy`). |
| @IsApplicant, @IsApplicantHOD, @IsPFR, @IsPowerEndorser, @IsTapVerifier, @IsTapApprover, @IsTapHOD, @IsChiefController, @IsTrafficController, @IsOccScheduler, @IsTarSysAdmin | Boolean flags (0/1) that describe the user’s role for each line. |

## Logic Overview
1. **Line Parsing**  
   The `@Line` string is split into two parts:  
   - `@Line1` – the first code (e.g., `DTL`).  
   - `@Line2` – the second code if present (e.g., `NEL`).  
   These codes determine which tables and filters will be applied.

2. **Filter Construction**  
   A string `@cond` is built to hold optional `WHERE` clauses based on the supplied filters: tariff type, access, status, and the date range.  
   Each filter is appended only when its value differs from `-1`.

3. **Dynamic Query Assembly**  
   For each line (`@Line1` and, if present, `@Line2`), the procedure evaluates the role flags to decide which records to return.  
   The decision logic follows a pattern:  
   - If the user is a plain applicant (`@IsApplicant = 1` and all other role flags = 0), only records where the user is the creator are selected.  
   - If the user is an applicant with a power endorser or PFR flag, records where the user is the creator **or** the record involves power are selected.  
   - If the user is an applicant with no power endorser or PFR but is a HOD, records are limited to the departments the user can query (via `TAMS_User_QueryDept`).  
   - If the user is not an applicant but has the power endorser or PFR flag, only records that involve power are selected.  
   - If the user is a HOD with no power endorser or PFR, records are limited to the user’s query departments.  
   - If the user is a HOD with power endorser or PFR, records are limited to the user’s query departments **or** involve power.  
   - If none of the above conditions match, all records for the line are returned.  

   The same logic is applied to the second line (`@Line2`) when it exists, with the same set of role flags.

4. **Final Query Execution**  
   After assembling the full SQL string, the procedure prints the query for debugging and then executes it. The result set contains header information for all tariff records that satisfy the constructed filters and role‑based restrictions.

## Tables Used
- `TAMS_TAR` – source of tariff header records.  
- `TAMS_WFStatus` – provides workflow status information for each tariff.  
- `TAMS_User_QueryDept` – holds the list of departments a user is allowed to query for each line.