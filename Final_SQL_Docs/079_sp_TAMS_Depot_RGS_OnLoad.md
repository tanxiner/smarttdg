# Procedure: sp_TAMS_Depot_RGS_OnLoad

### Purpose
Retrieves depot RGS information for a specified line and access date, including status, timing, and related TOA details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target depot line identifier |
| @TrackType | NVARCHAR(50) | (Unused in current logic) |
| @accessDate | DATETIME | Date for which depot data is requested |

### Logic Flow
1. Initialise helper variables: a line break string, current date/time, and a 6 AM cut‑off time.  
2. Set the operation date to the current date (previous day logic is commented out).  
3. Retrieve background colour codes for possession, protection, and cancelled states from **TAMS_Parameters** based on the supplied line.  
4. Define a fixed TOA callback time of 18:00.  
5. Execute a primary SELECT that joins **TAMS_TAR** and **TAMS_TOA** on TARId, filtering for records where:  
   * AccessDate equals @accessDate,  
   * TrackType is 'DEPOT',  
   * TOAStatus is not 0, and  
   * Line matches @Line.  
   For each record the query calculates:  
   * Electrical sections via a scalar function,  
   * PowerOffTime (for NEL lines with PowerOn=1 and Possession access) or the latest PowerOffTiming from **TAMS_Depot_Auth_Powerzone** where PowerOffType='Completed',  
   * CircuitBreakOutTime from the latest RackedOutTiming of type 'Completed' for the relevant access requirement,  
   * PartiesName via a scalar function,  
   * Contact information, TOANo, callback time, radio message times, line clear message time, and remarks via a user‑defined function,  
   * TOA status, a flag indicating whether a TOA authorization exists, and a colour code based on status and access type,  
   * Flags for grant TOA enablement and timestamps for updates and acknowledgements.  
   Results are ordered by AccessType, TOAType, and TARNo.  
6. Run a secondary SELECT to list cancelled or pending TOA records for the same line and access date, returning TARId and TARNo.  
7. Return the operation and access dates formatted as dd/mm/yyyy.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_TAR, TAMS_TOA  
* **Writes:** None