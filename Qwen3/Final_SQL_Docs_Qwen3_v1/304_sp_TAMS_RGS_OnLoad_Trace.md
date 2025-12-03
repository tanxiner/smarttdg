# Procedure: sp_TAMS_RGS_OnLoad_Trace

### Purpose
This stored procedure performs a series of operations to trace and record the status of RGS (Remote Ground Station) systems, including power off and circuit break times, parties involved, and other relevant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the procedure is being executed. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure they are empty before processing.
2. It sets various variables based on the current date and time, as well as parameters passed to the procedure.
3. It uses two cursors, @Cur01 and @Cur02, to iterate through TAMS_TAR and TAMS_TOA tables, respectively, filtering rows where the TOAStatus is not 0, 5, or 6, and the AccessDate matches the specified date.
4. For each row in the cursor, it extracts various details such as TARNo, PartiesName, PowerOffTime, CircuitBreakOutTime, etc., and stores them in temporary variables.
5. It then inserts these details into #TmpRGS table based on the line number passed to the procedure.
6. After processing all rows in both cursors, it fetches the Sno values from #TmpRGS and orders them by Sno for display purposes.
7. Finally, it drops the temporary tables and returns.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_Power_Sector
* **Writes:** #TmpRGS, #TmpRGSSectors