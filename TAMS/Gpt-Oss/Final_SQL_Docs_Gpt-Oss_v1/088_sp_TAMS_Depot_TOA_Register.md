# Procedure: sp_TAMS_Depot_TOA_Register

### Purpose
Registers a TOA for a specified TAR at a depot or mainline location, performing validation of TAR status, location, access date, and qualification codes before inserting or updating TOA records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Operational line (e.g., DTL, NEL) used to filter TAR status and determine PowerOn requirement. |
| @TrackType | NVARCHAR(50) | Track type (DEPOT or Mainline) that influences qualification logic and cutoff time. |
| @Type | NVARCHAR(20) | TOA type (e.g., DEPOT) used in the TOA record. |
| @Loc | NVARCHAR(20) | Station name; validated against TAR stations. |
| @TARNo | NVARCHAR(30) | Identifier of the TAR to be processed. |
| @NRIC | NVARCHAR(30) | NRIC of the person requesting the TOA; used for qualification checks and encryption. |
| @TOAID | INT OUTPUT | Returns the ID of the created or updated TOA. |
| @Message | NVARCHAR(50) OUTPUT | Returns a status code or error description indicating the outcome of the registration. |

### Logic Flow
1. **Transaction Setup** – A flag is set to indicate whether the procedure started a transaction; if no outer transaction exists, a new transaction is begun.  
2. **Temporary Table Creation** – A table named #tmpnric is created to hold qualification results for the supplied NRIC.  
3. **Cutoff Time Retrieval** – The TOA cutoff time is fetched from TAMS_Parameters based on @Line and @TrackType.  
4. **Qualification Code Retrieval** – QTS codes are collected for the line and track type. Two sets of codes are obtained: one for normal operation and one for protection scenarios. The selection logic differs for DEPOT versus Mainline.  
5. **TAR Existence Check** – The number of TARs matching @TARNo, the required status (0 for DTL, 1 for NEL), and the PowerOn flag (ignored for DTL) is counted.  
6. **Location Validation** – If @TrackType is DEPOT, the station count is assumed to be one; otherwise, the number of stations linked to the TAR that match @Loc is counted.  
7. **Error Handling for Missing TAR or Station** – If either count is zero, @Message is set to an error code (1 for missing TAR, 2 for missing station) and @RecStatus is marked as failure.  
8. **TAR Detail Retrieval** – When counts are valid, the TAR’s ID, line, access date, and access type are fetched, respecting the PowerOn condition for non‑DTL lines.  
9. **Line Consistency Check** – The requested @Line must match the TAR’s line; a mismatch sets @Message to 4 and marks failure.  
10. **Existing TOA Check** – The current TOA ID for the TAR is obtained.  
11. **Operation Date Determination** – For mainline, the operation date is set to today or yesterday depending on the current time relative to the cutoff; for depot, it is set to today.  
12. **Depot Access Window Validation** – For DEPOT track type, the current access date/time must fall within the allowed window defined by the cutoff; otherwise, @Message is set to 6 or 7.  
13. **Access Date Consistency** – The TAR’s access date must match the expected date (today for DEPOT, tomorrow for Mainline); a mismatch triggers error codes 6, 7, or 8.  
14. **Qualification Processing (No Existing TOA)** –  
    a. Each QTS code is processed by calling either sp_TAMS_Depot_TOA_QTS_Chk or sp_TAMS_TOA_QTS_Chk, inserting the result into #tmpnric.  
    b. The InCharge name and status are extracted from #tmpnric.  
    c. If no valid status and the access type is Protection, the protection QTS codes are processed similarly.  
    d. The final qualification status is determined; if invalid, @Message is set to 5 or 6 and the flow ends.  
15. **TOA Creation** – When qualification is valid, a new TOA record is inserted into TAMS_TOA with encrypted NRIC, timestamps, and status set to 0.  
16. **Audit and Party Records** – An audit entry is added to TAMS_TOA_Audit and a party record is inserted into TAMS_TOA_Parties with the InCharge details.  
17. **Success Code** – @Message is set to 99 and @RecStatus to success.  
18. **Existing TOA Handling** – If a TOA already exists:  
    a. The supplied NRIC is compared to the InCharge NRIC; a mismatch sets @Message to 5.  
    b. If matched, the TOA status is examined: status 0 updates the operation date; status 1 or 2 triggers AddParties or BookOut messages; any other status results in an invalid TAR status error.  
19. **Registration Log** – Every attempt is recorded in TAMS_TOA_Registration_Log with the encrypted NRIC, line, station, TAR number, and outcome.  
20. **Error Trap** – Any error during the process sets @Message to an error string and rolls back the transaction if it was started internally.  
21. **Commit/Rollback** – If the procedure started the transaction, it is committed on success or rolled back on error. The final @Message value is returned.

### Data Interactions
**Reads**  
- TAMS_Parameters (for cutoff time and qualification codes)  
- TAMS_TAR_AccessReq (joined with TAMS_TAR to evaluate operation conditions)  
- TAMS_TAR (for status, line, access date, access type, and PowerOn flag)  
- TAMS_TAR_Station (to count stations linked to the TAR)  
- TAMS_Station (to validate the supplied station name)  
- T