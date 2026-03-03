# Procedure: sp_TAMS_SectorBooking_Special_Rule_Chk

### Purpose
Verifies that all required special sector combinations are booked for a given access type when traction power is off.

### Parameters
| Name          | Type          | Purpose |
| :---          | :---          | :--- |
| @AccessType   | NVARCHAR(20)  | Indicates the type of access to check – either ‘Possession’ or ‘Protection’. |
| @Sectors      | NVARCHAR(2000) | Semicolon‑delimited list of sector IDs to evaluate. |
| @PowerSelTxt  | NVARCHAR(50)  | Text that determines if traction power is on; used to set a flag. |

### Logic Flow
1. **Power Flag Determination**  
   - If @PowerSelTxt equals ‘Traction Power ON’, set @PowerOnInd to 1; otherwise 0.  
   - Initialise counters @ISSCtr, @CombSectCtr, @SelCombSectCtr, @RetMsg to 0.

2. **Temp Table Setup**  
   - Create temporary tables #TmpCombSect (CombSectID) and #TmpCombSectMax (CombSectID, Combination, CombCheck).  
   - Truncate both tables to ensure they are empty.

3. **Possession Access Check (Power Off)**  
   - If @AccessType is ‘Possession’ and @PowerOnInd is 0:  
     a. Count special, active sectors in @Sectors and store in @ISSCtr.  
     b. If any exist:  
        i. Insert into #TmpCombSect the CombiSectorId values from TAMS_Special_Sector_Booking where AccessType is ‘Possession’, the sector is in @Sectors, and the record is active.  
        ii. Count total rows in #TmpCombSect → @CombSectCtr.  
        iii. Count rows in #TmpCombSect whose CombSectID appears in @Sectors → @SelCombSectCtr.  
        iv. If @SelCombSectCtr < @CombSectCtr, set @RetMsg to 1 (missing combination); otherwise set @RetMsg to 0.

4. **Protection Access Check (Power Off)**  
   - If @AccessType is ‘Protection’ and @PowerOnInd is 0:  
     a. Count special, active sectors in @Sectors and store in @ISSCtr.  
     b. If any exist:  
        i. Insert into #TmpCombSectMax the distinct SectorId and Combination pairs from TAMS_Special_Sector_Booking where AccessType is ‘Protection’, the sector is in @Sectors, and the record is active; set CombCheck to 0.  
        ii. Open a cursor over #TmpCombSectMax ordered by CombSectID.  
        iii. For each cursor row:  
            - Truncate #TmpCombSect.  
            - Insert into #TmpCombSect the CombiSectorId values for the current SectorId and Combination where the record is active.  
            - Count total rows → @CombSectCtr.  
            - Count rows whose CombSectID appears in @Sectors → @SelCombSectCtr.  
            - If @SelCombSectCtr < @CombSectCtr, update the current #TmpCombSectMax row’s CombCheck to 0 (incomplete); else set it to 1 (complete).  
        iv. After cursor completion, count how many CombSectID groups in #TmpCombSectMax have a sum of CombCheck less than 1.  
        v. If any such groups exist, set @RetMsg to 2 (missing combination); otherwise set @RetMsg to 0.

5. **Result and Cleanup**  
   - Return @RetMsg as RetMsgInd.  
   - Drop the temporary tables #TmpCombSect and #TmpCombSectMax.

### Data Interactions
* **Reads:**  
  - TAMS_Sector  
  - TAMS_Special_Sector_Booking  
  - dbo.SPLIT  

* **Writes:**  
  - #TmpCombSect (temporary)  
  - #TmpCombSectMax (temporary)