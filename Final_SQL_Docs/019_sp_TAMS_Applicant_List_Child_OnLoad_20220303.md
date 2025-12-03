# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303

### Purpose
Retrieve a list of TAR records for a specific sector and line, filtered by access dates and TAR type, and return the distinct set of applicant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier for which sectors and TARs are queried. |
| @ToAccessDate | NVARCHAR(20) | Upper bound of the access date range (inclusive). |
| @FromAccessDate | NVARCHAR(20) | Lower bound of the access date range (inclusive). |
| @TARType | NVARCHAR(20) | Optional TAR type filter; if null or empty all types are included. |
| @SectorID | INT | Identifier of the sector to return TARs for. |

### Logic Flow
1. **Current Date Determination**  
   Convert the current system date to a `DATETIME` value (`@CurrDate`) using the 103 (dd/mm/yyyy) style.

2. **Temporary Table Setup**  
   Create two temporary tables:  
   - `#TmpSector` to hold active sectors for the specified line.  
   - `#TmpAppList` to hold applicant (TAR) records that meet the criteria.

3. **Clear Temporary Tables**  
   Truncate both temporary tables to ensure they are empty before insertion.

4. **Populate `#TmpSector`**  
   Insert rows for each active sector on the given line where the current date falls between the sector’s `EffectiveDate` and `ExpiryDate`.  
   The `Direction` column is mapped to `1` for values `'BB'` or `'NB'`, otherwise `2`.  
   Rows are ordered by the sector’s `[Order]` field.

5. **Populate `#TmpAppList`**  
   Insert rows by joining `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector`.  
   Conditions applied:  
   - Matching TAR and sector IDs.  
   - Status ID linked to a workflow status of type `'TARWFStatus'`.  
   - Same line as the input.  
   - TAR status ID not zero.  
   - Sector active and current date within its validity period.  
   - TAR access date between the converted `@ToAccessDate` and `@FromAccessDate`.  
   - TAR type matches `@TARType` if supplied.  
   The `Direction` field is again mapped to `1` or `2` based on the sector’s `Direction` value.

6. **Return Result Set**  
   Select distinct TAR records from `#TmpAppList` where `SectorID` equals `@SectorID`.  
   Group by all selected columns to eliminate duplicates and order the output by `TARID`.

7. **Cleanup**  
   Drop the temporary tables `#TmpSector` and `#TmpAppList`.

### Data Interactions
* **Reads:**  
  - `TAMS_Sector`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Sector`  
  - `TAMS_WFStatus`  

* **Writes:**  
  None to permanent tables (only temporary tables are created and dropped).