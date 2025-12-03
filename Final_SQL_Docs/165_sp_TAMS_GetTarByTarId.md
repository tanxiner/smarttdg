# Procedure: sp_TAMS_GetTarByTarId

### Purpose
Retrieve a single TAR record and its related status and withdrawer information by the TAR Id.

### Parameters
| Name     | Type    | Purpose |
| :------- | :------ | :------ |
| @TarId   | integer | Identifier of the TAR record to fetch; defaults to 0 if not supplied. |

### Logic Flow
1. The procedure receives an integer `@TarId`.  
2. It performs a `SELECT` on the `TAMS_TAR` table, filtering rows where `[Id]` equals `@TarId`.  
3. For each column in the result set, the procedure returns the raw value from `TAMS_TAR`.  
4. The `WithdrawDate` column is converted to a string in `dd/mm/yyyy` format using `Convert(varchar,WithdrawDate,103)`.  
5. The `WithdrawBy` column is populated by a sub‑query that selects the top 1 `Name` from `TAMS_User` where `Userid` matches the `WithdrawBy` value in `TAMS_TAR`.  
6. The `TARStatus` column is populated by a sub‑query that selects the top 1 `WFStatus` from `TAMS_WFStatus` where:
   - `WFStatusId` equals the `TARStatusId` from `TAMS_TAR`;
   - `Line` matches the `Line` value in `TAMS_TAR`;
   - `TrackType` matches the `TrackType` value in `TAMS_TAR`;
   - `WFType` equals `'TARWFStatus'`.  
7. The result set contains all requested columns, including the derived `WithdrawDate`, `WithdrawBy`, and `TARStatus` values.  
8. The procedure ends after returning the single row (or no row if the Id does not exist).

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_User`, `TAMS_WFStatus`  
* **Writes:** None

---