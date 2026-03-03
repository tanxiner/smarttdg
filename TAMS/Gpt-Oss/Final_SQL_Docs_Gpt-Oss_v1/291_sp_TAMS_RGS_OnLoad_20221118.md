# Procedure: sp_TAMS_RGS_OnLoad_20221118

### Purpose
Loads and prepares RGS data for a specified line, generating a list of active requests and a cancel list with calculated times, remarks, and status flags.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line (DTL or NEL) for which RGS data is retrieved. |

### Logic Flow
1. Temporary tables #TmpRGS and #TmpRGSSectors are created and cleared.  
2. Current date and time are captured; a cutoff time of 06:00:00 and a callback time of 04:00 are defined.  
3. Parameters RGSPossessionBG and RGSProtectionBG for the selected line are read from TAMS_Parameters.  
4. OperationDate and AccessDate are set based on whether the current time is before or after the cutoff: after cutoff uses today for operation and tomorrow for access; before cutoff uses yesterday for operation and today for access.  
5. The number of possession records for the line on the access date, where TOAStatus is not 0 or 6 and AccessType is Possession, is counted into @lv_PossessionCtr.  
6. A cursor @Cur01 iterates over TAR and TOA records for the line and access date where TOAStatus is not 0, ordered by AccessType, TOAStatus descending, and Id.  
7. For each record:  
   a. Counters and flags are initialized.  
   b. The ES number is obtained via dbo.TAMS_Get_ES_NoBufferZone.  
   c. Parties name is obtained via dbo.TAMS_Get_TOA_Parties.  
   d. Contact number string is built from MobileNo and TetraRadioNo.  
   e. If the line is DTL, a cursor @Cur02 iterates over sectors linked to the TAR that are not buffer and not gaps; for each sector:  
      - OCCAuth rows with status 10 or 7 buffer are counted; if none, IsTOAAuth is set to 0.  
      - Rows with PowerOffTime are counted; if none, IsPowerOff is set to 0 and PowerOffTime cleared; otherwise PowerOffTime is taken from WorkFlowTime.  
      - Rows with RackedOutTime are counted; if none, IsCircuitBreak is set to 0; otherwise CircuitBreakTime is taken from WorkFlowTime.  
   f. If the line is not DTL, a cursor @Cur02 iterates over power sectors linked to the TAR that are not buffer; similar logic is applied using PowerSection and OCCAuthStatusId 8.  
   g. Remarks are constructed: for DTL, ARRemark and TVFMode are concatenated; for NEL, rack‑out and SCD application requirements are checked and prefixed with “Rack Out” or “SCD” as appropriate, then ARRemark and TVFMode are appended.  
   h. TVF stations are retrieved via dbo.TAMS_Get_TOA_TVF_Stations and appended to the remarks if remarks already exist, or used as the sole remark if none.  
   i. Colour code and grant TOA enable flag are set based on AccessType, TOAStatus, and the possession counter logic, with special handling for possession and protection cases.  
   j. TOACallBackTime is set to empty if TOANo is missing; otherwise it remains 04:00.  
   k. A row containing all calculated fields, flags, and identifiers is inserted into #TmpRGS.  
8. After processing all records, @Cur01 is closed and deallocated.  
9. The RGS list is returned by selecting all rows from #TmpRGS ordered by Sno.  
10. The cancel list is returned by selecting TAR records whose TOAStatus is not in (0,5,6) for the line and access date.  
11. The formatted OperationDate and AccessDate are returned.  
12. Temporary tables are dropped.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Power_Sector, TAMS_Power_Sector, TAMS_TAR_AccessReq, TAMS_Access_Requirement.  
* **Writes:** #TmpRGS, #TmpRGSSectors (temporary tables only).