# Procedure: sp_TAMS_TOA_Get_Parties

### Purpose
Retrieve party details, witness lists, and booking statistics for a specified TOA record.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TOAID | BIGINT | Identifier of the TOA record to query |

### Logic Flow
1. **Party Count** – Return the `NoOfParties` value from `TAMS_TOA` where `Id` matches the supplied `@TOAID`.  
2. **Party Details** – Return a numbered list of all parties linked to the TOA:  
   - `Sno` is a row number ordered by `ID`.  
   - `PartiesName` is the party’s name.  
   - `PartiesNRIC` is the masked NRIC obtained by decrypting `NRIC` and masking the first four characters.  
   - `PartiesIsTMC` shows “Yes” if `IsTMC` equals 1, otherwise “No”.  
   - `InCharge` shows “Y” if `IsInCharge` equals 1, otherwise “N”.  
   - `RecID` is the party’s record ID.  
   - `BookInStatus` is the current booking status.  
   The rows are ordered by `ID` ascending.  
3. **Witness List** – Return the names and IDs of parties where `IsInCharge` is 0 (i.e., not the in‑charge party), ordered by `ID`.  
4. **Selected Witness** – Return the ID of the party that is marked as a witness (`IsWitness = 1`) and not in charge.  
5. **Work Parties Booked Count** – Count parties that are not in charge and whose `BookInStatus` is ‘In’.  
6. **Total Parties Booked Count** – Count all parties whose `BookInStatus` is ‘In’, regardless of charge status.

### Data Interactions
* **Reads:** `TAMS_TOA`, `TAMS_TOA_Parties`  
* **Writes:** None