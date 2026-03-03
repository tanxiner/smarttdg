# Procedure: sp_TAMS_TOA_OnLoad

### Purpose
Retrieve detailed information for a specific TOA record identified by @TOAID.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TOAID | BIGINT | Identifier of the TOA record to load |

### Logic Flow
1. Accept @TOAID as input.  
2. Query the TAMS_TOA table for the row where Id equals @TOAID.  
3. Join that row to the TAMS_TAR table on the TARId foreign key.  
4. For the matched pair, select the following columns:  
   - QRLocation from TAMS_TOA  
   - TARNo from TAMS_TAR  
   - InChargeNRIC from TAMS_TOA, decrypted and masked to 4 characters  
   - InChargeName, MobileNo, TetraRadioNo from TAMS_TOA, defaulting to empty string if NULL  
   - TVFMode from TAMS_TAR, defaulting to 'N.A' if NULL  
   - NoOfParties from TAMS_TOA, defaulting to 1 if NULL  
   - TOANo from TAMS_TOA, defaulting to empty string if NULL  
   - ProtectionType from TAMS_TOA, defaulting to empty string if NULL  
5. Return the result set containing these columns.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR  
* **Writes:** None