# Procedure: sp_TAMS_Form_Submit_20220930

### Purpose
Creates or updates a TAR record, populates related sector, station, power, and attachment data, assigns workflow status, and sends a notification email when a Late TAR is submitted.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Railway line identifier (e.g., “NEL”). |
| @AccessDate | NVARCHAR(20) | Date of access request (unused in logic). |
| @AccessType | NVARCHAR(20) | Type of access (“Protection”, “Possession”, etc.). |
| @TARType | NVARCHAR(10) | TAR category (“Late”, “Regular”, etc.). |
| @Sectors | NVARCHAR(2000) | Semicolon‑separated list of sector IDs to include. |
| @PowerSelVal | NVARCHAR(10) | Power selection value (unused). |
| @PowerSelTxt | NVARCHAR(100) | Text describing power state (“Traction Power ON” or OFF). |
| @IsExclusive | INT | Flag indicating exclusive protection (1 = yes). |
| @HODForApp | NVARCHAR(20) | Login ID of the HOD who will approve the TAR. |
| @UserID | NVARCHAR(20) | Login ID of the user submitting the form. |
| @TARID | BIGINT | Primary key of the TAR record to update or create. |
| @Message | NVARCHAR(500) OUTPUT | Error or success message returned to caller. |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark it as internal.  
2. **User Identification** – Resolve `@UserIDID` from `TAMS_User` using the supplied `@UserID`.  
3. **Exclusive Protection Colour** – If `@AccessType` is “Protection” and `@IsExclusive` is 1, fetch the colour code for “Exclusive Protection” from `TAMS_Type_Of_Work`.  
4. **Sector Insertion** – Insert a row into `TAMS_TAR_Sector` for each sector ID in `@Sectors`.  
   * For each sector, set `TARID`, `Line`, `SectorID`, `SectorName`, `SectorType`, and the colour code (exclusive protection colour if applicable).  
5. **Station Insertion** – Insert into `TAMS_TAR_Station` all stations that belong to the supplied sectors.